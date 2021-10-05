height = int(input('введите высоту в символах :'))
width = height * 4

count = 1

for i in range(height):
    gap = int((width - count) / 2)
    line = (" " * gap) + ("*" * count)
    count += 4
    print(line)

for i in range(height):
    count = 1 if i == height - 1 else 3
    gap = int((width - count) / 2)

    if count == 1:
        line = (" " * (i * 2 + 1)) + "*"
    else:
        line = (" " * (i * 2)) + "*" + (" " * gap) + "*" + (" " * gap) + "*"

    width -= 4
    print(line)
