import theano
import theano.tensor as T
from theano import pp

x = T.dscalar('x')
y = x**2
gy = T.grad(y,x)
print gy
f = theano.function([x], gy)
print f(4)
print f(98.2)
x2= T.dvector('x')
y2 = x2 ** 2
f2 = theano.function([x2],y2)
print f2([2,2])