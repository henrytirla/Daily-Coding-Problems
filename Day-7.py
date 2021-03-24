"""Given a list of words, find all pairs of unique indices such that the concatenation of
the two words is a palindrome.
For example, given the list ['code','edoc','da','ad'],
return [ ( 0, 1), ( 1,0), (2, 3)]."""
#
# words =['code','edoc','da','ad']
# all_pairs=[]
# for i  in range(len(words)):
#     #print(words[i])
#     first_word =words[i]
#     for j in range(len(words)):
#         #print(words[j],"---j")
#         second_word = words[j]
#         if first_word  == second_word[::-1]:
#             all_pairs.append((i,j))
# print(all_pairs)

def is_palindrome(word):
    return word== word[::-1]
def palindrome_pairs(words):
    result = []
    for i, wordl in enumerate(words):
        for j, word2 in enumerate(words):
            if i == j:
               continue
            if is_palindrome(wordl + word2):
               result.append((i, j))
    return result

print(palindrome_pairs(['code','edoc','da','ad']))
        