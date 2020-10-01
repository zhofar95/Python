import numpy as np 
a = np.array(([1,2,3,4],[5,6,7,8]))
b = np.array(([2,3],[4,5],[6,7],[8,9]))

hasil1 = a.dot(b)
hasil2 = np.dot(a,b)

print(hasil2)

#melihat ukuran matrix

print("ukuran matrix hasil2 adalah", hasil2.shape)

#transpose

print(a.transpose())
print(np.transpose(a))
print(a.T)

#flatten matrix/mengubah matrik menjadi baris
print(a.ravel())
print(np.ravel(a))

#reshape
print(a.reshape(4,2))

#Resize
a.resize(8,1)
print(a)

#stacking


a1 = np.array(([1,2,3],[3,4,5]))
b1 = np.array(([5,6,7], [3,7,8]))

c1=np.hstack((a1,b1))
c2=np.vstack((a1,b1))

print(c2)
