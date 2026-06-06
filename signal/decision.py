def get_final_decision(score):

    if score >= 10:

        return "LONG"

    elif score <= -10:

        return "SHORT"

    elif score >= 4:

        return "WATCH LONG"

    elif score <= -4:

        return "WATCH SHORT"

    return "NO TRADE"