import collections
import tensorflow as tf

slim = tf.contrib.slim


class Block(collections.namedtuple('Block', ['scope', 'unit_fn', 'args'])):

    def subsample(self, inputs, factor, scope=None):
        # 下采样
        if factor == 1:
            return inputs
        else:
            return slim.max_pool2d(inputs, [1, 1], stride=factor, scope=scope)

    def con2d_same(self, inputs, num_outputs, kernel_size, stride, scope=None):
        if stride == 1:
            return slim.conv2d(inputs, num_outputs, kernel_size, stride=1, padding='SAME', scope=scope)
        else:
            pad_total = kernel_size - 1
            pad_beg = pad_total // 2
            pad_end = pad_total - pad_beg
            inputs = tf.pad(inputs, [[0, 0], [pad_beg, pad_end], [pad_beg, pad_end], [0, 0]])
            return slim.conv2d(inputs, num_outputs, kernel_size, stride=stride, padding='VALID', scope=scope)

