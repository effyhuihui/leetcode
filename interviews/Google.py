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
print rle('aaaaabbbccc')


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
输入： dat ab"fghi"jk   wp"q msl"v   输出：  [dat ab] , [fghijk],   [wp],  [q mslv]
输入：      axg"h   msdk"xlc  d"ber"hn   输出： [axg],  [h   msdkxlc],  [d],  [berhn]
也就是说双引号是成对出现的，字符串最前面和最后面的空格是不计的，但是中间的空格是要计的，详见例子就能明白。
'''

def splitStr(s):
    s = s.strip()
    res = []
    space_split = False
    while s:
        if not space_split:
            first_quote = s.index('"')
            res.append(s[:first_quote])
            s = s[first_quote+1:]
            s = s.strip()
            space_split = True
        else:
            if ' ' in s:
                second_quote = s.index('"')
            else:
                second_quote = len(s)
            string_end = s.index(' ')
            res.append(s[:second_quote]+s[second_quote+1:string_end])
            s = s[string_end:]
            s.strip()
            space_split = False

#print splitStr('dat ab"fghi"jk   wp"q msl"v')
#print splitStr('     axg"h   msdk"xlc  d"ber"hn')

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
print zigzag_opt([9,8,7,6,5,4,3])
print zigzag_opt([1,2,3,4,5,6,7])



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
print rearrange('AABB')

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
print findPeak(board)


'''

G：
1. find all rotation symmetric numbers less than N digits,  16891 -> 16891,
2. give integer, 12345, 返回 32154
    give a target string and list of strings, find the longest string that
has target as prefix, follow up, stream of target string, 用trie，每个节点保
留最长string信息。
3. integer array add one
    rotation abc->bcd->cde, give a list of strings, group them if them are
rotations.
居然给我laptop，然后直接上面写，然后debug通过，给test case通过

4. given grid of colors, coordinate of a point and its color, find the
perimeter of the region that has the same color of that point.
    print all morse code given the length constraints, short “*” takes one
, long “——“takes two. (find a bug in the code) 就是排列组合的典型题
5. design: chromecast, how to know which app can be supported? There is a
cloud that can give the information to the chrome cast, appID, deviceID,
cache design.

'''
def colorPerimeter(board,i,j):
    m,n = len(board), len(board[0])




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
        print p, cur
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