def calculate_orderflow_score(
    orderbook_bias,
    buy_wall_size,
    sell_wall_size,
    aggressor,
    cvd_bias
):

    bull = 0
    bear = 0

    # Orderbook

    if orderbook_bias == "BULLISH":

        bull += 1

    elif orderbook_bias == "BEARISH":

        bear += 1

    # Liquidity Wall

    if buy_wall_size > sell_wall_size:

        bull += 1

    elif sell_wall_size > buy_wall_size:

        bear += 1

    # Aggressor

    if aggressor == "BUYER":

        bull += 1

    elif aggressor == "SELLER":

        bear += 1

    # CVD

    if cvd_bias == "BULLISH":

        bull += 1

    elif cvd_bias == "BEARISH":

        bear += 1

    return bull, bear