load = [10, 50, 20, 80, 30, 90, 40, 60, 10, 20]

smoothed_load = []

for i in range(len(load) - 2):
    part = load[i:i+3]
    avg = int(sum(part) / 3)
    smoothed_load.append(avg)

print("Исходная нагрузка:", load)
print("Сглаженный тренд:", smoothed_load)
