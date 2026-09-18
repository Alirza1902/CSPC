"""
Compare the speed of the pure-Python loop version vs the vectorised
NumPy version of the decay simulation.
"""

import time
from decay import simulate, simulate_loop

N0 = 200_000
lam = 0.4

start = time.perf_counter()
simulate_loop(N0, lam)
loop_time = time.perf_counter() - start

start = time.perf_counter()
simulate(N0, lam)
numpy_time = time.perf_counter() - start

speedup = loop_time / numpy_time

print(f"Pure-Python loop time: {loop_time:.4f} s")
print(f"NumPy vectorised time: {numpy_time:.4f} s")
print(f"NumPy is {speedup:.1f}x faster")
