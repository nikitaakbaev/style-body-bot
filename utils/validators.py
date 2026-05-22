MIN_MEASUREMENT = 40
MAX_MEASUREMENT = 200


def parse_measurement(value: str) -> float | None:
    normalized = value.strip().replace(",", ".")

    try:
        number = float(normalized)
    except ValueError:
        return None

    if MIN_MEASUREMENT <= number <= MAX_MEASUREMENT:
        return number

    return None
