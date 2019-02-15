import matplotlib.pyplot as plt
x=[1,2,3,5,6,7,8,9,10]
y=[5,7,4,6,7,8,9,2,5,6]
x2=[1,2,3,4,5,6,7,8,9,10]
y2=[7,5,6,4,8,12,13,10,2,5]
plt.plot(x,y)
plt.plot(x2,y2,label='england')
plt.xlabel('over number')
plt.ylabel('runs')
plt.title('my graph')
plt.legend()
plt.show()
