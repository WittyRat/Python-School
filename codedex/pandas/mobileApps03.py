"""Everyone is chronically on their phone these days. 📱👀

We've created a DataFrame named apps that contains (fictional) data about popular apps:

Call .head() or .tail() to see only the start or end of the DataFrame.
Call .info(). Are there any missing values?
Call .describe(). What is the average number of downloads?"""
import pandas as pd

# Popular mobile apps
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

#print(apps.head())
#print(apps.info())
print(apps.describe())
