"""Go into your phone and find the number of steps you’ve taken in the last week and add them into an array.

Find the min, max, sum, and average using .min(), .max(), .sum(), .average()."""

import numpy as np

steps = np.array([459,830,693,568,405,905,938])

print(np.min(steps))
print(np.max(steps))
print(np.sum(steps))
print(np.average(steps))

