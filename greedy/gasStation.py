__author__ = 'effy'
# -*- coding: utf-8 -*-
'''
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i
to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Thought:
If the circuit is possible, i.e. ∑gas ≥ ∑cost. Then once computed the minimum extra gas needed for the circular route
, the minimum extra gas if we start on the next position is the same but not counting the previous position.

首先，如果sum(gas) >= sum(cost)的话，那么肯定有一个station是可以走完一个circle的，而如果sum(gas)<sum(cost)的话，那么一定无解。
这里用diff表示走完一站邮箱剩下的油，如果加上gas[i]也到不了下一站，那么继续将i+1设置为起点，然后再检查。 为什么直接跳到i+1呢？很简单，
因为要是从last start point走不到i+1, 那么在last start point与i+1之间的station都不可能走到i+1 -----因为在连贯的一条路线中任意一个station
的起始值至少都是>=0的（因为diff>=0才会向前），而从任意一个station起始的话，diff只能为0，所以更不可能走到i+1！

并且在check过sum(gas)与sum(cost)之后，如果sum(gas)>sum(cost)，那么必定有一个能完成circle的station，我们只要遍历一遍，一边遍历一边做
“排除法”就好了，最后一个start point就是那个start station。
'''

class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1
        n = len(gas)
        diff = 0
        stationIndex = 0
        for i in range(n):
            if gas[i]+diff < cost[i]:
                stationIndex = i+1
                diff = 0
            else:
                diff += gas[i]-cost[i]
        return stationIndex


class Solution_secondround:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        if sum(gas)<sum(cost):
            return -1
        l = len(gas)
        start = 0
        gas_left = 0
        for i in range(l):
            gas_left += gas[i]
            ## if current point can not be start point, check for the next one
            ## and reset gas_left to 0
            if gas_left < cost[i]:
                start = i+1
                gas_left = 0
            ## otherwise current start point still has the hope to reach the end
            ## reduce gas_left with current cost
            else:
                gas_left -= cost[i]
        return start