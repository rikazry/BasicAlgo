import unittest
import random
import sorts
import timeit

class test(unittest.TestCase):
    def setUp(self):
        self.random_seq_size = 100 
        self.random_seq = random.sample(range(self.random_seq_size),\
                self.random_seq_size)
    def test_merge_sort(self):
        start = timeit.default_timer()       
        Y = sorts.merge_sort(self.random_seq)
        end = timeit.default_timer()
        print("Merge sort took %s sec" % str(end-start))
        self.assertEqual(Y, sorted(self.random_seq))

    def test_quick_sort(self):
        start = timeit.default_timer()       
        Y = sorts.quick_sort(self.random_seq)
        end = timeit.default_timer()
        print("Quick sort took %s sec" % str(end-start))
        self.assertEqual(Y, sorted(self.random_seq))

    def test_quick_select(self):
        sorted_list = sorted(self.random_seq)
        for k in range(len(self.random_seq)):
            self.assertEqual(sorted_list[k],\
                    sorts.quick_select(self.random_seq,k))
        
        
if __name__ == '__main__':
   unittest.main() 
