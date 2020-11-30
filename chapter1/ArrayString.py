#Algorithm to determine if a string has all unique characters
#Brute force: time complexity O(n2)
def unique(astring):
    for i in range(len(astring)):
        for j in range(i+1, len(astring)):
            if astring[i] == astring[j]:# list has duplicate item
                return False
    return True
# -----------------------------------------------------------------------------------------------
#Time complexity O(n)
def unique(astring):

    alist = set()

    for char in astring:
        if char in alist:
            return False
        else:
            alist.add(char)
    return True
# ----------------------------------------------------------------------------------------------------------
#Time complexity : o(n)
def unique(astring):
    if len(astring) > 128:
        return False

    data_set = [False] * 128

    for i in range(0,len(astring)):
        position = ord(astring[i])

        if data_set[position] == True:#character exists in the list(duplicate character)
            return False
        data_set[position] = True# character not in the list , update position value to True

    return True


print(unique('hello'))
print(unique('halo'))

