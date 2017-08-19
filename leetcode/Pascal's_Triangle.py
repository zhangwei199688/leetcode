'''
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''
class Solution(object):
    def generate(self, numRows):
        row = [0, 1, 0]
        newrow = []
        resultrow = []
        times = 0
        for i in range(numRows):
            times += 1
            for i in range(times):
                a = row[i] + row[i + 1]
                newrow.append(a)
            resultrow.append(newrow)
            row = newrow
            row = [0] + row
            row = row + [0]
            newrow = []
        return resultrow

#A usage of map function
class Solution(object):
    def generate(self, numRows):
        res=[[1]]
        for i in range(1,numRows):
            res+=[map(lambda x,y:x+y,res[-1]+[0],[0]+res[-1])]
        return res[:numRows]

