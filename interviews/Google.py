__author__ = 'effy'
# -*- coding: utf-8 -*-
'''
Product of word length which words that share no letters(all lower case)
E.g {feed , see, stuck }: max product:
5×4=20 Complexity?
Follow up:optimal way to exit earlier in loop.
'''
def encode(s):
    encoded = 0
    for char in s:
        encoded |= 1<<(ord(char)-ord('a'))
    return encoded

def no_overlap(s1,s2):
    return (encode(s1) & encode(s2)) == 0

def maxProduct(words):
    encode_array = []
    for word in words:
        encode_array.append(encode(word))
    ## associated array indices with words
    indices = range(len(words))
    indices.sort(key=lambda i:len(words[i]))
    indices.reverse()
    max_len_product = 0
    for i in range(len(words)):
        index1 = indices[i]
        for j in range(i+1,len(words)):
            index2 = indices[j]
            if no_overlap(encode_array[index1], encode_array[index2]):
                max_len_product = max(max_len_product, len(words[index1])*len(words[index2]))
                break
    return max_len_product



'''
2. RLE run-length compression aaaaabbbccc ->a5b3c3
'''
def rle(s):
    prev = s[0]
    res = ''
    count = 1
    for i in range(1,len(s)):
        if s[i] != prev:
            res += prev + str(count)
            count = 1
            prev = s[i]
        else:
            count += 1
    res+= prev+str(count)
    return res
#print rle('aaaaabbbccc')

'''
(3)完全平方解集，做一个：int minsol（int i）。
比如1=1^2 所以minsol(1)返回1,
2=1^2+1^2 返回2,
4=2^2或者4个1^2,1比4小， 返回1，
12=2^2+2^2+2^2或者3^2+3个1^2返回3.
'''
import math
def minsol(num):
    ways = [i for i in range(num+1)]
    for i in range(2,num+1):
        for j in range(i):
            gap = i-j
            if gap > 1 and int(math.sqrt(gap)) **2 == gap:
                ways[i] = min(ways[i], ways[j]+1)
    return ways[-1]
print minsol(12)
'''
Encode: helll=> he3xl,
decodeRequirements:
1. Decode(encode(s))==s;
2. Shortest length
Follow up: unit test: test requirement 12
'''
def decode(s):
    res = ''
    l = len(s)
    i = 0
    while i < l:
        if s[i] == 'x':
            if i>0 and i<l-1 and s[i-1].isdigit and not s[i+1].isdigit:
                if s[i-1] != 0:
                    res.append(s[i+1]*int(s[i-1]))
                elif s[i-1] == 0 and i-2>=0 and s[i-2].isdigit:
                    res.append(s[i+1]*int(s[i-2:i]))
                else:
                    res.append()

        else:
            res += s[i]
        i += 1
    return res

'''
4. Poland operation list convert to tree
E.g. {push 4, push 5, add, push 9, mul, sqrt} => tree: {sqrt,{mul,{9, add(4,5)}}}
[4,5,add,9,mul,sqrt] => {sqrt,{mul, {9, add(4,5)}}}
'''
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def recover(array):
    if len(array) == 3:
        root = TreeNode(array[-1])
        root.left = TreeNode(array[1])
        root.right = TreeNode(array[0])
        return root
    else:
        root = TreeNode(array[-1])
        root.left = recover(array[-1])
        return root

'''
5. Design Question: Get program running on data centers,
try catch and scalability , cache followups
'''

'''
quick sort & quick select
'''
def quickSort(nums):
    l = len(nums)
    if l <=1:
        return nums
    middle = nums[l/2]
    leftsub, rightsub = [],[]
    for i in range(l):
        if i!=l/2:
            if nums[i]<middle:
                leftsub += nums[i]
            else:
                rightsub += nums[i]
    return quickSort(leftsub) + [middle] + quickSort(rightsub)


def quickSelect(nums,k):
    l = len(nums)
    if l < k:
        return None
    pivot = nums[l/2]
    leftsub,rightsub,count = [],[],1
    for i in range(l):
        if i != pivot:
            if nums[i] == pivot: count+=1
            elif nums[i] < pivot: leftsub.append(nums[i])
            else: rightsub.append(nums[i])
    m = len(leftsub)
    if m <= k and m+count<k:
        return pivot
    elif m > k:
        return quickSelect(leftsub,k)
    else:
        return quickSelect(rightsub,k-m-count)

