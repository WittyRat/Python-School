"""Halley's Comet is a comet visible from Earth every 75 years. It is the only known "short-period comet" that is consistently visible to the naked eye from Earth. It was last seen in 1986 and the next one will happen in 2061. 💫

Using .arange(), create an array of numbers with the years when Halley's Comet will appear next from year 1986 to 3000."""

import numpy as np

arr = np.arange(start=1986, stop=3000, step=75)
print(arr)