import unittest

from pages.brower_engine import BrowerEngine
from pages.movie_reviews import MovieReviews


class TestMovieReviews(unittest.TestCase):
    driver = BrowerEngine().init_driver()

    def test_movie_reviews(self):
        MovieReviews(driver=self.driver).search()