"""✨ Here at Codédex, we are 🤩 big fans of music 🎹. The only thing better than a perfect playlist is a playlist with all your favorite songs. Let's create a Python script that organizes the songs into a .txt file. Let's make a playlist!

First, let's define a dictionary to store liked songs:

liked_songs = {
  'title': 'artist'
}

Next, create a function to display and write liked songs to a file:

def write_liked_songs_to_file(liked_songs, file_name):

Open the file in write mode.
Write each song and artist by iterating through the liked_songs dictionary."""

my_liked_songs = {
    "Stay Gold": "Jax Jones, Ado", 
    "Majestic Catastrophe": "Rico Sasaki",
    "adonis": "STIM" 
}


def write_liked_songs_to_file(liked_songs, file_name):
    file = open(file_name, "w")
    file.write("Liked songs:\n")
    for song, artist in liked_songs.items():
        file.write(f"{song} by {artist}\n")
    file.close()

write_liked_songs_to_file(my_liked_songs, "my_liked_songs.txt")