'''
find the kth largest/smallest element in an array (heap, quick select?)
'''

'''
第二题，把一个任意的数组，调整成小大小大小大。。。。的形式。
'''
## brutal force O(nlgn)
def zigzag(nums):
    nums.sort()
    l = len(nums)
    if l%2:
        small, big = nums[:len(nums)/2+1], nums[len(nums)/2+1:]
    else:
        small, big = nums[:len(nums)/2], nums[len(nums)/2:]
    res = []
    i,j=0,0
    while i<len(small) and j<len(big):
        res.append(small[i])
        res.append(big[j])
        i += 1
        j += 1
    if i < len(small):
        res.append(small[i])
    return res

## O(n) 三个三个看 012， 234， 456
##小大小
##   小大小
##      小大..
def zigzag_opt(nums):
    if len(nums) <=1:
        return nums
    if len(nums) == 2:
        if nums[0] > nums[1]:
            nums[0], nums[1] = nums[1], nums[0]
        return nums
    l = len(nums)
    for i in range(0,l,2):
        print i
        if i == l-1:
            return nums
        if i+2< l:
            num1, num2, num3 = nums[i],nums[i+1],nums[i+2]
            nums[i+1],nums[i] = max(num1, num2, num3), min(num1,num2,num3)
            nums[i+2] = num1+num2+num3-nums[i]-nums[i+1]
        else:
            if nums[i] > nums[i+1]:
                nums[i] ,nums[i+1] = nums[i+1], nums[i]
    return nums
#print zigzag_opt([9,8,7,6,5,4,3])
#print zigzag_opt([1,2,3,4,5,6,7])



'''
比如ABBA —> ABAB, BABA

假如不可能就回傳false AA—>false
'''
def rearrange(s):
    chars = list(s)
    res = []
    def dfs(path, remain_char):
        if not remain_char:
            res.append(path)
        else:
            for i in range(len(remain_char)):
                if (path == [] or remain_char[i] != path[-1]) and (i==0 or remain_char[i]!=remain_char[i-1]):
                    dfs(path+[remain_char[i]], remain_char[:i] + remain_char[i+1:])
    dfs([], chars)
    return res

def rearrange2(s):
    char_map = {}
    for char in s:
        char_map[char_map] = char_map.get(char,0) + 1
    res = []
    def dfs(path,char_map):
        if not char_map:
            res.append(path)
        else:
            for char in char_map:
                if char != s[-1]:
                    char_map[char] -= 1
                    if char_map[char] == 0:
                        del char_map[char]
                    dfs(path + [char], char_map)
    dfs([], char_map)
#print rearrange('AABB')

'''
word break ii
'''















'''
第二题，设计贪吃蛇的数据结构，queue + 二维boolean数组。然后写一个每次移动的函数。
'''

'''
Continental divider

给一个矩阵，其中0代表海洋，其他数字代表高度。秉着水往低处流的原则，求出能够流向任意海洋的点。 比如说

0 0 0 1 2 3 0
0 1 2 2 4 3 2
2 1 1 3 3 2 0
0 3 3 3 2 3 3
'''
def findPeak(board):
    m,n = len(board), len(board[0])
    visited = [[False for i in range(n)] for j in range(m)]
    def dfs(i,j,height):
        if i >= 0 and i < m and j >=0 and j<n and not visited[i][j] and board[i][j] >= height:
            visited[i][j] = True
            return max(dfs(i-1,j,board[i][j]), dfs(i+1,j, board[i][j]), dfs(i,j-1,board[i][j]), dfs(i,j+1,board[i][j]))
        return height
    peak = 0
    for i in range(m):
        for j in range(n):
            if board[i][j] == 0:
                cur_height = dfs(i,j,0)
                peak = max(peak, cur_height)
    return peak

board = [ [0, 0, 0, 1, 2, 3, 0], [0, 1, 2, 2, 4, 3, 2], [2, 1, 1, 3, 3, 2, 0],
          [0, 3, 3, 3, 2, 3, 3]]
