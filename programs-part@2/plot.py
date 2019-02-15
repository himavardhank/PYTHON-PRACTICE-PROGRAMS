import matplotlib.pyplot as plt
plt.bar([1,3,5,7,9],[5,2,7,8,2],label="example1",color='r')
plt.bar([1,8,5,8,9],[5,2,8,8,1],label="example2")
plt.legend()
plt.xlabel('barnumber')
plt.ylabel('barheight')
plt.title('mygraph')
plt.show()
