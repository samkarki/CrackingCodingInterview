# time complexity: O(mn) space complexity O(1)
def mergeSort(l1,l2):#
    x = []
    i = 0
    j = 0
    while (i < len(l1)) and (j < len(l2)):
        if l1[i] > l2[j]:
            x.append(l2[j])
            j = j + 1

        elif l1[i] < l2[j]:
            x.append(l1[i])
            i = i + 1
        else:
            x.append(l1[i])
            x.append(l2[j])
            i = i + 1
            j = j + 1

    while (i < len(l1)):
        x.append(l1[i])
        i = i + 1
    while (j < len(l2)):
        x.append(l2[j])
        j = j + 1

    return x

a=[10,12,13,14,18]
b=[16,17,19,20,22]
print(mergeSort(a,b))