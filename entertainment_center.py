import fresh_tomatoes
import media

# creating a new movie instance called toy_story.
toy_story = media.Movie("Toy Story",
                        "A story of a boy",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # noqa
                        "http://www.youtube.com/watch?v=-9ceBgWV8io")

# creating a new movie instance called Avatar
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # noqa
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")

# creating a new movie instance called CCV
CCV = media.Movie("CCV",
                  "A bloody power struggle erupts between three brothers",
                  "https://upload.wikimedia.org/wikipedia/en/3/3e/Chekka_Chivantha_Vaanam.jpg",  # noqa
                  "https://www.youtube.com/watch?v=qDPjDR297Wc")

# creating a new movie instance called VTV
VTV = media.Movie("VTV",
                  "romantic",
                  "https://upload.wikimedia.org/wikipedia/en/a/a8/Vinnaithaandi_Varuvaaya_poster.jpg",  # noqa
                  "http://www.youtube.com/watch?v=-9ceBgWV8io")

# creating a new movie instance called Ninty Six
Ninty_six = media.Movie("nintysix",
                        "romantic",
                        "https://upload.wikimedia.org/wikipedia/commons/8/80/Starfortbattlefield.jpg",  # noqa
                        "https://www.youtube.com/watch?v=r0synl-lI4I")

# creating a new movie instance called NOTA
NOTA = media.Movie("NOTA",
                   "Political",
                   "https://upload.wikimedia.org/wikipedia/en/7/72/Nota_film_poster.jpg",  # noqa
                   "https://www.youtube.com/watch?v=r0synl-lI4I")

# Creating an array with all the movies and call fresh_tomatoes open movie function to view all of the listed movies in html page.  # noqa
movies = [toy_story, avatar, CCV, VTV, Ninty_six, NOTA]
fresh_tomatoes.open_movies_page(movies)
