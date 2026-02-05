# Initialize count of Armstrong numbers
count = 0

print("Armstrong numbers between 100 and 999:")

# Loop through numbers from 100 to 999
for num in range(100, 1000):
    # Extract digits
    hundreds = num // 100
    tens = (num // 10) % 10
    units = num % 10
    
    # Check if sum of cubes of digits equals the number
    if hundreds**3 + tens**3 + units**3 == num:
        print(num, end=" ")
        count += 1

print("\nTotal Armstrong numbers found:", count)
