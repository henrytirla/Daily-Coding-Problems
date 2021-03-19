"""Given a word w and a string s, find all indices in s which are the starting locations
of anagrams of w. For example, given w is ab and s  is abxaba, return [ 0, 3, 4]."""

w ="ab"
s ="abxaba"
indices_array=[]
for i ,letter in enumerate(s):
    count = 0
    if s[i:i+2] == "ab" or s[i:i+2] == "ba":
        count +=1
        indices_array.append(i)


print(indices_array)







