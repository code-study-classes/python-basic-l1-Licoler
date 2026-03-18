db1 = [101, 102, 105, 108, 110]
db2 = [105, 199, 101, 115, 105]

common_users = []

for x in db1:
    if x in db2 and x not in common_users:
        common_users.append(x)

print("Совпадающие ID:", common_users)
