def get_support_resistance(
    df,
    lookback=20
):

    support = (
        df["low"]
        .tail(lookback)
        .min()
    )

    resistance = (
        df["high"]
        .tail(lookback)
        .max()
    )

    return support, resistance