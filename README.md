# CSPC - Computer Science for Physics and Chemistry

My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup
Create the environment for a given lab:
    conda env create -f PW<n>/Lab\ <X>/environment.yml
    conda activate cspc

---

## PW1 - Lab A: Reproducible Foundations

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

## PW1 --- Lab B

The observed decay data (decay_observed.csv) was plotted alongside the analytical 
decay law N0*e^(-λt) with λ = 0.3. The observed points closely followed the shape 
of the analytical curve, confirming that the data is consistent with exponential 
decay.

The Snakemake pipeline (Snakefile) automates the generation of figure.png from 
decay_observed.csv by running plot.py, and only reruns the plotting step when the 
input data or script has changed.