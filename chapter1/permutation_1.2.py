# Time complexity O(n2) depends upon the type of sorting
def permutation(s1, s2):

    if len(s1) !=  len(s2):
        return False
    s1 = s1.lower()
    s2 = s2.lower()

    l1 = sorted(s1)
    astring = "".join(l1)

    l2 = sorted(s2)
    bstring = "".join(l2)

    for i in range(0, len(s1)):
        if astring[i] == bstring[i]:
            return True
    return False


# Time complexity O(n)
def permutation(s1, s2):
    if len(s1) !=  len(s2):
        return False

    # s1 = s1.lower()
    # s1 = s1.lower()

    c1= [0] * 128
    for i in range(0, len(s1)):
        pos = ord(s1[i])
        c1[pos] = c1[pos] + 1

    c2 = [0] * 128
    for i in range(0, len(s1)):
        pos = ord(s2[i])
        c2[pos] = c2[pos] + 1

    j = 0
    found = True

    while j < 128 and found:
        if c1[j] == c2[j]:
            return True
    return False

print(permutation('Heart','earth'))