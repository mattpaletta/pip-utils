from unittest import TestCase
from piputils.search import search


class TestSearch(TestCase):

    def test_tensorflow(self):
        print(list(search(package = "tensorflow")))