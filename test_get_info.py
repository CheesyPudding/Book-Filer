from unittest import TestCase
from books import get_info


class TestGetInfo(TestCase):
    def test_get_info_not_tuple_2_line_text_file(self):
        expected = {'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L',
                    'Shelf': '12', 'Category': 'Architecture', 'Subject': '20th Century'}
        actual = get_info("Mock_Books_2.txt")  # file will be a dictionary, as tuples need at least 2 items
        self.assertEqual(expected, actual)

    def test_get_info_minimum_3_line_text_file(self):
        expected = ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L',
                     'Shelf': '12', 'Category': 'Architecture', 'Subject': '20th Century'},
                    {'Author': 'Sinclair', 'Title': 'Morrisseau', 'Publisher': 'Editions Franco-Amerique',
                     'Shelf': 'Reading', 'Category': 'Art', 'Subject': 'Canadian'})
        actual = get_info("Mock_Books_1.txt")
        self.assertEqual(expected, actual)

    def test_get_info_4_line_text_file_categories_random_order(self):
        expected = ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L',
                     'Shelf': '12', 'Category': 'Architecture', 'Subject': '20th Century'},
                    {'Author': 'Sinclair', 'Title': 'Morrisseau', 'Publisher': 'Editions Franco-Amerique',
                     'Shelf': 'Reading', 'Category': 'Art', 'Subject': 'Canadian'},
                    {'Author': 'Gore', 'Title': '2001 Household Hints & Dollar Stretchers',
                     'Publisher': 'Hanover House',
                     'Shelf': '9', 'Category': 'Home economics', 'Subject': 'History'})
        actual = get_info("Mock_Books_3.txt")
        self.assertEqual(expected, actual)

    def test_get_info_3_line_text_file_No_Publishers(self):
        expected = ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': None,
                     'Shelf': '12', 'Category': 'Architecture', 'Subject': '20th Century'},
                    {'Author': 'Sinclair', 'Title': 'Morrisseau', 'Publisher': None,
                     'Shelf': 'Reading', 'Category': 'Art', 'Subject': 'Canadian'})
        actual = get_info("Mock_Books_4.txt")
        self.assertEqual(expected, actual)

    def test_get_info_5_line_text_file(self):
        expected = ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L',
                     'Shelf': '12', 'Category': 'Architecture', 'Subject': '20th Century'},
                    {'Author': 'Sinclair', 'Title': 'Morrisseau', 'Publisher': 'Editions Franco-Amerique',
                     'Shelf': 'Reading', 'Category': 'Art', 'Subject': 'Canadian'},
                    {'Author': 'Sawyer', 'Title': 'The Terminal Experiment', 'Publisher': 'Harper Prism',
                     'Shelf': '10', 'Category': 'Fiction', 'Subject': 'SF'},
                    {'Author': 'Silverberg', 'Title': "At Winter's End", 'Publisher': 'Warner Books',
                     'Shelf': '18', 'Category': 'Fiction', 'Subject': 'SF'})
        actual = get_info("Mock_Books_5.txt")
        self.assertEqual(expected, actual)
