#要求一
def calculate(min, max):
    total=0
    for n in range(min,max+1):
        total+=n
    print(total)

calculate(1, 3) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8) # 你的程式要能夠計算 4+5+6+7+8，最後印出 30


#要求二
def avg(data):
    num = data['count']
    if num == 0:
        print(0)
    else:
        total=0
        for person in data['employees']:
            total+=person['salary']
        avarage = total/num
        print(avarage)

avg({
"count":3,
"employees":[
{
"name":"John",
"salary":30000
},
{
"name":"Bob",
"salary":60000
},
{
"name":"Jenny",
"salary":50000
}
]
}) # 呼叫 avg 函式


#要求三
def find_max(para_list):
    max = []
    for n in para_list:
        if max == []:
            max.append(n)
        else:
            if n > max[0]:
                max[0] = n
    return max[0]

def find_min(para_list):
    min = []
    for n in para_list:
        if min == []:
            min.append(n)
        else:
            if n < min[0]:
                min[0] = n
    return min[0]

def maxProduct(nums):
    big1=find_max(nums)
    nums.remove(big1)
    big2=find_max(nums)
    big_mul = big1*big2
    nums.append(big1) #回復原狀

    small1=find_min(nums)
    nums.remove(small1)
    small2=find_min(nums)
    small_mul = small1*small2
    nums.append(small1) #回復原狀

    if big_mul >= small_mul:
        print(big_mul)
    else:
        print(small_mul)

maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([-1, -2, 0]) # 得到 2


#要求四
def twoSum(nums, target):
    for N, n in enumerate(nums):
        p = target - n
        if p in nums[N + 1:]:
            index = N + 1 + nums[N + 1:].index(p)
            return([N, index])
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9


#要求五
def maxZeros(nums):
    if len(nums) == sum(nums):
        print(0)
    elif sum(nums) == 0:
        print(len(nums))
    else:
        head, tail = 0, len(nums) - 1 
        one_i = []
        for N, n in enumerate(nums):
            if n == 1:
                one_i.append(N)
        gap = []
        for I, i in enumerate(one_i):
            if I == 0:
                gap.append(i - head)
            if I == len(one_i) - 1:
                former = one_i[I - 1]
                if i - former - 1 > gap[0]:
                    gap[0] = i - former - 1

                if tail - i > gap[0]:
                    gap[0] = tail - i
            else:
                former = one_i[I - 1]
                if i - former - 1 > gap[0]:
                    gap[0] = i - former - 1
        print(gap[0])
maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3