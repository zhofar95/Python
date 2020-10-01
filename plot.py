import matplotlib.pyplot as plt 
import numpy as np 

x =np.linspace(0,30,30)
y = x**2
y1 = x**3

plt.xlabel('Satuan')
plt.ylabel('hasil')
plt.plot(x, label='biasa', marker='*')
plt.ploy(y, label='kuadrat', marker='-')
plt.ploy(y1, label='pangkat tiga', marker='-')

plt.plot(y1)
plt.show()