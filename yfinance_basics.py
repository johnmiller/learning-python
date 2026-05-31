"""Small tutorial script for learning the yfinance library.

Run:
    py ./yfinance-basics.py

Optional plotting support:
    py -m pip install matplotlib
"""

from __future__ import annotations

import yfinance as yf
import pandas as pd


def print_header(title: str) -> None:
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


def example_1_single_ticker_info() -> None:
    """Show basic company information for one ticker."""
    print_header("Example 1: Single Ticker Fundamentals (MSFT)")

    msft = yf.Ticker("MSFT")
    info = msft.info

    keys_to_show = [
        "longName",
        "sector",
        "industry",
        "country",
        "marketCap",
        "trailingPE",
        "dividendYield",
    ]

    for key in keys_to_show:
        print(f"{key:14}: {info.get(key)}")


def example_2_price_history() -> None:
    """Get recent historical price data."""
    print_header("Example 2: Price History")

    msft = yf.Ticker("MSFT")
    history_5d = msft.history(period="5d")
    print("MSFT 5-day history:")
    print(history_5d[["Open", "High", "Low", "Close", "Volume"]].tail())


def collect_fields(tickers: list[str], fields: list[str]) -> pd.DataFrame:
    """Collect selected fields from ticker .info into a DataFrame."""
    rows = []

    for ticker in tickers:
        info = yf.Ticker(ticker).info
        row = {"Ticker": ticker}
        for field in fields:
            row[field] = info.get(field)
        rows.append(row)

    return pd.DataFrame(rows)


def example_3_compare_companies() -> None:
    """Compare a few companies on selected metrics."""
    print_header("Example 3: Compare Company Fields")

    tickers = ["WMT", "MO", "NVDA", "CRM"]
    fields = ["sector", "industry", "currentRatio", "quickRatio", "trailingPE"]
    comparison = collect_fields(tickers, fields)
    print(comparison)


def example_4_download_multiple_tickers() -> pd.DataFrame:
    """Download OHLCV data for multiple symbols at once."""
    print_header("Example 4: Download Multiple Tickers")

    symbols = ["MSFT", "AAPL", "GOOGL", "SPY"]
    prices = yf.download(
        tickers=symbols,
        period="6mo",
        interval="1d",
        auto_adjust=True,
        progress=False,
        group_by="column",
    )

    close_prices = prices["Close"]
    print("Adjusted close prices (last 5 rows):")
    print(close_prices.tail())
    return close_prices


def example_5_returns_analysis(close_prices: pd.DataFrame) -> None:
    """Use pandas to compute returns and simple risk stats."""
    print_header("Example 5: Returns Analysis With pandas")

    daily_returns = close_prices.pct_change().dropna()

    summary = pd.DataFrame(
        {
            "avg_daily_return": daily_returns.mean(),
            "daily_volatility": daily_returns.std(),
            "best_day": daily_returns.max(),
            "worst_day": daily_returns.min(),
        }
    )

    print("Daily return summary:")
    print(summary)

    cumulative = (1 + daily_returns).cumprod() - 1
    print("\nCumulative return over period:")
    print(cumulative.tail(1).T.rename(columns={cumulative.index[-1]: "cum_return"}))


def example_6_financial_statements() -> None:
    """Access annual financial statement data."""
    print_header("Example 6: Financial Statements")

    nvda = yf.Ticker("NVDA")
    income_stmt = nvda.financials

    if income_stmt.empty:
        print("No income statement data returned.")
        return

    print("NVDA annual income statement (top rows):")
    print(income_stmt.head(8))


def example_7_optional_plot(close_prices: pd.DataFrame) -> None:
    """Optional chart if matplotlib is installed."""
    print_header("Example 7: Optional Plot")

    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib not installed. Install with: py -m pip install matplotlib")
        return

    normalized = close_prices / close_prices.iloc[0] * 100
    ax = normalized.plot(figsize=(10, 5), title="Normalized Prices (start = 100)")
    ax.set_ylabel("Indexed Price")
    plt.tight_layout()
    plt.show()


def main() -> None:
    print_header("yfinance Tutorial Script")
    print("This script demonstrates practical yfinance + pandas workflows.")

    example_1_single_ticker_info()
    example_2_price_history()
    example_3_compare_companies()
    close_prices = example_4_download_multiple_tickers()
    example_5_returns_analysis(close_prices)
    example_6_financial_statements()
    example_7_optional_plot(close_prices)


if __name__ == "__main__":
    main()