from pylab import *
from numpy import *
def f(x,v,t):
    return -x
n = 300
h = 10*6.28/float(n)
t = zeros(n,float)
v = zeros(n,float)
x = zeros(n,float)
v[0] = 5.0
for i in range(1,n):
    t[i]=h*i
    x[i]=v[i-1]*h+x[i-1]
    v[i]=v[i-1]+h*f(x[i-1],v[i-1],t[i-1])
plot(t,x,'k-')
plot(t,v,'k--')
xlabel('t')
ylabel('y = sin x ve y = cos x')
show()