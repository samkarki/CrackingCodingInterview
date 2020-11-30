def magicindex(alist, start, end):


    while start <= end:
        mid = (start + end) // 2
        if alist[mid] == mid:
            return mid
        elif alist[mid] < mid:
            return magicindex(alist, mid + 1 , end)
        else:
            return magicindex(alist, start, mid -1)

    return -1


# alist= [-10, -1, 0, 3, 11, 30, 50, 100 ]
alist1= [-10, -5, 2, 2,2, 3, 4, 7, 9, 12, 13]
start = 0
end = len(alist1) - 1
print(magicindex(alist1, start, end))