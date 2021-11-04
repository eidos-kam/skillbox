print('Задача 9. Аннуитетный платёж')

# Кредит в сумме S млн руб.,
# выданный на n лет под i% годовых,
# подлежит погашению равными ежегодными выплатами в конце каждого года,
# включающими процентные платежи и сумму в погашение основного долга.
#
# Проценты начисляются в один раз в год.
# После выплаты третьего платежа
# достигнута договорённость между кредитором и заёмщиком
# о продлении срока погашения займа на n_2 лет
# и увеличении процентной ставки с момента конверсии до i_2%.
#
# Напишите программу,
# которая выводит план погашения оставшейся части долга.
#
# A = KS
#
# K = i(1 + i) ** n / (1 + i) ** n - 1
#
# Пример:
#
# Введите сумму кредита: 40e6
# На сколько лет выдан? 5
# Сколько процентов годовых? 6
#
# Период: 1
#
# Остаток долга на начало периода: 40000000.0
# Выплачено процентов: 2400000.0
# Выплачено тела кредита: 7095856.02
#
#
# Период: 2
#
# Остаток долга на начало периода: 32904143.98
# Выплачено процентов: 1974248.6387999998
# Выплачено тела кредита: 7521607.3812
#
# Период: 3
#
# Остаток долга на начало периода: 25382536.5988
# Выплачено процентов: 1522952.195928
# Выплачено тела кредита: 7972903.824072
#
# Остаток долга: 17409632.774728
#
# =================================================
#
# На сколько лет продляется договор? 2
# Увеличение ставки до: 10
#
# Период: 1
#
# Остаток долга на начало периода: 17409632.774728
# Выплачено процентов: 1740963.2774728
# Выплачено тела кредита: 3751267.5625271997
#
# Период: 2
#
# Остаток долга на начало периода: 13658365.2122008
# Выплачено процентов: 1365836.52122008
# Выплачено тела кредита: 4126394.3187799198
#
# Период: 3
#
# Остаток долга на начало периода: 9531970.89342088
# Выплачено процентов: 953197.0893420881
# Выплачено тела кредита: 4539033.750657911
#
# Период: 4
#
# Остаток долга на начало периода: 4992937.142762969
# Выплачено процентов: 499293.71427629696
# Выплачено тела кредита: 4992937.125723703
#
# Остаток долга: 0.017039266414940357


def get_input_float_data(input_string: str):
    """
    проверка вводимого значения на предмет возможности приведения
    к полоижетльному действительному числу (тип float без знака)
    :param input_string:
    :return:
    """
    while True:
        result_item = input(input_string)
        if result_item.replace('.', '', 1).isdigit() and float(result_item) > 0:
            return float(result_item)
        else:
            print("Вы ошиблись при вводе")


def get_input_int_data(input_string: str):
    """
    проверка вводимого значения на предмет возможности приведения к полоижетльному целому числу (тип int без знака)
    :param input_string:
    :return:
    """
    while True:
        result_item = input(input_string)
        if result_item.isdigit() and int(result_item) > 0:
            return int(result_item)
        else:
            print("Вы ошиблись при вводе")


def calculate_annuity(total_debt: float, total_years: int, percents_by_period: float):
    """
    расчет аннутитетного платежа
    :param total_debt: сумма кредита
    :param total_years: срок кредита
    :param percents_by_period: процентов за период (1 год)
    :return: вовзрашает размер аннуитетного платежа
    """
    annuity_k = percents_by_period * (1 + percents_by_period) ** total_years / \
              ((1 + percents_by_period) ** total_years - 1)
    return total_debt * annuity_k


def calculate_payments(total_debt: float, total_years: int, percents_by_period: float, **kwargs):
    """
    выводит график гашения процентов и основного долга за срок кредита
    :param total_debt: сумма кредита
    :param total_years: срок кредита
    :param percents_by_period: процентов за период (1 год)
    :param kwargs: дополнительный параметр steps для прерывания расчета по первому графику гашения
    :return: возвращает остаток основного долга по кредиту
    """
    annuity = calculate_annuity(total_debt, total_years, percents_by_period)
    steps = kwargs.get('steps', total_years)
    for year in range(1, steps + 1):
        percents_payed = total_debt * percents_by_period
        credit_body = annuity - percents_payed
        print("\nПериод:", year)
        print("\nОстаток долга на начало периода:", round(total_debt, 2))
        print("Выплачено процентов:", round(percents_payed, 2))
        print("Выплачено тела кредита:", round(credit_body, 2))
        total_debt -= credit_body
    return total_debt


total_debt = get_input_float_data("Введите сумму кредита: ")
total_years = get_input_int_data("Срок кредита: ")
percents_by_period = get_input_int_data("Процентов годовых: ") / 100


total_debt = calculate_payments(total_debt, total_years, percents_by_period, steps=3)
print(f"\nОстаток долга: {round(total_debt, 2)} \n{'=' * 40}")

total_years = get_input_int_data("На сколько лет продляется договор? ") + 2
percents_by_period = get_input_int_data("Увеличение ставки до: ") / 100


total_debt = calculate_payments(total_debt, total_years, percents_by_period)
print(f"\nОстаток долга: {round(total_debt, 2)}")
