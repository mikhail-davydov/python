def is_good_password(st: str) -> bool:
    len_cond = len(st) >= 9
    upper_cond = any(True if c.isupper() else False for c in st)
    lower_cond = any(True if c.islower() else False for c in st)
    digit_cond = any(True if c.isdigit() else False for c in st)

    if not len_cond or not upper_cond or not lower_cond or not digit_cond:
        return False

    return True


print(is_good_password('МойПарольСамыйЛучший111'))


# course solution
def is_good_password(string):
    if len(string) < 9:
        return False

    has_upper = False
    has_lower = False
    has_digit = False

    for c in string:
        if c.isupper():
            has_upper = True
        elif c.islower():
            has_lower = True
        elif c.isdigit():
            has_digit = True

    return all([has_upper, has_lower, has_digit])


# alternative solution #1
def is_good_password(s: str):
    if all(
            (len(s) >= 9,
             any(c.islower() for c in s),
             any(c.isupper() for c in s),
             any(c.isdigit() for c in s))
    ):
        return True
    else:
        return False


# alternative solution #2
def is_good_password(p):
    return len(p) > 8 and p.upper() != p and p.lower() != p and any(i.isdigit() for i in p)
