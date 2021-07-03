def dezi_to_bin(number: int) -> str:
    zw_summe: int = number
    result: str = ""

    while zw_summe > 1:
        rest = zw_summe % 2
        result += f"{str(rest)}"
        zw_summe = int(zw_summe / 2)
    result += f"{str(zw_summe)}"
    result = result[::-1]

    return result


def bin_to_dezi(bin_num: str) -> int:
    exp: list = [x for x in range(len(bin_num)-1, -1, -1)]
    dezi_sum = 0

    for ziffer in range(len(bin_num)):
        dezi_sum += int(bin_num[ziffer]) * 2 ** exp[ziffer]

    return dezi_sum


def switch_hex(case: int) -> str:
    if case == 10:
        case = 'A'
        return case
    elif case == 11:
        case = 'B'
        return case
    elif case == 12:
        case = 'C'
        return case
    elif case == 13:
        case = 'D'
        return case
    elif case == 14:
        case = 'E'
        return case
    elif case == 15:
        case = 'F'
        return case
    else:
        case = case
        return str(case)


def dezi_to_hex(number: int) -> str:
    zw_summe: int = number
    result: str = ""
    digits = []

    if zw_summe < 16 and zw_summe > 9:
        result = switch_hex(zw_summe)
    elif zw_summe < 10:
        result = f"{number}"
    else:
        while zw_summe >= 16:
            rest = zw_summe % 16
            if rest > 9:
                rest = switch_hex(rest)
            zw_summe = int(zw_summe / 16)
            digits.append(rest)
            if zw_summe < 16 and zw_summe > 9:
                digits.append(switch_hex(zw_summe))
            elif zw_summe < 10:
                digits.append(zw_summe)
        for dig in digits:
            result += f"{str(dig)}"
        result = result[::-1]

    return result


def switch_dezi(case: str) -> int:
    if case == 'A':
        case = 10
        return case
    elif case == 'B':
        case = 11
        return case
    elif case == 'C':
        case = 12
        return case
    elif case == 'D':
        case = 13
        return case
    elif case == 'E':
        case = 14
        return case
    elif case == 'F':
        case = 15
        return case
    else:
        case = case
        return int(case)


def hex_to_dezi(hex_number: str) -> int:
    exp: list = [x for x in range(len(hex_number) - 1, -1, -1)]
    dezi_sum = 0
    nummer = 0

    for ziffer in range(len(hex_number)):
        if hex_number[ziffer] is not type(int):
            nummer = switch_dezi(hex_number[ziffer])
        dezi_sum += nummer * 16 ** exp[ziffer]

    return dezi_sum
