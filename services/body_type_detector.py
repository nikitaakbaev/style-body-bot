BODY_TYPE_TITLES = {
    "pear": "Груша",
    "inverted_triangle": "Перевернутый треугольник",
    "apple": "Яблоко",
    "rectangle": "Прямоугольник",
    "hourglass": "Песочные часы",
}


def detect_body_type(bust: float, waist: float, hips: float) -> dict:
    bust_hips_diff = bust - hips
    max_min_diff = max(bust, waist, hips) - min(bust, waist, hips)

    if abs(bust_hips_diff) <= 5 and hips - waist >= 25 and bust - waist >= 20:
        body_type = "hourglass"
        reason = "Грудь и бедра близки по объему, а талия заметно уже."
    elif hips - bust >= 8:
        body_type = "pear"
        reason = "Бедра заметно шире груди, а талия выражена."
    elif bust - hips >= 8:
        body_type = "inverted_triangle"
        reason = "Грудь заметно шире бедер, поэтому верх визуально активнее нижней части."
    elif waist >= hips - 5 and waist >= bust - 8:
        body_type = "apple"
        reason = "Талия близка к груди и бедрам или выражена сильнее, чем бедра."
    elif max_min_diff <= 15:
        body_type = "rectangle"
        reason = "Грудь, талия и бедра близки по значениям, талия выражена мягко."
    else:
        body_type = "rectangle"
        reason = "Параметры близки к ровному силуэту без резкого перепада между зонами."

    return {
        "type": body_type,
        "title": BODY_TYPE_TITLES[body_type],
        "reason": reason,
        "confidence": "примерно",
    }
