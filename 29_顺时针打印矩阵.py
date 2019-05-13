from numpy import *

num_array=array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]])
# num_array=array([[1,2,3],[4,5,6],[7,8,9]])
# print(array.size)

def print_matrix(num_array,row,columns,start):
    end_x=columns-start
    end_y=row-start
    for i in range(start,end_x):
        print(num_array[start][i])
    if start<end_y:
        for i in range(start+1,end_y):
            print(num_array[i][end_x-1])
    if start<end_x and start<end_y:
        for i in range(end_x-2,start-1,-1):
            print(num_array[end_y-1][i])
    if start<end_x and start<end_y-1:
        for i in range(end_y-2,start,-1):
            print(num_array[i][start])
def matrix_clockwise(num_array):
    row=num_array.shape[0]
    columns=num_array.shape[1]
    if num_array.size <0:
        return
    start=0
    while columns>start*2 and row>start**2:
        print_matrix(num_array,row,columns,start)
        start+=1
if __name__ == '__main__':
    matrix_clockwise(num_array)
