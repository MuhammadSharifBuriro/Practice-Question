total = int(input("Enter Total bill: ")) 
if total > 5000 :
    print("Discount 20 is: ",20/100 *total)
elif total >3000 and total <4000 : 
    print("Discount 10 %",10/100 *total)
else :
    print("No discount")