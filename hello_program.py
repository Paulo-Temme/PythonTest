"""Ein einfaches Programm zum Abrufen von Aktienkursen."""

import argparse

import yfinance as yf


def main() -> None:
    """Gibt einen Gruß aus und zeigt den aktuellen Aktienkurs."""

    print("Hallo Ich bin eiin Program")

    parser = argparse.ArgumentParser(
        description="Zeigt den aktuellen Schlusskurs einer Aktie von Yahoo Finance."
    )
    parser.add_argument(
        "symbol",
        help="Ticker-Symbol der Aktie, z.B. AAPL",
    )
    args = parser.parse_args()

    ticker = yf.Ticker(args.symbol)
    hist = ticker.history(period="1d")
    if hist.empty:
        print(f"Keine Daten für {args.symbol} gefunden.")
    else:
        current = hist["Close"].iloc[-1]
        print(f"Aktueller Schlusskurs von {args.symbol}: {current:.2f}")


if __name__ == "__main__":
    main()
