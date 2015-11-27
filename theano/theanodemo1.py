import theano
import theano.tensor as T

x = T.dmatrix('x')
z = 1/(1+T.exp(-x))
logistic = theano.function([x],z)
out = logistic([[1,2],[2,3]])
print out

s2 = (1 + T.tanh(x / 2)) / 2
logistic2 = theano.function([x],s2)
out2 = logistic2([[1,2],[2,3]])
print out
