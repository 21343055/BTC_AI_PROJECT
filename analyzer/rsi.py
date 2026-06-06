def analyze_rsi(
    df,
    period=14
):

    delta = df["close"].diff()

    gain = delta.where(
        delta > 0,
        0
    )

    loss = -delta.where(
        delta < 0,
        0
    )

    avg_gain = (
        gain
        .rolling(period)
        .mean()
    )

    avg_loss = (
        loss
        .rolling(period)
        .mean()
    )

    rs = avg_gain / avg_loss

    rsi = (
        100
        -
        (
            100
            /
            (1 + rs)
        )
    ).iloc[-1]

    if rsi > 70:

        status = "OVERBOUGHT"

    elif rsi < 30:

        status = "OVERSOLD"

    else:

        status = "NEUTRAL"

    return {

        "value": float(rsi),

        "status": status
    }