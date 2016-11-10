from tqdm import tqdm
import numpy as np
import matplotlib.pyplot as plt
def f(x,r):
	for i in range(200):
		x=r*x*(1.0-x)
	return x
plotv = np.vectorize(f,excluded=['x'])
dx=2000
ds=200
rangestart=3.4
rangeend=4
for s in tqdm(np.linspace(0,1,ds)):
	points=plotv(r=np.linspace(rangestart,rangeend,dx),x=s)
	plt.scatter(np.linspace(rangestart,rangeend,dx),points, s=0.01,marker='x')
plt.axis([rangestart, rangeend, 0, 1])
plt.savefig("graph.jpg", dpi=1000)


