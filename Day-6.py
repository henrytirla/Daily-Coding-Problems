"""Given a word w and a string s, find all indices in s which are the starting locations
of anagrams of w. For example, given w is ab and s  is abxaba, return [ 0, 3, 4]."""

w ="ab"
s ="abxaba"
indices_array=[]
for i ,letter in enumerate(s):

    if s[i:i+2] == "ab" or s[i:i+2] == "ba":
        indices_array.append(i)


print(indices_array)







