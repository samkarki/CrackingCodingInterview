#used some online resource  for this one, can't recall which one.
def countways(n):

    memo = {}
    if n in memo:
        return memo[n]
    if n ==0 or n==1:
        return 1
    elif n==2:
        return 2
    else:
        f = countways(n-1) + countways(n-2) + countways(n-3)
        memo[n] = f

    return f

print(countways(4))