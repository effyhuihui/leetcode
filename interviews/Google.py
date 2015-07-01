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
    indices = range(len(words))
    indices.sort(key=lambda i:len(words[i]))
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
2. RLE run-length compression
'''

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

3. Word abbreviation,
e.g. Between=>b5n,friend=>f4d
Follow-up: implement Bool checkduplicate(string [] dict, string word)
E.g. {feed }, feed => false;{door }, deer =>true;{dare}, deer => false
如果dict里有word 和input word的abbreviation 一样，则return true
'''

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
def splitString(s):
    ## strip the leading and trailing spaces and split by double quote
    split_by_quote = s.strip().split('"')
    print split_by_quote


def splitStr(s):
    s = s.strip()
    start = 0
    res = []
    count_quote = 0
    for i in range(len(s)):
        if s[i] =='"':
            count_quote += 1
            if count_quote == 1:
                res.append(s[start:i])
                start = i+1
            else:
                count_quote = 0

print splitString('dat ab"fghi"jk   wp"q msl"v')
print splitString('     axg"h   msdk"xlc  d"ber"hn')

'''
find the kth largest/smallest element in an array (heap, quick select?)
'''

'''
第二题，把一个任意的数组，调整成小大小大小大。。。。的形式。
'''
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

那么就要给出 第二行的4 （这有这点出发，能够找到连通道四个0的区域的一条非递增
路线），当然也有可能找不到这样的点，或者找到多个点。

一句话思路

从原题矩阵中建立一个有向图，其中结点是矩阵中等高联通区域，而有向边连接的这些结点在矩阵中所代表的联通区域相邻，
其方向是从底高度节点指向高高度结点；我们从低高度结点到高高度结点遍历整个有向图，并在遍历中不断地对汇入当前节点的海洋节点求并集；
最后包括所有海洋节点的节点便是所求的节点。

详细步骤

建立所有有向图节点：通过遍历矩阵，我们可以找到所有的相邻的高度一样的区域。我们把每一个这样的区域组成一个有向图的节点，
用这个区域的高度来标识这个节点的高度。要注意的是，我们要在原矩阵的每个元素上记录其所属的有向图节点，以便于下一步中建立有向边。
这些有向图的节点里面还应包括一个bitset，以便第三步中进行对其能到达海洋求并集。给每一个高度为0 的有向图节点的bitset里面set一个unique 的bit。
建立节点有向边: 再次遍历矩阵，这次注意所遍历元素的上下左右所有相邻元素。如果这些相邻元素和当前元素属于不同有向图的节点，则通过有向边连接他们，
边的方向是由底高度节点指向高高度节点。在设置有向边的时候，要注意去除重复的边。
遍历有向图：将有向图从底到顶遍历。遍历的时候，将前导节点的bitset 并入当前节点，如果当前节点的bitset中包括所有的海洋bits，
那么当前节点就标记为成功节点。
得出答案：再一次遍历原矩阵里面的所有元素，如果某个元素所属的有向图节点是成功节点，那么这个元素也就是属于所要找的点。

'''

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

