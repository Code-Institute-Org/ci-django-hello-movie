from django.test import TestCase
from .forms import MovieForm


class TestForm(TestCase):
    def test_movie_title_is_required(self):
        form = MovieForm({"title": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("title", form.errors.keys())
        self.assertEqual(form.errors["title"][0], "This field is required.")

    def test_summary_field_is_not_required(self):
        form = MovieForm(
            {
                "title": "Blade Runner",
                "director": "Ridley Scott",
                "genre": "Science Fiction",
                "rating": 4,
                "watched": False,
                "imdb_link": "https://www.imdb.com/title/tt0083658/",
            }
        )
        self.assertTrue(form.is_valid())

    def test_watched_field_is_not_required(self):
        form = MovieForm(
            {
                "title": "Blade Runner",
                "director": "Ridley Scott",
                "genre": "Science Fiction",
                "rating": 4,
                "summary": "a",
                "imdb_link": "https://www.imdb.com/title/tt0083658/",
            }
        )
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = MovieForm()
        self.assertEqual(
            form.Meta.fields,
            [
                "title",
                "director",
                "genre",
                "summary",
                "rating",
                "watched",
                "imdb_link",
            ],
        )
