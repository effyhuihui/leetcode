'''
Write a SQL query to find all numbers that appear 
at least three times consecutively.

+----+-----+
| Id | Num |
+----+-----+
| 1  |  1  |
| 2  |  1  |
| 3  |  1  |
| 4  |  2  |
| 5  |  1  |
| 6  |  2  |
| 7  |  2  |
+----+-----+
For example, given the above Logs table, 1 is the only number that appears consecutively 
for at least three times.
'''

'''
分析: 此题目是需要求出连续次数不少于3次的数字, 因为mysql 判断是否连续就是判断下这一行的Num 是否和上一行
的Num 相等, 不相等则不连续, 上一行的值我们可以用@last 表示. 然后用@rownum 记录连续次数就行了. 
要注意, 最终结果是要distinct 或者 group by的. 因为可能会有多个连续的1.
'''
SELECT DISTINCT Num FROM (
    SELECT Num, IF(Num = @last, @row := @row + 1, @row := 1) as times, @last := Num
    FROM Logs, (SELECT @last := 'x', @row := 0) r
) t
WHERE times >= 3



'''
http://bookshadow.com/weblog/2015/01/14/leetcode-consecutive-numbers/
'''

# Write your MySQL query statement below
SELECT DISTINCT Num FROM (
  SELECT Num, COUNT(Rank) AS Cnt FROM (
    SELECT    Num,
              @curRank := @curRank + IF(@prevNum = Num, 0, 1) AS rank, @prevNum := Num
    FROM      Logs s, (SELECT @curRank := 0) r, (SELECT @prevNum := NULL) p
    ORDER BY  ID ASC
  ) t GROUP BY Rank HAVING Cnt >= 3 
) n;


































