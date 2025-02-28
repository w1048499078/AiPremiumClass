import numpy as np
a = [3,4,5]
//创建数组
b = np.array(a)
//创建数据带数据类型
a = np.array([4,5,6], float)
print(a)
//创建多维数组 三行三列
a = np.array([4,5,6],[7,8,9],[10,11,12])
print(a)
//通过zeros创建数组  三行三列
a = np.zeros((3,3),dtype = float)
print(a)
//创建一个全为1的数组 三行两列
a = np.ones((3,2))
print(a)
//创建等差数列 从2开始，8结束，1为差的等差数列，小于8
a = np.arange(2,8,1)
print(a)
//创建单位矩阵
a = np.eys(3)
print(a)
//创建[0,1]随机数
a = np.random.random(7)
print(a)
//创建指定长度，符合正态分布的随机数，指定其均值为0，标准差为0.1
mu,sigma = 1,0.3
a = np.random.normal(mu,sigma,10)
print(a)
###Nunpy数组访问
a = np.array([3,4],[7,8],[9,6],[8,7])
print(a[0])
a[0]
a[2:]
a[:,:1]
a[2,2]

###Nunpy数组遍历
a = np.array([2,3,4,5,6])
for i in a
    print(i)
//多维遍历 
a = np.array([2,3,4],[6,7,8],[5,6,7])
for i,j in a
    print(i*j)

###NumPy 数组的常⽤属性
a = np.array([2,3,4],[6,7,8],[5,6,7])
print("ndim:", a.ndim)
print("shape:", a.shape)
print("size", a.size)
print("dtype", a.dtype)






