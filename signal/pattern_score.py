def calculate_pattern_score(pattern):

    score = 0

    if pattern == "HAMMER":
        score += 1

    elif pattern == "SHOOTING_STAR":
        score -= 1

    return score