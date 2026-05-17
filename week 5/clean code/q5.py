def get_status(score):
    if score >= 90:
        return "excellent"
    elif score >= 70 and score < 90:
        return "good"
    elif score >= 55 and score < 70:
        return "average"
    elif score < 55:
        return "fail"
    return "unknown"


def is_valid_age(age):
    if isinstance(age, int) and age > 0 and age < 120:
         return True
    return False


def get_greeting(hour):
    if hour >= 5 and hour < 12:
        return "Good morning"
    elif hour >= 12 and hour < 17:
        return "Good afternoon"
    elif hour >= 17 and hour < 21:
        return "Good evening"
    elif hour >= 21 or hour < 5:
        return "Good night"


print(get_status(90))