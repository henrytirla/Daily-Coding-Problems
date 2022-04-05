""""This problem was recently asked by Google.

Given a list of numbers and a number k,
return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17,
return true since 10 + 7 is 17."""
def Suminlist(array,k):
    sums =[]
    for i in range(len(array) - 1):
        first_num = array[i]
        for j in range(i + 1,len(array)):
            second_num = array[j]
            if first_num + second_num == k:
                sums.extend((first_num,second_num))
    return sums,True






a =Suminlist([3,2,1,6],9)
print(a)