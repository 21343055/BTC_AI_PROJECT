def calculate_position_size(
    account_size,
    risk_percent,
    entry,
    stop_loss
):

    max_risk = (
        account_size
        * risk_percent
        / 100
    )

    stop_distance = abs(
        entry - stop_loss
    )

    if stop_distance == 0:

        return None

    position_size = (
        max_risk
        / stop_distance
    )

    return {

        "max_risk":
            float(max_risk),

        "position_size":
            float(position_size)
    }