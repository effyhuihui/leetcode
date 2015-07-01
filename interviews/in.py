# -*- coding: utf-8 -*-

'''
1. print out a multiplication table ie. 1 x1 to 12 x12 
'''
def printMatrix(n):
	res = []
	for i in range(1,n+1):
		res.append([])
		for j in range(i,n+1):
			res[-1].append(i*j)
	print res
printMatrix(3)



























'''
2. Using OOP design a elevator
3. write code to print the matrix from outside to inside.
4. Given a list of words, find whether a new word is anagram of word in list.  
5. Input a string and output the number of words (need to run   on coderpad)
6. code challenge are on uber's github page 
7. implement boggle game
8. Design from scratch and talk about scaling, product, and   performance concerns.
9. 给定一个string，判断能否用这个string来组成一个palindrome。e.g. 'uber' -->
False, 'aab' --> True, 'carecra' --> True  （奇数字母最多只有一个）
Follow up: 给出所有能够组成的palindrome，因为时间原因可以不用担心
duplicates。
第二题就是permutation
http://www.mitbbs.com/article_t/Dreamer/34337437.html

onsite:
1. team的核心非manager人员(感觉要升成一个lead): 很简单的Fibonacci数列问题的
变体。A编码成1,B编码成2,Z编码成26。然后给一串数字问有多少种方法解码。比如32
只能解成CB, 26可以解成Z或者BF
2. team资深人员问，社交网络里，计算陌生人中共有朋友最多的一个人的办法。设计
存储，和计算流程。
3. team稍微junior一点的人，问打印powerset。
4. team lunch，大概5个人，中间hiring manager茬进来聊了一下天。5个白人，其中3
个美国本土白人2个欧洲白人，1个ABC。
5. 兄弟团队的lead: 给一个dict比如lock, locker, erning,然后给一个输入词,比如
lockerning, 返回能不能拆成dict里的词的不重合的组合。比如lockerning->yes, 
lockern->false.

pinterst:
1. given an array of words, find the longest and common substring between two words in the array(and what are the two words)  --- trie prefix tree
2. word break
3.jump game
'''


