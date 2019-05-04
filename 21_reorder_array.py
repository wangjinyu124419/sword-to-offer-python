"""
// 面试题21：调整数组顺序使奇数位于偶数前面
// 题目：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有
// 奇数位于数组的前半部分，所有偶数位于数组的后半部分。
"""

def recoder_array(input_array):
    p1=0
    p2=len(input_array)-1

    while p2>p1:
        if input_array[p1]%2!=0:
            p1+=1
        else:
            if input_array[p2]%2==0:
                p2-=1
            else:
                input_array[p1],input_array[p2]=input_array[p2],input_array[p1]
    print(input_array)
    return input_array
if __name__ == '__main__':
    input_array=[1,2,3,4,5,6,7,8,9,10]
    recoder_array(input_array)

