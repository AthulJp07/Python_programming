arr = list(map(int,input('Enter the elements of the array:').split()))
duplicates = []
seen = set()

for n in arr:
    if n in seen:
        if n not in duplicates:
            duplicates.append(n)
    else:
        seen.add(n)
if len(duplicates) == 0:
    print("No duplicate elements found in the array.")
else:
    print("Duplicate elements in the array are:", duplicates)