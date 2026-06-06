def generate_entry(
    market_state,
    buy_wall_price,
    sell_wall_price,
    support,
    resistance,
    atr,
    tp2_multiplier=1.0
):

    # ==========================
    # LONG SETUP
    # ==========================

    if market_state in [
        "STRONG LONG",
        "POTENTIAL BULLISH REVERSAL"
    ]:

        entry = buy_wall_price

        stop_loss = (
            support
            - (atr * 0.5)
        )

        tp1 = resistance

        tp2 = (
            resistance
            + (atr * tp2_multiplier)
        )

    # ==========================
    # SHORT SETUP
    # ==========================

    elif market_state in [
        "STRONG SHORT",
        "POTENTIAL BEARISH REVERSAL"
    ]:

        entry = sell_wall_price

        stop_loss = (
            resistance
            + (atr * 0.5)
        )

        tp1 = support

        tp2 = (
            support
            - (atr * tp2_multiplier)
        )

    # ==========================
    # NO SETUP
    # ==========================

    else:

        return None

    return {

        "entry":
            float(entry),

        "stop_loss":
            float(stop_loss),

        "tp1":
            float(tp1),

        "tp2":
            float(tp2)
    }