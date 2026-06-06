def analyze_volume(
    df,
    period=20
):

    avg_volume = (
        df["volume"]
        .rolling(period)
        .mean()
        .iloc[-1]
    )

    current_volume = (
        df["volume"]
        .iloc[-1]
    )

    volume_ratio = (
        current_volume
        /
        avg_volume
    )

    if volume_ratio > 2:

        status = "VERY HIGH"

    elif volume_ratio > 1.5:

        status = "HIGH"

    elif volume_ratio < 0.7:

        status = "LOW"

    else:

        status = "NORMAL"

    return {

        "ratio": float(volume_ratio),

        "current_volume":
            float(current_volume),

        "average_volume":
            float(avg_volume),

        "status":
            status
    }