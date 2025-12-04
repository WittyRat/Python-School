"""This project will generate your very own verse of the classic carol "Jingle Bells".
There are lots of other silly versions out there involving everything from Batman to My Little Pony,
so this is an opportunity for you to make your very own.

If you've ever played the game Mad Libs, or even made the version we have over on Mission Encodeable (find it here),
where you enter various words and are then presented with a silly sentence, it works in a very similar way."""

BELL_ASCII_ART = """			   			  		
				   _,--._
                                 ,'  _.._`.
                            ,^.,' ,-" _," ;
                   _,----.._\\|( _/,--"  ,<
                 ,'     ____(_))< ___..".  `.
                :  _,-"__,-" (_)-.      ,\\.  \
                :,'..-"  _,-")|(\\ `._.-"_,\\  \
                 `.__ ,-"    '-`'   \\.-"   Y  :
                 /  /:-...______...-:      |  |
                (  ( |-...______...-'      ;  ;_
                 \\ ,\\|              |     /,^/  ;._
                  `  .              .        _,'   ;
                     :              :    _,-'    ,"
                     '              ` ,-'     _,"
                    '                '    _,-"`.
                   ;`--...______,,,--":.-"     ;
                  :                    :  `..."
                  '---....______,,,,---'
                           :     ;
                            `.,."          
"""

def generate_lyrics(noun, animal, place_plural, verb):

    carol = f"Jingle bells, jingle bells, jingle all the way!\nDashing through the {noun}\nOn a one-{animal}-open-sleigh\nO'er the {place_plural} we go\n{verb} all the way."
    return carol

print(BELL_ASCII_ART)
print("Welcome user!")
noun = input("Give me a noun: ")
animal = input("Give me an animal: ")
place = input("Give me a place: ")
verb = input("Give me a verb: ")
print(generate_lyrics(noun, animal, place, verb))