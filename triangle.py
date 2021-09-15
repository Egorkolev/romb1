rows = int(input('введите высоту треугольника:'))
cols = 12

for i in range(rows):
    print(i, end='\t')
    for j in range(cols):
        if i == rows - 1:
            print('* ', end='')
        else:
            print(' ', end='')
    print()
