def detect_trend(
    df,
    fast_ema=20,
    slow_ema=50
):

    ema_fast = (
        df["close"]
        .ewm(
            span=fast_ema,
            adjust=False
        )
        .mean()
        .iloc[-1]
    )

    ema_slow = (
        df["close"]
        .ewm(
            span=slow_ema,
            adjust=False
        )
        .mean()
        .iloc[-1]
    )

    if ema_fast > ema_slow:
        return "BULLISH"

    return "BEARISH"