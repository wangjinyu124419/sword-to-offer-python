#循环遍历实现
def max_sub_sum(nums_list):
    #初始最大值
    max_sum=nums_list[0]
    #开始索引
    start_index=0
    #结束索引
    end_index=0
    #从一开始遍历
    for i in range(1,len(nums_list)):
        #如果当前所以的数字大于start到当前索引的和，则start_index应该更新为当前索引，同时更新结束索引。
        if nums_list[i]>sum(nums_list[start_index:i+1]):
            start_index=i
            end_index=i
            max_sum = nums_list[i]
            continue
        temp_sum=sum(nums_list[start_index:i+1])
        if temp_sum>max_sum:
            end_index=i
            max_sum=temp_sum
    return max_sum,start_index,end_index


#动态规划，递归实现
def max_i(nums_list,i):
    if i==0 or max_i(nums_list,i-1)<=0:
        return nums_list[i]
    else:
       return max_i(nums_list,i-1)+nums_list[i]


def max_sub_sum_rec(nums_list):
     return max([max_i(nums_list,i)  for i in range(len(nums_list))])



if __name__ == '__main__':
    nums_list=[1,-2,3,10,-4,7,2,-5]
    nums_list=[-1,2,3,-1,2,10,-5,15]
    # res=max_sub_sum(nums_list)
    res=max_sub_sum_rec(nums_list)
    print(res)


