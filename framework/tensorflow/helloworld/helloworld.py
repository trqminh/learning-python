# An error code example
'''
import tensorflow as tf

graph = tf.Graph()

a = tf.constant("hi world")

sess = tf.Session(graph = tf.get_default_graph())


with graph.as_default():
    a = tf.constant('hello world')



print(a.eval(session = sess))

#print(graph.get_operations())
'''

import tensorflow as tf
import numpy as np


graph1 = tf.Graph()
graph2 = tf.Graph()

with graph1.as_default():
    str_1 = tf.constant('hello world 1')
    a1 = tf.constant([[1,2,3],[5,6,6]]) # any kind of type in tf.constant are accepted
    x1 = tf.Variable([1,2])
    p1 = tf.placeholder(tf.int32, name = 'p1')


with graph2.as_default():
    str_2 = tf.constant('hello world 2')
    a2 = tf.constant([[1,4,2],[5,6,6]])
    p2 = tf.placeholder(dtype = tf.int32, name = 'p2')
    mul = tf.multiply(p2,a2)
    
    x2 = tf.Variable(tf.zeros([1,3]), name = 'x2')
    px = tf.placeholder(shape = (3,4),dtype = tf.float32)
    matmult = tf.matmul(x2,px)


sess1 = tf.Session(graph = graph1)
sess2 = tf.Session(graph = graph2)
print('------------------------------------')

print('Graph 1 operations: ', graph1.get_operations())
print('Graph 2 operations: ', graph2.get_operations())

print('------------------------------------')

print(str_1.eval(session = sess1))
print(sess1.run(str_1))
print(str_2.eval(session = sess2))
print(sess2.run(a2[1]))
print(mul.eval(session = sess2, feed_dict = {p2 :[4]}))
sess2.run(x2.initializer)
#sess2.run(tf.global_variables_initializer())
print(matmult.eval(session = sess2, feed_dict = {px : np.zeros([3,4])}))
