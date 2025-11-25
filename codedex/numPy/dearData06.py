"""Dear Data is a book full of postcards sent back and forth between two designers, containing weekly data recorded from their everyday lives. It was a fascinating experiment that combined data science and art and it showed that there's so much interesting data to be found in your day-to-day life! 💌



In this final exercise, you are going to capture some data from your day-to-day... using NumPy arrays! 🔢

Think of something that you do within a day or within a week that can be observered with some number. Some inspirations could be:

🍵 Recording your mood (out of 10) in each waking hour today.
💤 How many hours you slept.
💧 The number of glasses of water you drink everyday this week.
🥱 The number of yawns.
👀 How many ____ you ____.
Use your phone's notes or a notebook to capture this data and then store them in an array.

Does this make sense to keep this data in a 1D array or a 2D array?

Now, use index and slicing to analyze it a bit - what is the average number during waking hours? How about what is the difference between the beginning and the end of the duration?"""

import numpy as np

#10 day data (not real :))

#array in 1d
mood = np.array([3, 5, 9, 7, 1, 3, 8, 5, 7, 10])
hours_slept = np.array([6, 8, 0, 2, 4, 5, 8, 0, 2, 9])
water_drank = np.array([4, 8, 5, 4, 8, 7, 5, 4, 2, 9])
amount_of_yawns = np.array([58, 70, 3, 68, 0, 39, 83, 0, 2, 832])

#same array but in 2d
data = np.array([
    [3, 5, 9, 7, 1, 3, 8, 5, 7, 10],
    [6, 8, 0, 2, 4, 5, 8, 0, 2, 9],
    [4, 8, 5, 4, 8, 7, 5, 4, 2, 9],
    [58, 70, 3, 68, 0, 39, 83, 0, 2, 832]])
#print(data[0])

print(f"average amount of hours slept in 10 days: {np.average(data[1])}")
print(f"average amount of hours slept in 10 days: {np.average(hours_slept)}")