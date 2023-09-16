from math import ceil


def calculate_total_amount(from_reserve, to_reserve, price):
    duration = (to_reserve - from_reserve).total_seconds() / (
        3600
    )  # Преобразуем разницу в секундах в количество часов
    duration_in_days = ceil(
        duration / 24
    )  # Пересчитываем в дни и округляем в большую сторону

    if duration_in_days <= 1:
        return price.one_day * duration_in_days
    elif 2 <= duration_in_days <= 3:
        return price.two_three_days * duration_in_days
    elif 4 <= duration_in_days <= 7:
        return price.four_seven_days * duration_in_days
    elif 8 <= duration_in_days <= 14:
        return price.eight_fourteen_days * duration_in_days
    elif duration_in_days >= 15:
        return price.fifteen_thirty_days * duration_in_days
    else:
        return 0
