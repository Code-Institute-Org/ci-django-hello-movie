from django.test import TestCase
from .models import Movie


class TestModels(TestCase):
    # dict of fields to create a movie object
    data = {
        "title": "Blade Runner",
        "director": "Ridley Scott",
        "genre": "Science Fiction",
        "summary": "A blade runner must pursue and terminate four replicants who stole a ship in space, and have returned to Earth to find their creator.",
        "rating": 4,
        "imdb_link": "https://www.imdb.com/title/tt0083658/",
    }

    # create a movie object before tests are run using data dict
    def setUp(self):
        movie_data = self.data
        Movie.objects.create(**movie_data)

    def test_watched_defaults_to_false(self):
        movie = Movie.objects.get(id=1)
        self.assertFalse(movie.watched)

    def test_movie_string_method_returns_title(self):
        movie = Movie.objects.get(id=1)
        self.assertEqual(str(movie), "Blade Runner")
