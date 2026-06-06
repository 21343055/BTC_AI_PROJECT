import pandas as pd

from collector.client import (
    get_data
)

from config.settings import (
    FUNDING_LIMIT
)


def get_funding_rate(
    symbol="BTCUSDT"
):

    params = {

        "symbol": symbol,

        "limit": FUNDING_LIMIT
    }

    data = get_data(
        "/fapi/v1/fundingRate",
        params
    )

    if not data:

        return 0

    df = pd.DataFrame(data)

    df["fundingRate"] = (
        df["fundingRate"]
        .astype(float)
    )

    latest_funding = (
        df["fundingRate"]
        .iloc[-1]
    )

    return (
        latest_funding
        * 100
    )