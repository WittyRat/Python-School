"""We've loaded data about popular apps into a DataFrame named apps.

Edit the DataFrame in the following ways:

Begin by adding a column named downloaded that contains True or False depending on whether you have the app downloaded on your phone.
Sort the apps by rating so the highest rated apps are at the top of the DataFrame
Change the name of the column app_name to name."""

import pandas as pd

# App data
app_data = {
  'app_name': [
    'YouTube', 'TikTok', 'Instagram', 'Spotify', 'Duolingo', 
    'Twitter', 'Headspace', 'Discord', 'Depop'
  ],
  'category': [
    'Video', 'Social Media', 'Social Media', 'Music', 'Education',
    'Social Media', 'Health', 'Communication', 'Shopping'
  ],
  'rating': [
    4.7, 4.6, 4.5, 4.6, 4.7,
    4.3, None, 4.7, 4.4
  ],
  'downloads_millions': [
    5000, 3000, 3500, 2000, None,
    1500, 500, 600, 200
  ]
}

# Create the DataFrame
apps = pd.DataFrame(app_data)

apps["downloaded"] = ["True", "True", "False", "True", "False", "False", "False", "True", "False"]
#print(apps)

sorted_apps = apps.sort_values(by="rating", ascending=False)
#print(sorted_apps)

apps = apps.rename(columns={"app_name": "name"})
print(apps)

