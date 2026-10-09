# CSPC - Computer Science for Physics and Chemistry

My coursework repository. Each practical is under PW<n>/Lab <X>/.

# Setup
Create the environment for a given lab:
    conda env create -f PW<n>/Lab\ <X>/environment.yml
    conda activate cspc

# PW1 - Lab A: Reproducible Foundations

**What I built:**
- A radioactive decay simulation (pure-Python loop and vectorised NumPy versions), with tests and a speed comparison script.

**Speed comparison (loop vs NumPy):**
- loop  : 3.9410 s
- numpy : 0.0004 s
- speed-up: 11258.6x faster

**Tests:** all passing? yes (3 passed: test_starts_at_N0, test_rejects_negative_rate, test_matches_law)

**Conclusion:**
- The vectorised NumPy version is dramatically faster than the pure-Python loop because it replaces the per-atom Python-level loop with a single batched operation (`rng.binomial`) handled in compiled C code. I learned how much overhead pure-Python loops carry for large-scale numerical work, and how `pytest.raises` and `pytest.approx` let you test both error handling and statistical/floating-point behaviour cleanly. No major problems encountered.

---

All Git actions from the VSCode terminal, using git commands. Attendance at this practical is mandatory.

# PW1 --- Lab B

The observed decay data (decay_observed.csv) was plotted alongside the analytical 
decay law N0*e^(-λt) with λ = 0.3. The observed points closely followed the shape 
of the analytical curve, confirming that the data is consistent with exponential 
decay.

The Snakemake pipeline (Snakefile) automates the generation of figure.png from 
decay_observed.csv by running plot.py, and only reruns the plotting step when the 
input data or script has changed.
<<<<<<< HEAD
# PW2 --- Lab A
=======
## PW2 --- Lab A
>>>>>>> 8e269a40d6d9b0cd4ad38cde2ce82e5a38ab3732

The mean acceleration I measured from the free-fall data was -8.58 m/s^2, roughly consistent with -g, confirming the object is in free fall.

The acceleration is very noisy (large standard deviation) because differentiation divides the difference of nearby noisy measurements by a small time step (0.1 s), so noise is amplified, and taking two derivatives amplifies it twice, which makes the acceleration swing wildly while the position looks smooth.

The standard deviation of the acceleration was about 28.7 m/s^2, far larger than g itself.

Integrating the noisy acceleration back up recovered the position to within 0.78 m of the measured values (at most), because integration is a smoothing operation that suppresses noise, the opposite of differentiation.
# PW2 --- Lab B

#  Part 2: Three routes to a minimum
- On f(x)=(x-3)^2+1 all three methods (gradient descent, Newton, SLSQP) reach x ≈ 3.
- On g(x)=x^4-3x^2+x+5 from x0=0: gradient descent and SLSQP found the global
  minimum x ≈ -1.30 (g ≈ 1.486). Newton found x ≈ 0.170 where g'' = -5.65 < 0,
  so it is a MAXIMUM, not a minimum (Newton only solves g'(x)=0 and does not
  distinguish minima from maxima).
- From x0=2: gradient descent and Newton found the local minimum x ≈ 1.131
  (g'' = 9.35 > 0, g ≈ 3.93), while SLSQP jumped to the global minimum x ≈ -1.30.
- Conclusion: on a convex problem the methods agree; on a complicated landscape
  the starting point and the algorithm both determine which stationary point is found.

# Part 3: Reaction rate
Fitted first-order rate constant k = 0.262 (close to the expected ≈ 0.25; the
difference comes from measurement noise). The fitted curve passes through the data.

# Part 4: Equilibrium
Newton (root-finding) and SLSQP (minimising the squared imbalance) agree: x = 0.664.
Equilibrium composition: H2 = 0.336 mol, I2 = 0.336 mol, HI = 1.328 mol.

#  Part 5: Titration
Equivalence point at V = 50.00 mL (pH = 7.00), where the pH curve jumps and its slope peaks.
