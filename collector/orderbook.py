from collector.client import (
    get_data
)

from config.settings import (
    DEPTH_LIMIT
)


def get_orderbook(
    symbol="BTCUSDT"
):

    params = {

        "symbol": symbol,

        "limit": DEPTH_LIMIT
    }

    depth = get_data(
        "/fapi/v1/depth",
        params
    )

    if not depth:

        return None

    bid_volume = sum(
        float(bid[1])
        for bid in depth["bids"]
    )

    ask_volume = sum(
        float(ask[1])
        for ask in depth["asks"]
    )

    imbalance = (
        bid_volume
        /
        (
            bid_volume
            + ask_volume
        )
    )

    largest_bid = max(
        depth["bids"],
        key=lambda x:
        float(x[1])
    )

    largest_ask = max(
        depth["asks"],
        key=lambda x:
        float(x[1])
    )

    return {

        "bid_volume":
            bid_volume,

        "ask_volume":
            ask_volume,

        "imbalance":
            imbalance,

        "buy_wall_price":
            float(
                largest_bid[0]
            ),

        "buy_wall_size":
            float(
                largest_bid[1]
            ),

        "sell_wall_price":
            float(
                largest_ask[0]
            ),

        "sell_wall_size":
            float(
                largest_ask[1]
            )
    }