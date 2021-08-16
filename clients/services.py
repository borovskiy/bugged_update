def telephone_check(enter_string_data: str) -> bool:
    """функция проверки числа на принадлежность к номеру телефона"""
    if ('8' or '7' == enter_string_data[0]) and len(enter_string_data) == 11:
        truncated_number = enter_string_data
    elif '+7' == enter_string_data[0:2]:
        truncated_number = enter_string_data[1:]

    else:
        return False
    if truncated_number.isdigit():
        return True
    else:
        return False
