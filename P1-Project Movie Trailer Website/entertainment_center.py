import media
import fresh_tomatoes

# Arrays and lists are actually not the same thing 99.9% of the time, you'll want to use lists.
# They're flexible, and good for pretty much every purpose.
# toy_story y Avatar son instancias
toy_story = media.Movie("Toy Story",
                        "A story if a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#Con la sgte linea solo impime por pantalla la storyLine, que seria la 2da variable de instancia
#print (toy_story.storyline)



avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

#llama al metodo de instancia creado en la clase media.py y reproduce el trailer de la pelicula.
#avatar.show_trailer()



school_of_rock = media.Movie("School of Rock",
                             "Using rock music to learn at school",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")


ratatouille = media.Movie("Ratatouille",
                          "A rat is a cheff in Paris",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=uVeNEbh3A4U")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "Going back in time to meet authors",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=U_3gIxrcWK8")

hunger_games = media.Movie("Hunger Games",
                           "A really real reality show",
                           "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=M_8Jwh8K_Ns")

# arrays de todas las peliculas
movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]

# esta funcion toma un array para generar una lista de peliculas en una webPage, por eso se le pasa el argumento movies
fresh_tomatoes.open_movies_page(movies)

#Imprime el array declarado en la clase media.py
#print (media.Movie.VALID_RATINGS)

#Imprime la documentacion del codigo dejada entre triple " en la clase media.py
#print(media.Movie.__doc__)