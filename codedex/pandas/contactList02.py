"""First thing first, import pandas at the top of the file.

Then, create a DataFrame named contacts containing information about your friends, family, or fictional characters. Your DataFrame should have at least 3 columns and 4 rows.

Feel free to be creative about what columns to include. If you need inspiration, you could consider columns like name, age, phone_number, astrological_sign. 💫"""

import pandas as pd

data = [
    ["Bart", 10, "939-555-0113", "Taurus"],
    ["Lisa", 8, "939-555-0114", "Virgo"],
    ["Homer", 39, "939-555-0115", "Taurus"],
    ["Marge", 36, "939-555-0116", "Pisces"]
    ]

contacts = pd.DataFrame(data, columns=["name", "age", "phone_number", "astrological_sign"])
print(contacts)
