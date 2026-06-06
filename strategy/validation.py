def validate_entry(
    current_price,
    entry
):

    distance = (
        abs(
            current_price
            - entry
        )
        /
        current_price
    ) * 100

    if distance < 0.30:

        status = "READY"

    elif distance < 1:

        status = "WAIT PULLBACK"

    else:

        status = "TOO FAR"

    return {

        "distance":
            float(distance),

        "status":
            status
    }

def final_trade_decision(
    market_state,
    trade_quality,
    setup_status
):

    if trade_quality == "AVOID":

        return "NO TRADE"

    if setup_status == "TOO FAR":

        return "NO TRADE"

    if market_state == "STRONG LONG":

        return "LONG"

    if market_state == "STRONG SHORT":

        return "SHORT"

    if market_state == "POTENTIAL BULLISH REVERSAL":

        return "WATCH LONG"

    if market_state == "POTENTIAL BEARISH REVERSAL":

        return "WATCH SHORT"

    return "NO TRADE"