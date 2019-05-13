"""
// 面试题14：剪绳子
// 题目：给你一根长度为n绳子，请把绳子剪成m段（m、n都是整数，n>1并且m≥1）。
// 每段的绳子的长度记为k[0]、k[1]、……、k[m]。k[0]*k[1]*…*k[m]可能的最大乘
// 积是多少？例如当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此
// 时得到最大的乘积18。
"""

def max_length(n):
    if n < 2:
        return 1
    if n==2:
        return 1
    if n==3:
        return 2

    return max([ max_length(i)*max_length(n-i) for i in range(1,n)])

if __name__ == '__main__':
    res=max_length(4)
    print(res)