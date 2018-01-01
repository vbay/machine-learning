import tensorflow as tf
# tensor 'x' is [[-2.25 + 4.75j], [-3.25 + 5.75j]]


rank_three_tensor = tf.ones([3, 4, 5])
matrix = tf.reshape(rank_three_tensor, [6, 10])