import pandas as pd

from collector.client import (
    get_data
)

from config.settings import (
    KLINE_LIMIT
)


def get_kline(
    symbol="BTCUSDT",
    interval="15m",
    limit=KLINE_LIMIT
):

    params = {

        "symbol": symbol,

        "interval": interval,

        "limit": limit
    }

    data = get_data(
        "/fapi/v1/klines",
        params
    )

    if not data:

        return pd.DataFrame()

    columns = [

        "open_time",
        "open",
        "high",
        "low",
        "close",
        "volume",

        "close_time",

        "quote_asset_volume",

        "number_of_trades",

        "taker_buy_base_volume",

        "taker_buy_quote_volume",

        "ignore"
    ]

    df = pd.DataFrame(
        data,
        columns=columns
    )

    df["open_time"] = pd.to_datetime(
        df["open_time"],
        unit="ms"
    )

    df["close_time"] = pd.to_datetime(
        df["close_time"],
        unit="ms"
    )

    numeric_cols = [

        "open",
        "high",
        "low",
        "close",
        "volume"
    ]

    df[numeric_cols] = (
        df[numeric_cols]
        .astype(float)
    )

    return df