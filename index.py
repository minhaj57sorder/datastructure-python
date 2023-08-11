# words = ['cat', 'window', 'defenestrate']
# for w in words:
#     print(w, len(w))
    
# class Point:
#     x: int
#     y: int

# def where_is(point):
#     match point:
#         case Point(x=0, y=0):
#             print("Origin")
#         case Point(x=0, y=y):
#             print(f"Y={y}")
#         case Point(x=x, y=0):
#             print(f"X={x}")
#         case Point():
#             print("Somewhere else")
#         case _:
#             print("Not a point")
            
# var =4

# from enum import Enum
# class Color(Enum):
#     RED = 'red'
#     GREEN = 'green'
#     BLUE = 'blue'

# color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

# match color:
#     case Color.RED:
#         print("I see red!")
#     case Color.GREEN:
#         print("Grass is green")
#     case Color.BLUE:
#         print("I'm feeling the blues :(")

# newlist = ["apple", "banana", "cherry"]

# for i in range(len(newlist)):
#     print(f"index of apple is: {i}")


# class User:
#     def __init__(self, fname:str, lname:str,age:int)->None:
#         self.fname = fname
#         self.lname = lname
#         self.age = age
    
#     def getFullName(self)->str:
#         return self.fname + self.lname
    

# usera = User("minhaj","sorder",26)

# print(f"user age {usera.getFullName}")


# s = "minhaj"

# print("-"*80)
# print(f"{s.center(20).strip()}")


# class Employee:
#     def __init__(self) -> None:
#         pass

# if __name__ == "__main__":
#     e1 = Employee()

# nums = [1,0,-1,0,-2,2]
# print(nums)

# class Solution:
#     def permute(self, nums):
#         result=[]
#         if len(nums)==1:
#             return [nums[:]]
#         for i in range(len(nums)):
#             n = nums.pop(0)
#             perms = self.permute(nums)
#             print(perms)
#             for perm in perms:
#                 perm.append(n)
#             result.extend(perms)
#             nums.append(n)
#         return result
    
# solution = Solution()

# print(solution.permute([1,2,3]))
# from collections import defaultdict
# class Solution:
#     def groupAnagrams(self, strs):
#         res = defaultdict(list)

#         for s in strs:
#             count = [0]* 26
#             for c in s:
#                 count[ord(c)-ord('a')] += 1
#             res[tuple(count)].append(s)
#             print()

# solution = Solution()
# print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

# nums = [1, 2, 3]
# print(nums[::])
# print(nums[1:][::-1]+nums[2:])
# print([0]*26)
# print(nums[:1])
# print(nums[:])
# print(nums[0:2])

# class Solution:
#     def topKFrequent(self, nums,k):
#         count = {}
#         freq=[ [] for i in range(len(nums)+1) ]

#         for n in nums:
#             count[n] = 1+ count.get(n,0)
#         for n,c in count.items():
#             freq[c].append(n)
#         res = []
#         for i in range(len(freq)-1,0,-1):
#             for n in freq[i]:
#                 res.append(n)
#                 if(len(res)==k):
#                     return res

# solution = Solution()
# print(solution.topKFrequent([1,1,1,2,2,3],2))
import datetime

# print(dir(datetime))
print(datetime.datetime.now().strftime("%I%p"))