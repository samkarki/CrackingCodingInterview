#Time complexity O(n) and space complexity:O(1)
# def replace(astring):
#
#     alist= list(astring)
#
#     for i in range(len(alist)):
#         if alist[i] == ' ':
#             alist[i]= '%20'
#     return (''.join(alist))

#time complexity: O(n)

def replace(astring):
    astring = astring.strip()
    return astring.replace(' ','%20')


print(replace("Mr John Smith "))