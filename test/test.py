import tensorflow as tf

t = tf.constant(42.0)
sess = tf.Session()
with sess.as_default():   # or `with sess:` to close on exit
    assert sess is tf.get_default_session()
    assert t.eval() == sess.run(t)