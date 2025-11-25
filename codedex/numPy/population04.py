"""Every metro city's population is constantly changing. Google your favorite city's population in the recent years and create an array for them.

Here are the NYC population from 2023 (top) to 2013 (bottom):

19571216
19673200
19854526
20104710
19463131
19544098
19593849
19636391
19657321
19653431
19626488
Print the first item and the last item. What did you get?
Now find the difference between them using subtraction. How did the population change in the last ten years?
COVID-19 happened during 2020-2022; those were some crazy years. Use slicing, and print the population during those years for your city."""
import numpy as np

population = np.array([19571216, 19673200, 19854526, 20104710, 19463131, 19544098, 19593849, 19636391, 19657321, 19653431, 19626488])

print(f"First item: {population[0]}")
print(f"Last item: {population[-1]}")
print(f"The difference between first and last item: {(population[-1] - population[0])}")

for i in range(1,4):
    print(population[i])