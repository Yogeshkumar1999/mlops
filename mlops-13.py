import tensorflow as tf
import numpy as np
import pandas as pd

x1 = tf.constant(10)
#x2 = tf.constant(100)
y = tf.constant(40)
w1 = tf.Variable(2)
#w2 = tf.Variable(10)
b = tf.Variable(5)
#with is tro auto matically close the object.

t = tf.GradientTape()

