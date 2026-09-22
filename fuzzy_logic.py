def calculate_priority(difficulty, urgency, weakness):

    difficulty = difficulty / 100
    urgency = urgency / 100
    weakness = weakness / 100

    low_difficulty = max(0, 1 - difficulty * 2)
    medium_difficulty = max(0, 1 - abs(difficulty - 0.5) * 2)
    high_difficulty = max(0, (difficulty - 0.5) * 2)

    low_urgency = max(0, 1 - urgency * 2)
    medium_urgency = max(0, 1 - abs(urgency - 0.5) * 2)
    high_urgency = max(0, (urgency - 0.5) * 2)

    low_weakness = max(0, 1 - weakness * 2)
    medium_weakness = max(0, 1 - abs(weakness - 0.5) * 2)
    high_weakness = max(0, (weakness - 0.5) * 2)

    high_priority = max(
        min(high_difficulty, high_urgency),
        min(high_urgency, high_weakness),
        min(high_difficulty, high_weakness)
    )

    medium_priority = max(
        min(medium_difficulty, medium_urgency),
        min(medium_urgency, medium_weakness),
        min(medium_difficulty, medium_weakness)
    )

    low_priority = min(
        low_difficulty,
        low_urgency,
        low_weakness
    )

    numerator = (
        low_priority * 25 +
        medium_priority * 55 +
        high_priority * 85
    )

    denominator = (
        low_priority +
        medium_priority +
        high_priority
    )

    if denominator == 0:
        return 50

    priority = numerator / denominator

    return max(0, min(100, priority))