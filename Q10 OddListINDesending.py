pids = [101, 84, 57, 93, 110, 77, 46, 121, 135, 92, 63]

odd_list = []

for i in pids:
    if i %2 != 0 :
        odd_list.append(i)
sorted_list = odd_list.sort(reverse=True)

print("Original List: ",pids)
print("The odd and Desending Sorted List: ",odd_list)