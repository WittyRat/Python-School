"""Dungeons & Dragons is a tabletop role-playing game where players create characters and embark on adventures in a fantasy world. 

Here's a DataFrame named characters that holds info on 10 D&D heroes.

Practice selecting individual columns:

Select only the name column and store it in a variable called character_names. Then print the type of this variable. What do you get?
Select the name, level, hp columns and store them in a variable called basic_stats.
Select all columns except alignment and store that in a variable called removed_alignment."""

import pandas as pd

# D&D characters data
characters_data = {
  'name': ['Thorne', 'Elira', 'Glim', 'Brug', 'Nyx', 'Kael', 'Mira', 'Drogan', 'Zara', 'Fenwick'],
  'race': ['Elf', 'Human', 'Gnome', 'Half-Orc', 'Tiefling', 'Dragonborn', 'Halfling', 'Dwarf', 'Aasimar', 'Goblin'],
  'class': ['Ranger', 'Cleric', 'Wizard', 'Barbarian', 'Rogue', 'Paladin', 'Bard', 'Fighter', 'Sorcerer', 'Warlock'],
  'level': [5, 3, 4, 2, 6, 7, 3, 5, 4, 2],
  'hp': [42, 28, 33, 25, 48, 56, 30, 44, 36, 24],
  'alignment': [
    'Chaotic Good', 'Lawful Good', 'Neutral', 'Chaotic Neutral', 'Chaotic Evil',
    'Lawful Neutral', 'Neutral Good', 'Neutral', 'Chaotic Good', 'Lawful Evil'
  ]
}

# Create the DataFrame
characters = pd.DataFrame(characters_data)

character_names = characters["name"]
print(character_names)

basic_stats = characters[["name", "level", "hp"]]
print(basic_stats)

removed_alignment = characters.drop("alignment", axis=1)
print(removed_alignment)