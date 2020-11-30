
def oneaway(s1,s2):
    if s1 == s2:
        return True
    m = len(s1)
    n= len(s2)

    if m == n:
        return equalSize(s1,s2)

    elif (m-n) > 1:
        return False

    elif m > n:
        larger = s1
        smaller = s2

    else:
        larger = s2
        smaller = s1

    return unequalSize(larger, smaller)

def equalSize(s1, s2):
    count = 0
    for i in range(s1):
        if s1[i] != s2[i]:
            count += 1

        if count > 1:
            return False
    return True

def unequalSize(larger, smaller):
    count = 0
    small_index = 0
    large_index = 0
    while small_index < len(smaller):
        if larger[large_index] != smaller[small_index]:
            count += 1
            large_index += 1

        else:
            small_index += 1
            large_index += 1

        if count > 1:
            return False
    return True

print(oneaway('pale','ple'))