ages=  [15,22,37,42,19,28,33,45,17,29,52,39,14,31]

new_list = []
for i in ages :
    if i > 30 :
        new_list.append(i)
new_list.sort()

print("Original list: ",ages)
print("new list and sorted lsit : ",new_list)