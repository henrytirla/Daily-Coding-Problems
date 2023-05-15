"""Min Rewards
Imagine that you're a teacher who's just graded the final exam in a class.
You have a list of student scores on the final exam in a particular order (not necessarily sorted)
, and you want to reward your students.
You decide to do so fairly by giving them arbitrary rewards following two rules:

All students must receive at least one reward.
Any given student must receive strictly more rewards than an adjacent student
(a student immediately to the left or to the right) with a lower score
 and must receive strictly fewer rewards than an adjacent student with a higher score.

Write a function that takes in a list of scores and returns the minimum number
of rewards that you must give out to students to satisfy the two rules.

You can assume that all students have different scores; in other words, the scores are all unique.

Sample Input
scores = [8, 4, 2, 1, 3, 6, 7, 9, 5]
Sample Output
25 // you would give out the following rewards: [4, 3, 2, 1, 2, 3, 4, 5, 1]"""



def minRewards(scores):
    reward= [1 for _ in scores]

    for i in range(1,len(scores)):
        if scores[i] > scores[i-1]:

            reward[i] =reward[i-1] +1


    for i in reversed(range(len(scores)-2)):
          if scores[i] > scores[i+1]:
              reward[i]= max(reward[i],reward[i+1]+1)


    return sum(reward)






if __name__ == '__main__':
    scores = [8, 4, 2, 1, 3, 6, 7, 9, 5]
    print(minRewards(scores))


"""Time Complexity: O(n)
The time complexity of this solution is linear, or O(n), 
where n is the length of the input list. This is because 
we perform two separate passes over the list of scores - 
once from left to right, and once from right to left. 
Each pass takes O(n) time, but since they are not nested, 
the time complexities add together, resulting in 2*O(n). 
However, in Big O notation, we drop the constant, so the 
final time complexity remains O(n).

Space Complexity: O(n)
The space complexity of this solution is also O(n), where n is the 
length of the input list. This is because we create a new list called 
rewards that is the same length as the input list. All other variables 
used in the solution take constant space, so the overall space complexity is O(n)."""