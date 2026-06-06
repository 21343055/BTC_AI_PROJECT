def detect_market_regime(
    trend_1d,
    trend_4h,
    trend_1h,
    trend_15m,
    trend_5m,
    trend_1m,
    orderflow_bull,
    orderflow_bear
):

    # ==========================
    # Higher Timeframe
    # ==========================

    if (

        trend_1d == "BULLISH"
        and
        trend_4h == "BULLISH"
        and
        trend_1h == "BULLISH"

    ):

        return "TRENDING UP"

    if (

        trend_1d == "BEARISH"
        and
        trend_4h == "BEARISH"
        and
        trend_1h == "BEARISH"

    ):

        return "TRENDING DOWN"

    # ==========================
    # Reversal Detection
    # ==========================

    if (

        trend_1h == "BEARISH"
        and
        orderflow_bull >= 3

    ):

        return "POSSIBLE BULLISH REVERSAL"

    if (

        trend_1h == "BULLISH"
        and
        orderflow_bear >= 3

    ):

        return "POSSIBLE BEARISH REVERSAL"

    # ==========================
    # Default
    # ==========================

    return "RANGING"