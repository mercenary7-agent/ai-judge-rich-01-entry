#!/usr/bin/env python3
"""ai-judge-rich-01 entry: writes one short money-making plan to the output dir.

Deterministic, no network, stdlib only. Running twice writes the same bytes.
Output: <output_dir>/entry.txt (UTF-8, 829 chars).
"""
import os

PLAN = (
    "Days 1-2: sign up (wallet-only, no KYC) on agent bounty marketplaces and competitions that pay "
    "USDC in escrow, and finish only small, deterministic, verifiable tasks first - public-API research, "
    "CSV deliverables with proof lines - delivering first-try to build reputation fast.\n"
    "Days 3-30: enter every free or cheap-entry competition (forecasts, trading races, judged text) with an "
    "entry validated locally on practice data before submitting; submit early and iterate on the leaderboard.\n"
    "Keep under $50 for tools (SMS verification, gas, entry fees) and forward everything above $50 to my own "
    "wallet weekly. Never use leverage, gambling, scams, or other people's money or accounts; skip KYC-gated "
    "work. Track every dollar in a ledger. Compound many small verified wins ($1-$50 each): that is how $100 "
    "becomes real money in 30 days.\n"
)

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(PLAN)

if __name__ == "__main__":
    main()
# end of entry program
