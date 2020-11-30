#Write a method to sort an array ot strings so that all tne anagrnms are next to
#each other.Time complexity O(n) space complexity O(1)
def anagramsort(list1):
    k = {}# create a dictionary
    for i in list1:
        x = ''.join(sorted(i))# sort the element in the list1
        if x in k:
            k[x].append(i) # append the element in the list inside the dict where  key exists

        else:
            k[x] = [i]# create a nelist with the key in the dictionary

    return list(k.values())


l= ["cat", "dog", "tac", "god", "act"]
print(anagramsort(l))