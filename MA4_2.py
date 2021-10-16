#!/usr/bin/env python3

from integer import Integer
import matplotlib.pyplot as plt
from time import perf_counter as perf

def main():
    
	timescpp = []
	timespy = []
	values = range(30, 45)

	for n in values:
		f = Integer(n)

		print("Timing for C++ where n =", n)
		start = perf()
		print(f.fib())
		end = perf()
		t = end - start
		print(round("Time: ", t), 3)
		timescpp.append(t)

		print("Timing for Python where n =", n)
		start = perf()
		print(fib_pure_py(n))
		end = perf()
		t = end - start
		print(round("Time: ", t), 3)
		timespy.append(t)
 
	print("Timing for C++ where n = 47")
	f = Integer(47)
	start = perf()
	print(f.fib())
	end = perf()
	t = end - start
	print(round("Time: ", t), 3)
 
	plt.plot(values, timescpp, 'r.', values, timespy, 'b.')
	plt.title("Computing time for fib(n)")
	plt.xlabel("n")
	plt.ylabel("Seconds")
 	plt.legend('C++', 'Python', loc="upper left")
	plt.savefig("FibCompute.png")

if __name__ == '__main__':
	main()
 
def fib_pure_py(n):
    if n <= 1:
        return n
    else:
        return(fib_pure_py(n-1) + fib_pure_py(n-2))