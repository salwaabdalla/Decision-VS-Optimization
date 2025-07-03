# Decision-VS-Optimization
# Decision vs Optimization – Subset Sum Problem (NP-Completeness)

This repository contains two Python implementations demonstrating the difference between **Decision** and **Optimization** problems using the classic **Subset Sum Problem**, a well-known NP-complete problem in computational complexity.



# Files Included

- `decision_subset_sum.py` – Checks whether a subset of numbers adds up exactly to a given target (YES/NO).
- `optimization_subset_sum.py` – Finds the largest subset sum that does not exceed the given target.


# Problem Overview

##  Decision Problem:
> Is there a subset of the array that sums exactly to the target?

**Output:** `True` or `False`

## Optimization Problem:
> What is the maximum possible sum ≤ target using any subset of the array?

**Output:** A number (the best possible sum)

---

# Example Output

```bash
$ python decision_subset_sum.py
Subset sum possible: True

$ python optimization_subset_sum.py
Closest subset sum to 30 is: 30
