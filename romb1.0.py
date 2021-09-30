height = int(input('введите высоту в символах :'))
width = height * 2

count = 1

for i in range(height):
    gap = int((width - count) / 2)
    line = (" " * gap) + ("*" * count)
    count += 2
    print(line)

for i in range(height):
    count = 1 if i == height - 1 else 3
    gap = int((width - count) / 2)

    if count == 1:
        line = (" " * i) + "*"
    else:
        line = (" " * i) + "*" + (" " * gap) + "*" + (" " * gap) + "*"

    width -= 2
    print(line)