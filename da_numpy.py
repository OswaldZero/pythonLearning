import numpy as np
#一维数据创建
sequence1=[1,2,3]
arr=np.array(sequence1)
print(type(arr))
# 二维数组创建
seq=[[1,3],[2,4]]
arr7=np.array(seq)
print(arr7.ndim,arr7.shape)
# 指定数据类型
sequence2=[1,2,3]
arr4=np.array(sequence2,np.int32)
# 特殊数组
arr1=np.ones((3,4))
arr2=np.zeros((3,4))
arr3=np.eye(3)
print(arr1,arr2,arr3)