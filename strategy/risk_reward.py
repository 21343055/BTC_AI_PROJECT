def calculate_rr(
    entry,
    stop_loss,
    tp1,
    tp2
):

    risk = abs(
        entry - stop_loss
    )

    if risk == 0:

        return None

    reward1 = abs(
        tp1 - entry
    )

    reward2 = abs(
        tp2 - entry
    )

    rr1 = reward1 / risk

    rr2 = reward2 / risk

    return {

        "risk": float(risk),

        "reward1": float(reward1),

        "reward2": float(reward2),

        "rr1": float(rr1),

        "rr2": float(rr2)
    }