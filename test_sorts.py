import unittest
import random
import sorts
import timeit

class test(unittest.TestCase):
    def setUp(self):
        self.random_seq_size = 10000
        self.random_seq = random.sample(range(self.random_seq_size),\
                self.random_seq_size)
    def test_merge_sort(self):
        start = timeit.default_timer()       
        Y = sorts.merge_sort(self.random_seq)
        end = timeit.default_timer()
        print("Merge sort took %s sec" % str(end-start))
        self.assertEqual(Y, sorted(self.random_seq))
if __name__ == '__main__':
   unittest.main() 
