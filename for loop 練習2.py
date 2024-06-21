"""
编写一个函数 find_duplicate(nums)，
接受一个整数列表 nums 作为输入，
并返回列表中重复出现的数字。
列表中的数字范围在 1 到 len(nums) 之间，
且列表中可能包含多个重复数字，但每个数字只会重复一次。
"""
def find_duplicate(nums):
    seen= set()
    duplicate=[]
    for num in nums:
        if num in seen:
            duplicate.append(num)
        else:
            seen.add(num)
    return duplicate

nums=[0,0,1,3,6,8,8]
print(find_duplicate(nums))

