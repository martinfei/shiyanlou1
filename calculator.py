import sys
from collections import namedtuple

IncomeTaxQuickLooKupItem = namedtuple('IncomeTaxQuickLooKupItem',
        ['start_point','tax_rate','quick_subtractor'])

INCOME_TAX_START_POINT = 5000

INCOME_TAX_QUICK_LOOKUP_TABLE = [
        IncomeTaxQuickLooKupItem(80000,0.45,15160),
        IncomeTaxQuickLooKupItem(55000,0.35,7160),
        IncomeTaxQuickLooKupItem(35000,0.30,4410),
        IncomeTaxQuickLooKupItem(25000,0.25,2660),
        IncomeTaxQuickLooKupItem(12000,0.2,1410),
        IncomeTaxQuickLooKupItem(3000,0.1,210),
        IncomeTaxQuickLooKupItem(0,0.03,0)
        ]


SOCIAL_INSURANCE_MONEY_RATE = {
        'endowment_insurance': 0.08,
        'medical_insurance': 0.02,
        'unemployment_insurance': 0.005,
        'employment_injury_insurance': 0,
        'maternity_insurance': 0,
        'public_accumulation_funds': 0.06
}


def calc_income_tax_and_remain(income):
    social_insurance_money = income * sum(SOCIAL_INSURANCE_MONEY_RATE.values())
    real_income = income - social_insurance_money
    taxable_part = real_income - INCOME_TAX_START_POINT 

    for item in INCOME_TAX_QUICK_LOOKUP_TABLE:
        if taxable_part > item.start_point:
            tax = taxable_part * item.tax_rate - item.quick_subtractor
            return '{:.2f}'.format(tax),'{:.2f}'.format(real_income -tax)
    return '0.00','{:.2f}'.format(real_income)


def main():
    for arg in sys.argv[1:]:
        employee_id,income_string = arg.split(':')
        try:
            income = int(income_string)
        except ValueError:
            print('Parameter Error')
            continue

        _,remain = calc_income_tax_and_remain(income)
        print('{}:{}'.format(employee_id,remain))



if __name__ == '__main__':
    main()
