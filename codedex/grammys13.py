"""For many, music is so personal. We have created a playlist of songs that have won the “Song of the Year” 🏆 Grammy award in the past 5 years.

Let's play around with the data!

# List of songs with their durations (in minutes)
playlist = [('What Was I Made For?', 3.42), ('Just Like That', 5.05), ('Song 3', 6.55), ('Leave The Door Open', 4.02), ('I Can\'t Breath', 4.47), ('Bad Guy', 3.14)] 

First, use the filter() function to pick out the songs that are longer than 5 minutes (i.e., 5.00).

Next, use map() to convert all the durations of the songs in your playlist from minutes to seconds.

Lastly, add up the total playtime of the playlist with reduce().

Since map(), filter(), and reduce() all use function parameters, it may be helpful to define separate named functions for them:

A longer_than_five_minutes() function for filter().
A minutes_to_seconds() function for map().
An add_durations() function for reduce()."""

from functools import reduce

# List of songs with their durations (in minutes)
playlist = [('What Was I Made For?', 3.42), ('Just Like That', 5.05), ('Song 3', 6.55), ('Leave The Door Open', 4.02), ('I Can\'t Breath', 4.47), ('Bad Guy', 3.14)]


def filter_songs(song):
    return song[1] > 5.00


def min_to_sec(song):
    duration = song[1]
    minutes = int(duration)
    seconds = (duration-minutes)*100
    total_time = minutes * 60 + round(seconds)
    return total_time


def total_playtime(total, song):
    duration = song[1]
    return total + duration


filtered = filter(filter_songs, playlist)
song_time = map(min_to_sec, playlist)
add_durations = reduce(total_playtime, playlist, 0)


print(list(filtered))
print(list(song_time))
print(add_durations)

    
