import time
from . import misc


class Time_Block:

    def __init__(self, block_name='block'):
        self.block_name = block_name

    def __enter__(self):
        self.t0 = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        t = misc.sigfig(time.time() - self.t0, 5)
        print('Time taken for ' + str(self.block_name) + ': ' + t + ' s')
