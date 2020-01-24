ref: https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/udacity/2_fullyconnected.ipynb
## Some functions

* tf.truncated_normal()
```
weight_1 = tf.Variable(tf.truncated_normal([num_features, num_hiddens]))
Normal random distribution for initing weight
```
* tf.nn.softmax_cross_entropy_with_logits(labels=tf_train_labels, logits=logits)
```
ref: https://www.tensorflow.org/api_docs/python/tf/nn/softmax_cross_entropy_with_logits
```
* tf.reduce_mean(a)
```
tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=tf_train_labels, logits=logits))
(1/m) * (ai +.. + am)
```
* tf.train.GradientDescentOptimizer(alpha).minimize(loss)
```
optimizer = tf.train.GradientDescentOptimizer(0.5).minimize(loss)
Call optimizer in session for optimize loss with alpha = 0.5
```

## model

![](https://github.com/1612374/learning-python/blob/master/tensorflow/SGD_one_hidden_relu/Add%20relu%20to%20be%20nrnw_0.png)
![](https://github.com/1612374/learning-python/blob/master/tensorflow/SGD_one_hidden_relu/Add%20relu%20to%20be%20nrnw_1.png)
