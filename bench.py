#!/usr/bin/env python
import time, random

  # * For each N = 2^4, 2^8, 2^12, 2^16, 2^20:
  #   * Create a set S1, and time the following:
  #     * Insert each even number in range(0, N) in order into a set S1
  #     * Check whether S1 contains each value in range(0, N)
  #   * Create a list of N random numbers, and a new set S2. Time the following:
  #     * Insert the first N/2 random numbers into S2
  #     * Check whether S2 contains each random number

SIZES = [2**5, 2**9, 2**13, 2**17]
  
def bench(set_impl):
    name = set_impl.__name__
    for size in SIZES:
        s1 = set_impl()
        n_size =  size / 2
       
        start_time = time.time()
        for i in range(0, size):
            if i % 2 == 0:
                s1.insert(i)
        end_time = time.time()
        
        insertion_nonrandom = end_time - start_time

        start_time_lookup = time.time()
        for i in range(0, size):
            s1.contains(i)
        end_time_lookup = time.time()

        contains_nonrandom =  end_time_lookup - start_time_lookup
        
        random_numbers = []        
        s2 = set_impl()

        for i in range(0, size):
            random_numbers.append(random.random())

        start_time_random = time.time()
        for i in range(0, size/2):
            s2.insert(random_numbers[i])
        end_time_random = time.time()
        
        insertion_random = end_time_random - start_time_random

        start_time_random_lookup = time.time()
        for number in random_numbers:
            s2.contains(number)
        end_time_random_lookup = time.time()

        contains_random = end_time_random_lookup - start_time_random_lookup

        line = '\n' + str(n_size) + '\t' + name + '\t' + "insertion_nonrandom" + '\t' + str(insertion_nonrandom) + \
               '\n' + str(n_size) + '\t' + name + '\t' + "contains_nonrandom" + '\t' + str(contains_nonrandom) + \
               '\n' + str(n_size) + '\t' + name + '\t' + "insertion_random" + '\t' + str(insertion_random) + \
               '\n' + str(n_size) + '\t' + name + '\t' + "contains_random" + '\t' + str(contains_random) 

        
        with open("/Users/Jeena/Desktop/bench_output.tsv", "a") as outfile:
            outfile.write(line)









        

        
