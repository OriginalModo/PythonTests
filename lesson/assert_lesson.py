#Задача ПАРОЛЬ
#Написать функцию проверки "силы" пароля, возвращает всегда строку
# - если пароль короче 8 символов то вернуть Too Weak
# - если пароль содержит только цифры, только строчные, только заглавные то вернуть Too Weak
# - если пароль содержит символы любых 2 наборов вернуть Good
# - если пароль содержит символы любых 3 наборов вернуть Very Good

import string


def password_strength(value: str) -> str:
    if len(value) < 8:
        return 'Too Weak'
    digits = string.digits
    lowers = string.ascii_lowercase
    uppers = string.ascii_uppercase
    countt = 0
    for symbols in (digits, lowers, uppers):
        if any(i in symbols for i in value):
            countt += 1
            continue
    if countt == 3:
        return 'Very Good'
    return 'Weak' if countt == 1 else 'Good'
    # if all(i in digits for i in value) or all(i in lowers for i in value) or all(i in uppers for i in value):
    #     return 'Weak'
    # if any(i in digits for i in value) and any(i in lowers for i in value) and any(i in uppers for i in value):
    #     return 'Very Good'
    # if (any(i in digits for i in value) and any(i in lowers for i in value)) or (
    #         any(i in digits for i in value) and any(i in uppers for i in value)) or (
    #         any(i in lowers for i in value) and any(i in uppers for i in value)):
    # return 'Good'


if __name__ == '__main__':
    assert password_strength('') == 'Too Weak'
    assert password_strength('1234567') == 'Too Weak'
    assert password_strength('qwertya') == 'Too Weak'
    assert password_strength('QWERTYA') == 'Too Weak'
    assert password_strength('QAaa1') == 'Too Weak'
    assert password_strength('12345678') == 'Weak'
    assert password_strength('12345678233') == 'Weak'
    assert password_strength('aqwertya') == 'Weak'
    assert password_strength('aqwertyaasdd') == 'Weak'
    assert password_strength('QASDFERT') == 'Weak'
    assert password_strength('QASDFERTADSD') == 'Weak'
    assert password_strength('1234qasd') == 'Good'
    assert password_strength('1234QSDF') == 'Good'
    assert password_strength('1234QSDFAS') == 'Good'
    assert password_strength('ascvQSDF') == 'Good'
    assert password_strength('ascvQSDAF') == 'Good'
    assert password_strength('ascv12QSDAF') == 'Very Good'
    assert password_strength('123456aQ') == 'Very Good'
    assert password_strength('aaaaaaaA1') == 'Very Good'
    assert password_strength('QQQSSSSSSS1a') == 'Very Good'
    print('Good news!')
