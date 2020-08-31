# num_str = input()
# num = int(num_str)
# positive_num = abs(num)
# num_str = str(positive_num)
# rule_str = input().split()
# # rule = [int(i) for i in rule]
# res=''
# for i in range(len(num_str)):
#     idx = int(num_str[i])-1
#     res += rule_str[idx]
# res = int(res)
# if num<0:
#     res = -res
# print(res)
# import math.pi as pi
# import math
# pi = math.pi
# circle_num = int(input())
# circle_r = input().split()
# circle_r = [int(i) for i in circle_r]
# circle_r = circle_r[::-1]
# area = 0
# for i in range(len(circle_r)):
#     circle_area = pi * (circle_r[i] ** 2)
#     if i % 2 == 0:
#         area += circle_area
#     else:
#         area -= circle_area
# print('%.5f'%area)
#
#
# num = int(input())
# num_list = input().split()
# num_list = [int(i) for i in num_list]
# dp = [1 for i in range(num)]
# fangan = [0 for i in range(num+1)] # 长为idx的方案个数
# fangan[1] = 1
# for i in range(1, num):
#     dp[i] = 1+dp[i-1]
#     for j in range(i,0,-1):
#         idx = j + 1
#         if num_list[i] % idx==0:
#             dp[i]+=fangan[idx-1]
#             fangan[idx]+=1
#     fangan[1]+=1
# print(dp[-1])


# print((1e9+7))
# import copy
# a=[1,[1,2],3]
# b=copy.copy(a)
# print(a,b)
# b[1][1]=0
# b[0]=0
# print(a,b)
# class Singleton(object):
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, '_instance'):
#             return super(Singleton, cls).__new__(cls, *args, **kwargs)
# class Mycalss(Singleton):
#     pass


# import re
# res=re.findall(r'[\u4e00-\u9fa5]+','张三，sdeeda de深 度3frf344 r')
# print(res)


# a = {1,2,3}
# a.add(3)
# print(a)
# import datetime
# c=datetime.datetime.now()
# print(type(c))
# print(type(c.year))
# print(2^1)

# import sys
# sys.stdin.readline().strip()
# string = input()
# stack = []
# cur_num = 0
# for i in string:
#     if i.isdigit():
#         cur_num = cur_num*10 +int(i)
#     else:
#         if i in ['+', '-']:
#             stack.append(i)
#         if i in ['*','/']:
#             stack.append()

class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return nums
        stack = [(0, len(nums) - 1)]
        while stack:
            print(nums)
            left, right = stack.pop()
            print(left,right)
            if left < right:
                left_ = left
                right_ = right
                key = nums[left_]
                while left_ < right_:
                    while left_ < right_ and nums[right_] >= key:
                        right_ -= 1
                    nums[left_] = nums[right_]
                    while left_ < right_ and nums[left_] <= key:
                        left_ += 1
                    nums[right_] = nums[left_]
                nums[left_] = key
                stack.append((left, left_ - 1))
                stack.append((left_ + 1, right))
                # print(nums)
        return nums




def kuohao(startidx,string):
    res = 0
    cur_num = 0
    cur_num_sym = True
    pre_num = 0
    pre_num_sym = True
    pre_num_calculate = None
    i=startidx
    while i < len(string):
        # print(i)
        if string[i].isdigit():
            cur_num = cur_num * 10 + int(string[i])
            i+=1
        else:
            if cur_num_sym is False:
                cur_num = -cur_num
                cur_num_sym=True
            if pre_num_calculate is None:
                pass
            else:
                if not pre_num_sym:
                    pre_num = -pre_num
                if pre_num_calculate == '*':
                    cur_num = cur_num * pre_num
                else:
                    cur_num = pre_num / cur_num
                pre_num = 0
                pre_num_sym = True
                pre_num_calculate = None

        if string[i] in [ '+','-','*','/']:
            if string[i] in ['+','-']:
                res+=cur_num
                cur_num=0
                cur_num_sym=True if string[i]=='+' else False
                i+=1

            if string[i] in ['*','/']:
                pre_num = cur_num
                pre_num_sym = cur_num_sym
                cur_num=0
                cur_num_sym=True
                pre_num_calculate=string[i]
                i+=1

        if string[i] == ')':
            cur_num=-cur_num if cur_num_sym is False else cur_num
            return res+cur_num, i+1
        if string[i] == '(':
            cur_num, i = kuohao(i+1,string)
    # 最后再加上
    # if not cur_num_sym:
    #     cur_num = -cur_num
    # if pre_num_calculate is None:
    #     pass
    # else:
    #     if not pre_num_sym:
    #         pre_num = -pre_num
    #     if pre_num_calculate == '*':
    #         cur_num = cur_num * pre_num
    #     else:
    #         cur_num = pre_num / cur_num
    #     pre_num = 0
    #     pre_num_sym = True
    #     pre_num_calculate = None
# a=input()
# a=a+')'
# res,_=kuohao(0,a+')')
# print(res)
# class Solution1(object):
#     def verifyPostorder(self, postorder):
#         """
#         :type postorder: List[int]
#         :rtype: bool
#         """
#         return self.verifyHelper(0, len(postorder)-1, postorder)
#     def verifyHelper(self, startidx, endidx, postorder):
#         print(startidx,endidx)
#         if startidx>=endidx:
#             return True
#         rootval = postorder[endidx]
#         boundary = startidx
#         for boundary in range(startidx, endidx):
#             if postorder[boundary] > rootval:
#                 break
#         if postorder[boundary]<=rootval:
#             return True
#         for point in range(boundary, endidx):
#             if postorder[point]<rootval:
#                 return False
#         return self.verifyHelper(startidx, boundary-1,postorder) and self.verifyHelper(boundary, endidx-1,postorder)
# import math
# n=int(input())
# print(n)
# res = [2,3]
# def if_su(num,res):
#     sqrt_num = math.sqrt(num)
#     for i in res:
#         if i <= sqrt_num:
#             if num%i == 0:
#                 return False
#         else:
#             return True
# while res[-1]<=n:
#     now = res[-1] + 2
#     while not if_su(now,res):
#         print(now)
#         now += 2
#     res.append(now)
# a = res.pop()
# b = res.pop()
# if abs(a-n)<abs(b-n):
#     print(a)
# else:
#     print(b)

def dfs(strs, visited, subset, res):
    if len(subset)==len(strs):
        num = int(''.join(subset))
        if num % m == 0:
            res[0] += 1
        return
    for i in range(len(strs)):
        if visited[i]==1:
            continue
        if i!=0 and strs[i] == strs[i-1] and visited[i-1]==0:
            continue
        subset.append(strs[i])
        visited[i]=1
        dfs(strs, visited, subset,res)
        subset.pop()
        visited[i]=0
# nums = input().split()
# m = int(nums[1])
# s = nums[0]
# strs = [i for i in s]
# strs.sort()
# visited = [0 for i in range(len(strs))]
# res=[0]
# dfs(strs, visited, [],res)
# print(res[0])
import copy
# a=1
a={1:3}
b={1:4}
a.update(b)
print(a)
res=0
for i in range(9):
    res+=0.9
    print(res)
print(res)
# b=copy.deepcopy(a)
# print(id(a),id(b))
# print(2**15)
