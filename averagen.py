N = 10
count = 1
sum = 0
while count <= 10:
    num = int(input('Enter number:'))
    sum = sum + num
    count += 1

average = sum / N
print('N = {},sum = {}'.format(N,sum))
print('Average = {:.2f}'.format(average))
