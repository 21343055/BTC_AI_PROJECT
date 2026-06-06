import pandas as pd

from collector.client import (
    get_data
)

from config.settings import (
    OI_LIMIT
)


def get_open_interest_change(
    symbol="BTCUSDT"
):

    params = {

        "symbol": symbol,

        "period": "5m",

        "limit": OI_LIMIT
    }

    data = get_data(
        "/futures/data/openInterestHist",
        params
    )

    if not data:

        return 0

    df = pd.DataFrame(data)

    df["sumOpenInterest"] = (
        df["sumOpenInterest"]
        .astype(float)
    )

    df = df.sort_values(
        "timestamp"
    )

    oi_now = (
        df["sumOpenInterest"]
        .iloc[-1]
    )

    oi_prev = (
        df["sumOpenInterest"]
        .iloc[-2]
    )

    return (
        (
            oi_now
            - oi_prev
        )
        /
        oi_prev
    ) * 100