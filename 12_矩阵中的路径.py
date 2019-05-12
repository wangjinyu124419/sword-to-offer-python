'''
题目：请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个
格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则该路
径不能再进入该格子。 例如 a b c e s f c s a d e e 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含
"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
'''

from numpy import *
import  numpy as np

#主函数
def has_path(matrix,rows,cols,s):
    # visited=array()
    path_length=0
    #visited是大小与str_matrix相同的矩阵，用来记录矩阵中已经访问过得节点
    visited=np.zeros((3, 4))
    for row in range(rows):
        for col in range(cols):
            if has_core(matrix,rows,cols,row,col,path_length,s,visited):
                return True
    else:
        return False
#判断矩阵的坐标是否等于字符串对应的索引值
def has_core(matrix,rows,cols,row,col,path_length,s,visited):
    if path_length>= len(s):
        return  True

    #是存路径
    is_has_path=False

    #如果存在对应坐标
    if row>=0 and row<rows and col>=0 and col<cols and matrix[row][col]==s[path_length] and not visited[row][col]:
        # 路径前进一步
        path_length+=1
        #坐标标记为已经访问过
        visited[row][col]=True
        is_has_path= has_core(matrix,rows,cols,row,col-1,path_length,s,visited) or\
                     has_core(matrix,rows,cols,row,col+1,path_length,s,visited) or \
                     has_core(matrix,rows,cols,row+1,col,path_length,s,visited) or \
                     has_core(matrix,rows,cols,row-1,col,path_length,s,visited)

        #如果不存在路径，返回上一坐标,并将visited中对应坐标指为未访问状态
        if not is_has_path:
            path_length-=1
            visited[row][col] = False

    return is_has_path



if __name__ == '__main__':
    # 生成矩阵
    str_matrix = array([['a', 'b', 't', 'g'], ['c', 'f', 'c', 's'], ['j', 'd', 'e', 'h']])
    # str_matrix = array([['a', 'b', 't', 'g'], ['b', 'f', 'c', 's'], ['j', 'd', 'e', 'h']])

    # 矩阵的行数
    rows = str_matrix.shape[0]
    # 矩阵列数
    cols = str_matrix.shape[1]
    # print(has_path(str_matrix, rows, cols, 'abjdfb'))
    print(has_path(str_matrix, rows, cols, 'acjdfb'))
