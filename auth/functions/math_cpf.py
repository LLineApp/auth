import re

BLANK_LIST = [11 * '0', 11 * '1', 11 * '2', 11 * '3', 11 *
              '4', 11 * '5', 11 * '6', 11 * '7', 11 * '8', 11 * '9']


def isCpfValid(cpf):
    if not isinstance:
        return False

    cpf = re.sub("[^0-9]", '', cpf)

    if cpf in BLANK_LIST:
        return False

    if len(cpf) != 11:
        return False

    sum = 0
    weight = 10

    for n in range(9):
        sum = sum + int(cpf[n]) * weight

        weight = weight - 1

    verifyingDigit = 11 - sum % 11

    if verifyingDigit > 9:
        firstVerifyingDigit = 0
    else:
        firstVerifyingDigit = verifyingDigit

    sum = 0
    weight = 11
    for n in range(10):
        sum = sum + int(cpf[n]) * weight

        weight = weight - 1
    verifyingDigit = 11 - sum % 11

    if verifyingDigit > 9:
        secondVerifyingDigit = 0

    else:
        secondVerifyingDigit = verifyingDigit

    if cpf[-2:] == "%s%s" % (firstVerifyingDigit, secondVerifyingDigit):
        return True

    return False
