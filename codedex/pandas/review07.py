"""It's time to let your creativity shine!

Create a DataFrame about a topic of your choice! It should have at least 10 rows and 5 columns.

Once it is created, perform the following operations:

Add a new column
Sort the DataFrame by a particular column
Filter out rows based on one or more conditions
If you're having trouble thinking of topics, here are some ideas to get you started:

Statistics about your favorite sports team
Data about your favorite movies, books, video games, or music
Information about your friends and family
Note: If you need help creating your dataset, feel free to use ChatGPT or another AI tool to get you started. We found the following prompt helped create a good starting DataFrame:

Give me code to create a DataFrame about [your topic] with 10+ rows and 5+ columns. Some of the columns should be about [X, Y, Z]."""

import pandas as pd

data = {
    "Model": [
        "Tesla Model 3", "Tesla Model Y", "Nissan Leaf", "Chevy Bolt EUV",
        "Ford Mustang Mach-E", "Hyundai Ioniq 5", "Kia EV6", "BMW i4",
        "Volkswagen ID.4", "Rivian R1S", "Lucid Air Pure"
    ],
    "Manufacturer": [
        "Tesla", "Tesla", "Nissan", "Chevrolet",
        "Ford", "Hyundai", "Kia", "BMW",
        "Volkswagen", "Rivian", "Lucid"
    ],
    "Range_miles": [272, 330, 149, 247, 312, 303, 310, 301, 275, 316, 419],
    "Battery_kWh": [57, 75, 40, 65, 91, 77, 77, 83, 82, 135, 92],
    "Price_USD": [38500, 45990, 28900, 33995, 42995, 41950, 42900, 52995, 38400, 78400, 69900],
    "Fast_Charge_kW": [170, 250, 100, 55, 150, 235, 235, 200, 125, 220, 300]
}

df = pd.DataFrame(data)
#print(df)

df["do_i_own_it"] = ["False","False","False","False","False","False","False","False","False","False","False"]
#print(df)

sorted_df = df.sort_values(by="Range_miles")
#print(sorted_df)

teslas = df[
    (df["Manufacturer"] == "Tesla")
]
print(teslas)

#max_df = df.max()[2]
#print(max_df)