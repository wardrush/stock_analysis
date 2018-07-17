"""
Weekly Rotation S&P 500

Objectives:
- Trade only long, large index stocks
- Only execute trades once a week
- Jump on upward trending stocks with expectation they will continue

Trading Universe:
- S&P 500

Filters:
- Minimum Average Volume (20 days) >= 1,000,000 shares
- Minimum Price >= 1 USD

Position Sizing:
- Maximum of 10 positions, so positions of 1/10 total equity

Entry Rules:
- End-of-week close of SPY >= 200-SMA with a 2% downside buffer
- 3-day RSI of a stock <= 50

Ranking:
- Stocks should be ranked by increasing 200-day ROC

Enter:
- Upon market open in new trading week

Exit:
- When stock is no longer in the top 10 S&P 500 ranked (replace with new outranker)
- When SPY is below the 200-SMA with a 2% downside buffer at end of week close
"""