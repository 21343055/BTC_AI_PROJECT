def calculate_market_score(
    trend_1d,
    trend_4h,
    trend_1h,
    trend_15m,
    trend_5m,
    trend_1m,
    orderflow_bull,
    orderflow_bear,
    pattern_score=0
):

    score = 0

    # ==================================
    # 1D TREND
    # ==================================

    if trend_1d == "BULLISH":
        score += 4

    elif trend_1d == "BEARISH":
        score -= 4

    # ==================================
    # 4H TREND
    # ==================================

    if trend_4h == "BULLISH":
        score += 3

    elif trend_4h == "BEARISH":
        score -= 3

    # ==================================
    # 1H TREND
    # ==================================

    if trend_1h == "BULLISH":
        score += 2

    elif trend_1h == "BEARISH":
        score -= 2

    # ==================================
    # 15M TREND
    # ==================================

    if trend_15m == "BULLISH":
        score += 1

    elif trend_15m == "BEARISH":
        score -= 1

    # ==================================
    # 5M TREND
    # ==================================

    if trend_5m == "BULLISH":
        score += 1

    elif trend_5m == "BEARISH":
        score -= 1

    # ==================================
    # 1M TREND
    # ==================================

    if trend_1m == "BULLISH":
        score += 1

    elif trend_1m == "BEARISH":
        score -= 1

    # ==================================
    # ORDERFLOW
    # ==================================

    score += orderflow_bull
    score -= orderflow_bear

    # ==================================
    # CANDLESTICK PATTERN
    # ==================================

    score += pattern_score

    return score