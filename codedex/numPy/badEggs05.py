"""We've all been taught to check for cracked eggs before purchasing in grocery stores. But did you know that the probability of getting a rotten egg from a lot of 400 eggs is 3.5%?

Suppose we have a factory machine that determines the freshness of an egg (based on the expiration date, cracks in the shell, and smell) then assigns a number:

✨ 100% is a healthy fresh egg.
🤮 0% is completely rotten!
egg_carton1 = np.array([
  [0.89, 0.90, 0.83, 0.89, 0.97, 0.98], 
  [0.95, 0.95, 0.89, 0.95, 0.23, 0.99]
])

egg_carton2 = np.array([
  [0.89, 0.95, 0.84, 0.92, 0.94, 0.93], 
  [0.93, 0.95, 0.02, 0.03, 0.23, 0.99]
])

egg_carton3 = np.array([
  [0.83, 0.95, 0.89, 0.54, 0.37, 0.92], 
  [0.98, 0.99, 0.19, 0.23, 0.89, 0.91]
])

Which carton should you get?

Calculate the average freshness of each of the cartons with np.average() (which we will learn more about in chapter 2) and see which one has the lowest average (least fresh)."""

import numpy as np

egg_carton1 = np.array([
  [0.89, 0.90, 0.83, 0.89, 0.97, 0.98], 
  [0.95, 0.95, 0.89, 0.95, 0.23, 0.99]
])

egg_carton2 = np.array([
  [0.89, 0.95, 0.84, 0.92, 0.94, 0.93], 
  [0.93, 0.95, 0.02, 0.03, 0.23, 0.99]
])

egg_carton3 = np.array([
  [0.83, 0.95, 0.89, 0.54, 0.37, 0.92], 
  [0.98, 0.99, 0.19, 0.23, 0.89, 0.91]
])

print(np.average(egg_carton1))
print(np.average(egg_carton2))
print(np.average(egg_carton3))
