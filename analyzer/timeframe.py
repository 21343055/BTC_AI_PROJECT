from collector.price import get_kline
from analyzer.trend import detect_trend


def get_trend(
    symbol="BTCUSDT",
    interval="15m"
):
    """
    Mengambil data kline lalu
    mengembalikan trend berdasarkan EMA20 vs EMA50
    """

    df = get_kline(
        symbol=symbol,
        interval=interval
    )

    return detect_trend(df)


def get_multi_timeframe_trend(
    symbol="BTCUSDT"
):
    """
    Mengambil trend dari beberapa timeframe:
    1m, 5m, 15m, 1h, 4h, 1d
    """

    intervals = [
        "1m",
        "5m",
        "15m",
        "1h",
        "4h",
        "1d"
    ]

    trends = {}

    for interval in intervals:

        try:

            df = get_kline(
                symbol=symbol,
                interval=interval
            )

            trends[interval] = (
                detect_trend(df)
            )

        except Exception as e:

            print(
                f"Error trend {interval}: {e}"
            )

            trends[interval] = "UNKNOWN"

    return trends