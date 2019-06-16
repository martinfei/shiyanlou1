import sys

for age in sys.argv[1:]:
    age1 = int(age)
    if 0 <= age1 < 10:
        print('you belong to kids')
    elif 10 <= age1 < 18:
        print('you belong to teenager')
    elif 18 <= age1 < 30:
        print('you belong to adult')
    elif 30 <= age1 < 60:
        print('you belong to older')
    else:
        print('you belong to oldest')
