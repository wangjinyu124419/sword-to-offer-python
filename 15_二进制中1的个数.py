
def num_of_1(n):
    ret = 0
    while n:
        ret += 1
        n = n & n-1
    return ret
if __name__ == '__main__':
    print(num_of_1(12))