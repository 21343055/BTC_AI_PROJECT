from collector.client import (
    get_data
)

from config.settings import (
    TRADE_LIMIT
)


def get_aggtrade(
    symbol="BTCUSDT"
):

    params = {

        "symbol": symbol,

        "limit": TRADE_LIMIT
    }

    trades = get_data(
        "/fapi/v1/aggTrades",
        params
    )

    if not trades:

        return None

    buy_volume = 0

    sell_volume = 0

    cvd = 0

    for trade in trades:

        qty = float(
            trade["q"]
        )

        if trade["m"]:

            sell_volume += qty
            cvd -= qty

        else:

            buy_volume += qty
            cvd += qty

    delta = (
        buy_volume
        - sell_volume
    )

    return {

        "buy_volume":
            buy_volume,

        "sell_volume":
            sell_volume,

        "delta":
            delta,

        "cvd":
            cvd
    }