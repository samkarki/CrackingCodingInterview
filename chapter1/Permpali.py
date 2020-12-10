import string
def canFormPalindrome(astring):

    sp = string.punctuation
    for i in astring:
        if i in sp:
            astring = astring.replace(i, '')

    astring = astring.lower()
    astring = astring.replace(' ','')

    c1 = [0] * 26
    for i in astring:
        pos = ord(i) - ord('a')
        c1[pos] = c1[pos] + 1

    odd_count = 0
    for i in range(len(c1)):
        if c1[i] % 2 == 1:
            odd_count += 1

        if odd_count > 1:
            return False


    return True


print(canFormPalindrome("Tact Coa"))
print(canFormPalindrome("Don't nod"))
print(canFormPalindrome('I did, did I?'))
print(canFormPalindrome('hello'))