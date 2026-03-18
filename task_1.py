import random

scores = []
for i in range(10):
    scores.append(random.randint(1, 100))

print("Исходные баллы:", scores)

mn = min(scores)
mx = max(scores)

print("Удаляем минимум:", mn)
print("Удаляем максимум:", mx)

scores.remove(mn)
scores.remove(mx)

print("Оставшиеся баллы:", scores)

avg = sum(scores) / len(scores)
print("Средний рейтинг:", avg)
