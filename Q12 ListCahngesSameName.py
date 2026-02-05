from collections import Counter
Names = ["Kazi","Muhammad","Sharif","Kazi"]

Unique_Names = []
seen = set ()

for name in Names :
    if name not in seen :   
        Unique_Names.append(name)
        seen.add(name)

counts = Counter(Names)
print("Unique names (order preserved):", Unique_Names)
print("\nOccurrences of each name:")
for name in Unique_Names:
    print(name, ":", counts[name])