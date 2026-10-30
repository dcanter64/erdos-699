#!/usr/bin/env python3
"""
Regression test for sweep.py's hardened checkpoint loader
(review finding H1, fixed 2026-10-28).

The adversarial review planted a forged checkpoint
{"lo": 999, "hi": 999, "triples": 999999, "bad": []} under the name
block_000002_000051.json and the old loader silently accepted it,
corrupting the run total. This test plants that probe and several
variants and confirms read_checkpoint now rejects every one loudly
(SystemExit), while a genuine checkpoint produced by the real block
machinery is accepted with the exact closed-form count.

Run: python3 test_checkpoint_loader.py   (exit 0 iff all pass)
"""
import json
import os
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from counting import triples_in_range
import sweep
from sweep import read_checkpoint


def expect_reject(payload, lo, hi, label, raw=None):
    with tempfile.TemporaryDirectory() as td:
        f = os.path.join(td, f"block_{lo:06d}_{hi:06d}.json")
        with open(f, "w") as fh:
            fh.write(raw if raw is not None else json.dumps(payload))
        try:
            read_checkpoint(f, lo, hi)
        except SystemExit as e:
            print(f"  rejected ({label}): {e}")
            return
    raise AssertionError(f"forged checkpoint ACCEPTED: {label}")


def main():
    lo, hi = 2, 51
    good = triples_in_range(lo, hi)
    print(f"closed-form count for [{lo}, {hi}]: {good}")

    # The review's exact probe.
    expect_reject({"lo": 999, "hi": 999, "triples": 999999, "bad": []},
                  lo, hi, "review probe: wrong lo/hi, inflated count")
    # Right lo/hi, wrong count (incl. the silent-miss shape: a forged
    # file with correct count but a 'bad' list that hides real flags is
    # indistinguishable from genuine emptiness, which is why the count
    # and identity checks are the load-bearing ones; malformed or
    # out-of-block flag entries are rejected below).
    expect_reject({"lo": lo, "hi": hi, "triples": good + 1, "bad": []},
                  lo, hi, "inflated count")
    expect_reject({"lo": lo, "hi": hi, "triples": good - 1, "bad": []},
                  lo, hi, "deflated count")
    expect_reject({"lo": lo, "hi": hi, "triples": good,
                   "bad": [[9999, 3, 5]]},
                  lo, hi, "flagged triple outside block")
    expect_reject({"lo": lo, "hi": hi, "triples": good,
                   "bad": [[10, 5, 3]]},
                  lo, hi, "flagged triple with i > j")
    expect_reject({"lo": lo, "hi": hi, "triples": good,
                   "bad": [[10, 3, 4]]},
                  lo, hi, "flagged triple in closed region (2j <= 3i)")
    expect_reject({"lo": lo, "hi": hi, "triples": good, "bad": "none"},
                  lo, hi, "'bad' not a list")
    expect_reject({"lo": lo, "hi": hi, "triples": good,
                   "bad": [[10, 3]]},
                  lo, hi, "flagged entry not a triple")
    expect_reject(None, lo, hi, "truncated JSON",
                  raw='{"lo": 2, "hi": 51, "trip')
    expect_reject([1, 2, 3], lo, hi, "top level not an object")

    # Genuine acceptance: produce a real checkpoint with the block
    # machinery and confirm it loads with the exact count.
    sweep._init(hi)
    rlo, rhi, triples, bad = sweep.run_block((lo, hi))
    assert (rlo, rhi) == (lo, hi) and triples == good, (triples, good)
    with tempfile.TemporaryDirectory() as td:
        f = os.path.join(td, f"block_{lo:06d}_{hi:06d}.json")
        with open(f, "w") as fh:
            json.dump({"lo": rlo, "hi": rhi, "triples": triples,
                       "bad": bad}, fh)
        t, b = read_checkpoint(f, lo, hi)
        assert t == triples and b == [tuple(x) for x in bad]
    print(f"  accepted: genuine checkpoint for [{lo}, {hi}] "
          f"({triples} triples, {len(bad)} flagged)")
    print("ALL CHECKPOINT LOADER TESTS PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
