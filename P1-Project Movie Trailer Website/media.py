import webbrowser


class Movie():
    """This class provides a way to store movie related information"""
    # Al ser una variable global el nombre es en mayuscula
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

# Estos son atributos, o datos de la clase Movie()
# A continuacion vemos un constructor, cuando se crea una instancia, es el contructor el que es llamado
# Self se puede pensar como la instancia en cuestion, cuando toy_story se crea, self es la instancia toy_story
# lo que esta debajo del contructor puede ser llamado variables de instancia

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# Este es un metodo de instancia de la clase Movie()
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

