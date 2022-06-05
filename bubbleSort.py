arrayToSort = [7,1,3,2,5,4,8,6,9,10]
print(arrayToSort)
# Loop to access each element in the array
for i in range(len(arrayToSort)):

    # Compare array elements loop
    for j in range(0, len(arrayToSort) - i - 1):
        if arrayToSort[j] > arrayToSort[j + 1]:
            temp = arrayToSort[j]
            arrayToSort[j] = arrayToSort[j+1]
            arrayToSort[j+1] = temp

print(arrayToSort)