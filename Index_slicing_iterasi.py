import numpy as np 

a = np.arange(12)**2
print(a)

#mengambil nilai
print('nilai pertama dari a adalah', a[1])
print('nilai akhir dari a adalah', a[-1])

#Slicing (mengambil rentang nilai)

print('angka ketiga sampai lima', a[3:5])
print('angka ketiga sampai akhir', a[3:])
print('angka pertama sampai lima', a[:5])

#iterasi

for i in a:
	print('value', i**2)