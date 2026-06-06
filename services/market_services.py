from collector.price import (
    get_kline
)

from collector.funding import (
    get_funding_rate
)

from collector.open_interest import (
    get_open_interest_change
)

from collector.orderbook import (
    get_orderbook
)

from collector.aggtrade import (
    get_aggtrade
)


def load_market_data(
    symbol="BTCUSDT"
):

    df = get_kline(symbol)

    funding = (
        get_funding_rate(symbol)
    )

    oi_change = (
        get_open_interest_change(
            symbol
        )
    )

    orderbook = (
        get_orderbook(symbol)
    )

    aggtrade = (
        get_aggtrade(symbol)
    )

    market_data = {

        "df":
            df,

        "funding":
            funding,

        "oi_change":
            oi_change,

        "orderbook":
            orderbook,

        "aggtrade":
            aggtrade
    }

    return market_data