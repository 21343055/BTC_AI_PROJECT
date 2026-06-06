def get_trade_quality(rr):

    if rr >= 3:
        return "A+"

    elif rr >= 2:
        return "A"

    elif rr >= 1.5:
        return "B"

    elif rr >= 1:
        return "C"

    return "AVOID"