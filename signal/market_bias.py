def get_market_bias(
    trend,
    orderflow_bull,
    orderflow_bear
):

    if (
        orderflow_bull >= 3
        and
        trend == "BEARISH"
    ):

        return "POTENTIAL BULLISH REVERSAL"

    elif (
        orderflow_bear >= 3
        and
        trend == "BULLISH"
    ):

        return "POTENTIAL BEARISH REVERSAL"

    elif (
        trend == "BULLISH"
        and
        orderflow_bull > orderflow_bear
    ):

        return "STRONG LONG"

    elif (
        trend == "BEARISH"
        and
        orderflow_bear > orderflow_bull
    ):

        return "STRONG SHORT"

    return "MIXED SIGNAL"