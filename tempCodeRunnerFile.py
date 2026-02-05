pids = [101, 84, 57, 93, 110, 77, 46, 121, 135, 92, 63]

odd_list = []

for i in pids:
    if i %2 != 0 :
        odd_list.append(i)
print(odd_list)