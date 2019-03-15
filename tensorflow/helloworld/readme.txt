+ Basic thing: 
- Grap and Session (ref: https://medium.com/coinmonks/tensorflow-graphs-and-sessions-c7fa116209db)
- All below thing when you declare in no graph, it will be in the default graph (Am I correct?)
# tf.constant
# tf.placeholder
# tf.Variable

    Variables (ref: https://www.tensorflow.org/api_docs/python/tf/Variable)
    . For parameters to learn
    . Values can be derived from training
    . Initial values are required (often random)
    . Initalize by running a session
    Placeholders (ref: https://www.tensorflow.org/api_docs/python/tf/placeholder)
    . Allocated storage for data (such as for image pixel data during a feed)
    . Initial values are not required (but can be set, see tf.placeholder_with_default)

more: https://stackoverflow.com/questions/36693740/whats-the-difference-between-tf-placeholder-and-tf-variable


+ Sesion.run() and Tensor.eval() (ref: https://stackoverflow.com/questions/33610685/in-tensorflow-what-is-the-difference-between-session-run-and-tensor-eval)

'''Example'''
a = tf.constant([1,2,3])

sess = tf.Session()

print(sess.run(a))
print(a.eval(session = sess)) # both print line is the same


+ Other problem: https://stackoverflow.com/questions/46894808/tensorflow-how-to-initialize-variables-on-another-graph