#print findPeak(board)

'''
1. find all rotation symmetric numbers less than N digits,  16891 -> 16891,
2. give integer, 12345, 返回 32154
3. integer array add one
    rotation abc->bcd->cde, give a list of strings, group them if them are
rotations.
居然给我laptop，然后直接上面写，然后debug通过，给test case通过

5. design: chromecast, how to know which app can be supported? There is a
cloud that can give the information to the chrome cast, appID, deviceID,
cache design.

'''


'''
give you a series of paths and a start/end point, recover the path

'''
def recoverPath(adjacent, start,end):
    visited = {key:False for key in adjacent}
    res = []
    def dfs(path, cur):
        print cur, path
        visited[cur] = True
        if cur == end:
            res.append(path)
        else:
            for neighbor in adjacent[cur]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(path+[neighbor], neighbor)
            visited[cur] = False
            path = path[:-1]

    dfs([start], start)
    return res
#print recoverPath({'A':['B'],'B':['C'], 'C':['D','F'], 'D':['E'], 'E':['B'], 'F':[]}, 'A', 'F')

def recoverPath(start, end, path):
    start_node = {}
    for i in range(len(path)):
        start_node[path[i][0]] = start_node.get(path[i][0], []) + [i]
    edge_visited = [False for i in range(len(path))]
    p = [start]
    def dfs(cur):
        if cur == end and all(edge_visited):
            return True
        else:
            for e in start_node[cur]:
                if not edge_visited[e]:
                    edge_visited[e] = True
                    p.append(path[e][1])
                    if dfs(path[e][1]):
                        return True
                    edge_visited[e] = False
                    p.pop()
            return False
    if dfs(start):
        return p

start = 'a'
end = 'f'
paths = [('b', 'c'), ('d', 'e'), ('a', 'b'), ('c', 'd'), ('e', 'b'), ('b', 'c'), ('c', 'f')]
#print recoverPath('a','f', paths)
'''
给一个树root的pointer，树包含多个分支，树结构要自己创造。求一条最长[连续]
路径。
例如（括号对应上面node）  [修改：还有条件是 连续]
   树：                     2
                 |            |            |                |
                5            7          3                 6
         （|       | ）（   | ）   （|）         （|       |）
            6       3         2          4             5       8
                                 |
                                  3

返回3因为 （2-3-4） 这条线。优化要求时间O(n)
'''
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.children = []

class LongestPath:
    def __init__(self):
        self.longest = 0
    def dfs(self,root):
        if root == None:
            return 0
        cur = root.val
        local_longest=[0, 0]
        for child in root.children:
            if abs(cur - child.val) == 1:
                continous = self.dfs(child)
                if continous > local_longest[1]:
                    local_longest[0], local_longest[1] = max(local_longest[0],continous), min(local_longest[0],continous)
        self.longest = max(self.longest, sum(local_longest)+1)
        return local_longest[0]+1

'''
word abbrevation
word : wor1, wo1d, w1rd,1ord, wo2 w2d,w3,3d,4
'''
def abbr(word):
    res = []
    l = len(word)
    for offset in range(1,l+1):
        for index in range(l-offset+1):
            res.append(word[:index]+str(offset)+word[index+offset:])
    return res
#print abbr('word')

'''
1：（1）：写一个bool Palindrome(string s)，就是测s是否是Palindrome。
   （2）：已知bool Palindrome(string s)方程，写一个 int howmanyPalindrome
(string s), 输入s，返回s中包含多少个Palindrome的单词。 例如abbbac返回10，有a
,b,b,b,a,c,bb, bbb, bb, abbba.
'''
def checkPalindrome(s):
    start, end = 0, len(s)-1
    while start <= end:
        if s[start] == s[end]:
            start += 1
            end -= 1
        else:
            return False
    return True

def numOfPanlindrome(s):
    l = len(s)
    count = 0
    for i in range(l):
        for j in range(i+1,l+1):
            if checkPalindrome(s[i:j]):
                count += 1
    return count

#print numOfPanlindrome('abbbac')

'''
fibonaccia sum of a number
20 = 13+5+2
'''

