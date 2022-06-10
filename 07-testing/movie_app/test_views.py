from django.test import TestCase
from .models import Movie


class TestViews(TestCase):
    # dict of fields to create a movie object
    data = {
        "title": "Blade Runner",
        "director": "Ridley Scott",
        "genre": "Science Fiction",
        "summary": "A blade runner must pursue and terminate four replicants who stole a ship in space, and have returned to Earth to find their creator.",
        "rating": 4,
        "watched": False,
        "imdb_link": "https://www.imdb.com/title/tt0083658/",
    }

    # create a movie object before tests are run using data dict
    def setUp(self):
        movie_data = self.data
        Movie.objects.create(**movie_data)

    def test_get_movie_list(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "movie_app/movie_app_home.html")

    def test_movie_app_add_page(self):
        response = self.client.get("/add")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "movie_app/movie_app_add.html")

    def test_movie_app_edit_page(self):
        movie = Movie.objects.get(id=1)
        response = self.client.get(f"/edit/{movie.id}")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "movie_app/movie_app_edit.html")

    def test_can_add_movie(self):
        movie_data = self.data
        response = self.client.post("/add", movie_data)
        self.assertRedirects(response, "/")

    def test_can_delete_movie(self):
        movie = Movie.objects.get(id=1)
        response = self.client.get(f"/delete/{movie.id}")
        self.assertRedirects(response, "/")
        movie_exists = Movie.objects.filter(id=movie.id)
        self.assertEqual(len(movie_exists), 0)

    def test_can_toggle_movie(self):
        movie = Movie.objects.get(id=1)
        self.assertFalse(movie.watched)
        response = self.client.get(f"/toggle/{movie.id}")
        self.assertRedirects(response, "/")
        updated_movie = Movie.objects.get(id=movie.id)
        self.assertTrue(updated_movie.watched)

    def test_can_edit_item(self):
        movie = Movie.objects.get(id=1)
        response = self.client.post(
            f"/edit/{movie.id}",
            {
                "title": "Blade Runner",
                "director": "Ridley Scott",
                "genre": "Science Fiction",
                "summary": "A blade runner must pursue and terminate four replicants who stole a ship in space, and have returned to Earth to find their creator.",
                "rating": 5,
                "watched": False,
                "imdb_link": "https://www.imdb.com/title/tt0083658/",
            },
        )
        self.assertRedirects(response, "/")
        updated_movie = Movie.objects.get(id=movie.id)
        self.assertEqual(updated_movie.rating, 5)
