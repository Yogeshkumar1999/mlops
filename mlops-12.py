import numpy
import tensorflow as tf
x = tf.constant(3.0)
y = tf.constant(6.0)
w = tf.Variable(20.0)

def losscomputation():
    with tf.GradientTape() as tape:
        loss = tf.math.abs(w*x - y)
    dx = tape.gradient(loss, w)
    print w.numpy(), loss.numpy()
    w.assign(abs(w - dx))
i = 0
while i<= 10:
    losscomputation()
    i+=1
