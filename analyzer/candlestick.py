def detect_pattern(df):

    last = df.iloc[-1]

    body = abs(
        last["close"]
        -
        last["open"]
    )

    if body == 0:

        return "NONE"

    upper_wick = (
        last["high"]
        -
        max(
            last["open"],
            last["close"]
        )
    )

    lower_wick = (
        min(
            last["open"],
            last["close"]
        )
        -
        last["low"]
    )

    if (
        lower_wick > body * 2
        and
        upper_wick < body
    ):

        return "HAMMER"

    elif (
        upper_wick > body * 2
        and
        lower_wick < body
    ):

        return "SHOOTING_STAR"

    return "NONE"