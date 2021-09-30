height = int(input('введите высоту в символах :'))
width = height * 2

count = 1

for i in range(height):
    gap = int((width - count) / 2)
    line = (" " * gap) + ("*" * count)
    count += 2
    print(line)
