__author__ = 'effy'

'''
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

there are two conditions to be satisfied, separate to one condition for each.
and create solutions for both of them and then merge to final solution
'''
class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):

        l = len(ratings)

        left = [1]*l

        for i in range(1,l):
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1]+1
            else:
                left[i] = 1

        right = left[:]

        for i in range(l-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                right[i] = max(right[i+1]+1, right[i])
            else:
                right[i] = left[i]

        return sum(right)



class Solution_secondround:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        l = len(ratings)
        left = [1]*l
        for i in range(1,l):
            if ratings[i]>ratings[i-1]:
                left[i] = left[i-1]+1
        right = left[:]
        for i in range(l-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                right[i] = max(left[i], right[i+1]+1)
        return sum(right)


class Solution_3rd:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        candies = [1 for i in range(len(ratings))]
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1]+1
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1]+1)
        return sum(candies)