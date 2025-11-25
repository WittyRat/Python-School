"""Titanic is a classic movie about one of the most famous shipwrecks in human history. 🚢

Below is an array filled with real data from 50 of the passengers:

Passenger id (1 to 50)
Survived: 0 for no and 1 for yes.
Passenger class: 1 for Upper, 2 for Middle, 3 for Lower.
Age: 0-74

You can find the full dataset here: https://github.com/datasciencedojo/datasets/blob/master/titanic.csv

Your job as a data analyst is to find the following information:

What is the shape of this array?
What is the average age of the passengers?
What is the passenger number of the oldest passenger? Who is the youngest?
What is the percentage of folks that survived?
And now the final question of all:

What is the percentage of the folks that survived based on their passenger class? 😮"""

import numpy as np

passengers = np.array([
   [1, 0, 3, 22],
   [2, 1, 1, 38],
   [3, 1, 3, 26],
   [4, 1, 1, 35],
   [5, 0, 3, 35],
   [6, 0, 3, 18],
   [7, 0, 1, 54],
   [8, 0, 3, 2],
   [9, 1, 3, 27],
  [10, 1, 2, 14],
  [11, 1, 3, 4],
  [12, 1, 1, 58],
  [13, 0, 3, 20],
  [14, 0, 3, 39],
  [15, 0, 3, 14],
  [16, 1, 2, 55],
  [17, 0, 3, 2],
  [18, 1, 2, 12],
  [19, 0, 3, 31],
  [20, 1, 3, 8],
  [21, 0, 2, 35],
  [22, 1, 2, 34],
  [23, 1, 3, 15],
  [24, 1, 1, 28],
  [25, 0, 3, 8],
  [26, 1, 3, 38],
  [27, 0, 3, 2],
  [28, 0, 1, 1],
  [29, 1, 3, 5],
  [30, 0, 3, 18],
  [31, 0, 1, 40],
  [32, 1, 1, 70],
  [33, 1, 3, 33],
  [34, 0, 2, 66],
  [35, 0, 1, 28],
  [36, 0, 1, 42],
  [37, 1, 3, 5],
  [38, 0, 3, 18],
  [39, 0, 3, 18],
  [40, 1, 3, 14],
  [41, 0, 3, 40],
  [42, 0, 2, 27],
  [43, 0, 3, 29],
  [44, 1, 2, 0],
  [45, 1, 3, 19],
  [46, 0, 3, 33],
  [47, 0, 3, 14],
  [48, 1, 3, 22],
  [49, 0, 3, 41],
  [50, 0, 3, 18]
])

print(f"Shape of this array is: {np.shape(passengers)}")

print(f"Average age of the passenger is: {np.average(passengers, axis=0)[3]}")

biggest_age = np.max(passengers, axis=0)[3]
smallest_age = np.min(passengers, axis=0)[3]

for i in range(len(passengers)):
    if passengers[i][3] == biggest_age:
        print(f"The passenger number of the oldest passenger is: {passengers[i][0]}")
    
    if passengers[i][3] == smallest_age:
        print(f"the youngest person is aged: {smallest_age}")

survivors = np.sum(passengers, axis = 0)[1]
amount_of_people = np.max(passengers, axis = 0)[0]

print(f"{(survivors/amount_of_people)*100}% of people survived")