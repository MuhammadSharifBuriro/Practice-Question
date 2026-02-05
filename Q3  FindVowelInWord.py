# word = input("Enter a word: ")

# count = 0
# vowels = "aeiouAEIOU"
# for ch in word :
#     if ch in vowels :
#      count += 1 
# print ("Number of vowel Contain in this Word is: ",count)


word = input("Enter a word: ")

count = 0
vowel = "aeiouAEIOU"

for ch in word :
    if ch in vowel :
        count += 1 
print ("Vowel in this word is: ", count)