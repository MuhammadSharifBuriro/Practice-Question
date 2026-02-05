numbers = list(map(int, input("Enter numbers separated by space: ").split()))


evenList = []
oddList = []

for i in numbers:
    if i % 2 == 0 :
        evenList.append(i)
    else :
        oddList.append(i)
print("Even Numbers: ",evenList)
print("Odd Numbers: ",oddList)