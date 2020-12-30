from unittest import TestCase
import io
from unittest.mock import patch
from books import select_new_shelf


class TestSelectNewShelf(TestCase):
    @patch('builtins.input', side_effect=['0'])
    def test_select_new_shelf_no_book_shelf(self, mock_input):
        books_file = ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L',
                       'Shelf': '12', 'Category': 'Architecture', 'Subject': '20th Century'},
                      {'Author': 'Sinclair', 'Title': 'Morrisseau', 'Publisher': 'Editions Franco-Amerique',
                       'Shelf': 'Reading', 'Category': 'Art', 'Subject': 'Canadian'},
                      {'Author': 'Gore', 'Title': '2001 Household Hints & Dollar Stretchers',
                       'Publisher': 'Hanover House',
                       'Shelf': '9', 'Category': 'Home economics', 'Subject': 'History'})
        actual = select_new_shelf(books_file)
        expected = None
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['1'])
    def test_select_new_shelf_first_book_shelf(self, mock_input):
        books_file = ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L',
                       'Shelf': '12', 'Category': 'Architecture', 'Subject': '20th Century'},
                      {'Author': 'Sinclair', 'Title': 'Morrisseau', 'Publisher': 'Editions Franco-Amerique',
                       'Shelf': 'Reading', 'Category': 'Art', 'Subject': 'Canadian'},
                      {'Author': 'Gore', 'Title': '2001 Household Hints & Dollar Stretchers',
                       'Publisher': 'Hanover House',
                       'Shelf': '9', 'Category': 'Home economics', 'Subject': 'History'})
        actual = select_new_shelf(books_file)
        expected = '12'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['2'])
    def test_select_new_shelf_second_book_shelf(self, mock_input):
        books_file = ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L',
                       'Shelf': '12', 'Category': 'Architecture', 'Subject': '20th Century'},
                      {'Author': 'Sinclair', 'Title': 'Morrisseau', 'Publisher': 'Editions Franco-Amerique',
                       'Shelf': 'Reading', 'Category': 'Art', 'Subject': 'Canadian'},
                      {'Author': 'Gore', 'Title': '2001 Household Hints & Dollar Stretchers',
                       'Publisher': 'Hanover House',
                       'Shelf': '9', 'Category': 'Home economics', 'Subject': 'History'})
        actual = select_new_shelf(books_file)
        expected = '9'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['3'])
    def test_select_new_shelf_second_book_shelf(self, mock_input):
        books_file = ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L',
                       'Shelf': '12', 'Category': 'Architecture', 'Subject': '20th Century'},
                      {'Author': 'Sinclair', 'Title': 'Morrisseau', 'Publisher': 'Editions Franco-Amerique',
                       'Shelf': 'Reading', 'Category': 'Art', 'Subject': 'Canadian'},
                      {'Author': 'Gore', 'Title': '2001 Household Hints & Dollar Stretchers',
                       'Publisher': 'Hanover House',
                       'Shelf': '9', 'Category': 'Home economics', 'Subject': 'History'})
        actual = select_new_shelf(books_file)
        expected = 'Reading'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['4'])
    def test_select_new_shelf_out_of_range_book_shelf(self, mock_input):
        books_file = ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L',
                       'Shelf': '12', 'Category': 'Architecture', 'Subject': '20th Century'},
                      {'Author': 'Sinclair', 'Title': 'Morrisseau', 'Publisher': 'Editions Franco-Amerique',
                       'Shelf': 'Reading', 'Category': 'Art', 'Subject': 'Canadian'},
                      {'Author': 'Gore', 'Title': '2001 Household Hints & Dollar Stretchers',
                       'Publisher': 'Hanover House',
                       'Shelf': '9', 'Category': 'Home economics', 'Subject': 'History'})
        actual = select_new_shelf(books_file)
        expected = None
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['1'])
    def test_select_new_shelf_only_one_book_shelf(self, mock_input):
        books_file = ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L',
                       'Shelf': 'Reading', 'Category': 'Architecture', 'Subject': '20th Century'},
                      {'Author': 'Sinclair', 'Title': 'Morrisseau', 'Publisher': 'Editions Franco-Amerique',
                       'Shelf': 'Reading', 'Category': 'Art', 'Subject': 'Canadian'},
                      {'Author': 'Gore', 'Title': '2001 Household Hints & Dollar Stretchers',
                       'Publisher': 'Hanover House',
                       'Shelf': 'Reading', 'Category': 'Home economics', 'Subject': 'History'})
        actual = select_new_shelf(books_file)
        expected = 'Reading'
        self.assertEqual(expected, actual)