def sumFibo(num):
    fic_array = [1,1]
    def generate(ceiling):
        cur = fic_array[-1]+fic_array[-2]
        if cur < ceiling:
            fic_array.append(cur)
            generate(ceiling)
    generate(20)
    print fic_array
    dp = [i for i in range(num+1)]
    for i in range(2,num+1):
        for j in range(i):
            gap = i - j
            if gap in fic_array:
                dp[i] = min(dp[i],dp[j] + 1)
                break
    return dp[-1]
#print sumFibo(20)
'''
continental divider
'''
def divider(board):
    m, n = len(board), len(board[0])
    alc_visited  = [ [ False for i in range(n)] for j in range(m)]
    pacific_visited = [ [False for i in range(n)] for j in range(m)]
    def dfs(i,j,height, map):
        if i >= 0 and i <  m and j >=0 and j < n and not map[i][j] and board[i][j] >= height:
            map[i][j] = True
            new_height = board[i][j]
            dfs(i-1,j, new_height)
            dfs(i+1,j, new_height)
            dfs(i, j-1, new_height)
            dfs(i, j+1, new_height)

    for i in range(n):
        dfs(0,i, 0,alc_visited)
    for i in range(m):
        dfs(i,0,0,alc_visited)

    for i in range(n):
        dfs(m-1,i,0,pacific_visited)
    for i in range(m):
        dfs(i, n-1,0,pacific_visited)

    divide = []
    for i in range(m):
        for j in range(n):
            if alc_visited[i][j] and pacific_visited[i][j]:
                divide.append((i,j))
    return divide




'''
4. given grid of colors, coordinate of a point and its color, find the
perimeter of the region that has the same color of that point.
'''
def colorPerimeter(board,i,j):
    m, n = len(board), len(board[0])
    color = board[i][j]
    region = []
    visited = [ [False for i in range(n)] for j in range(m)]
    def findRegion(i,j):
        if not visited[i][j] and board[i][j] == color:
            visited[i][j] = True
            region.append((i,j))
    findRegion(i,j)

'''
 print all morse code given the length constraints, short “*” takes one
, long “——“takes two.  就是排列组合的典型题
'''
def mose(l):
    res = []
    def dfs(remain_l,path):
        if remain_l == 0:
            res.append(path)
        elif remain_l > 0:
            for i in range(1,3):
                if i == 1:
                    new_path = path + '*'
                else:
                    new_path = path + '--'
                dfs(remain_l-i, new_path)
    dfs(l,'')
    return res

'''
give a target string and list of strings, find the longest string that
has target as prefix, follow up, stream of target string, 用trie，每个节点保
留最长string信息。
'''
## one target string
def longestWord(words, target):
    longest = ''
    l = len(target)
    for word in words:
        if len(word) >=l and len(word) > longest and word[:l] == target:
            longest = word
    return longest

## stream of target strings
class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.max_length_map = {}

    def insert(self,word):
        cur = self.root
        l = len(word)
        for char in word:
            if char in cur.children:
                cur = cur.children[char]
            else:
                new = TrieNode()
                cur.children[char] = new
                cur = new
            self.max_length_map[cur] = max(self.max_length_map[cur], l)
            l -= 1
        cur.isWord = True


    def search(self,target):
        cur = self.root
        for char in target:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return self.max_length_map[cur]

import heapq
'''
dijkstra's shortest path
'''
## min heap
class Heap:
    def __init__(self):
        self.hp = []
    def push(self, val):
        self.hp.append(val)
        self.swim(len(self.hp)-1)

    def sink(self,index):
        while index < len(self.hp) and (self.hp[index] < self.hp[index*2] or self.hp[index] < self.hp[index*2+1]):
            if self.hp[index*2] < self.hp[index*2+1]:
                next_index = index*2
            else:
                next_index = index*2 + 1
            self.hp[index] , self.hp[next_index] = self.hp[next_index], self.hp[index]
            index = next_index

    def swim(self,index):
        while index and self.hp[index]<self.hp[index/2]:
            self.hp[index], self.hp[index/2] = self.hp[index/2] , self.hp[index]
            index = index/2


    def popMin(self):
        self.hp[0], self.hp[-1] = self.hp[-1], self.hp[0]
        m = self.hp.pop()
        self.sink(0)
        return m

    def peakMin(self):
        return self.hp[0]

def shortestPaht(source, target, ajl, edge_cost):
    frontier = {source}
    visited = {}
    distances = {source:0}
    heap = Heap()
    for node in frontier:
        for end in ajl[node]:
            if (node,end) in visited:
                continue
            else:
                pass

'''
efficient sorting to sort a nearly sorted array --- an array has each element that is at most kth away from its
correct position.
insertion sort
'''
def insertion(nums):
    for i in range(1,len(nums)):
        cur_val = nums[i]
        p = i
        while p > 0 and nums[p-1] > cur_val:
            nums[p] = nums[p-1]
            p = p-1
        nums[p] = cur_val
'''
continental divider
'''
def divider(board):
    m,n = len(board), len(board[0])
    atlantic = [ [False for i in range(n)] for j in range(m)]
    pacific =  [ [False for i in range(n)] for j in range(m)]
    for i in range(n):
        atlantic[0][i] = True
        pacific[m-1][i] = True
    for i in range(m):
        atlantic[i][0] = True
        pacific[i][n-1] = True
    def validCoordinate(i,j):
        if i >= 0 and i < m and j >= 0 and j < n:
            return True
        return False

    def dfs(i,j,sea):
        if i>=0 and i<m and j>=0 and j<n and sea[i][j] != True:
            sea[i][j] = True
            cur_height = board[i][j]
            if sea == 'atlantic':
                if validCoordinate(i+1,j) and board[i+1][j] <= cur_height:
                    dfs(i+1,j,sea)
                if validCoordinate(i,j+1) and board[i][j+1] <= cur_height:
                    dfs(i,j+1,sea)
            else:
                if validCoordinate(i-1,j) and board[i-1][j] <= cur_height:
                    dfs(i-1,j, sea)
                if validCoordinate(i,j-1) and board[i][j-1] <= cur_height:
                    dfs(i,j-1 ,sea)

    for i in range(m):
        for j in range(n):
            if atlantic[i][j]:
                dfs(i+1,j,atlantic)
                dfs(i,j+1, atlantic)
            if pacific[i][j]:
                dfs(i-1,j,pacific)
                dfs(i,j-1,pacific)


def connectedComponent(board):
    m, n = len(board), len(board[0])
    atlanta, pacific = {}, {}
    for i in range(m):
        atlanta[(i,0)] = (0,0)
        pacific[(i,n-1)] = (m-1, n-1)
    for i in range(n):
        atlanta[(0,i)] = (0,0)
        pacific[(m-1,i)] = (m-1,n-1)
    for i in range(1,m-1):
        for j in range(1,n-1):
            if board[i][j] >= board[i-1][j]


    def unoin(a,b,sea):
        root_a, root_b = find(a, sea) ,find(b, sea)
        if root_a != root_b:
            sea[root_a] = root_b

    def find(a,sea):
        if a not in sea:
            return None
        if sea[a] != a:
            sea[a] = find(sea[a], sea)
        return sea[a]



def longestIncreasingPath(board):
    m,n = len(board), len(board[0])
    longest = {}
    def validCoordinate(i,j):
        if i >= 0 and i < m and j >= 0 and j < n:
            return True
        return False
    def dfs(i,j):
        if not validCoordinate(i,j):
            return 0
        if (i,j) in longest:
            return longest[(i,j)]
        l_up, l_down, l_left, l_right = 0,0,0,0
        if validCoordinate(i-1, j) and board[i][j] + 1 == board[i-1][j]:
            l_up = dfs(i-1,j)
        if validCoordinate(i+1, j) and board[i][j] + 1 == board[i+1][j]:
            l_down = dfs(i+1,j)
        if validCoordinate(i, j-1) and board[i][j] + 1 == board[i][j-1]:
            l_left = dfs(i,j-1)
        if validCoordinate(i, j+1) and board[i][j] + 1 == board[i][j+1]:
            l_right = dfs(i,j+1)
        l = max(l_down, l_up, l_left, l_right) + 1
        longest[(i,j)] = l
        return l
    cur_l = 0
    for i in range(m):
        for j in range(n):
            cur_l = max(cur_l, dfs(i,j))
    return cur_l