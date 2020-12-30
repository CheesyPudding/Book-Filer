from unittest import TestCase
import io
from unittest.mock import patch
from books import search_category


class TestSearchCategory(TestCase):
    @patch('builtins.input', side_effect=['Gore'])
    def test_search_category_author_Gore(self, mock_input):
        books_file = ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L',
                       'Shelf': '12', 'Category': 'Architecture', 'Subject': '20th Century'},
                      {'Author': 'Sinclair', 'Title': 'Morrisseau', 'Publisher': 'Editions Franco-Amerique',
                       'Shelf': 'Reading', 'Category': 'Art', 'Subject': 'Canadian'},
                      {'Author': 'Gore', 'Title': '2001 Household Hints & Dollar Stretchers',
                       'Publisher': 'Hanover House',
                       'Shelf': '9', 'Category': 'Home economics', 'Subject': 'History'})
        actual = search_category(books_file, "Author")
        expected = ({'Author': 'Gore', 'Title': '2001 Household Hints & Dollar Stretchers',
                     'Publisher': 'Hanover House', 'Shelf': '9', 'Category': 'Home economics', 'Subject': 'History'},)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=[''])
    def test_search_category_all_results(self, mock_input):
        books_file = ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L',
                       'Shelf': '12', 'Category': 'Architecture', 'Subject': '20th Century'},
                      {'Author': 'Sinclair', 'Title': 'Morrisseau', 'Publisher': 'Editions Franco-Amerique',
                       'Shelf': 'Reading', 'Category': 'Art', 'Subject': 'Canadian'},
                      {'Author': 'Gore', 'Title': '2001 Household Hints & Dollar Stretchers',
                       'Publisher': 'Hanover House',
                       'Shelf': '9', 'Category': 'Home economics', 'Subject': 'History'})
        actual = search_category(books_file, "Author")
        expected = ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L',
                     'Shelf': '12', 'Category': 'Architecture', 'Subject': '20th Century'},
                    {'Author': 'Sinclair', 'Title': 'Morrisseau', 'Publisher': 'Editions Franco-Amerique',
                     'Shelf': 'Reading', 'Category': 'Art', 'Subject': 'Canadian'},
                    {'Author': 'Gore', 'Title': '2001 Household Hints & Dollar Stretchers',
                     'Publisher': 'Hanover House',
                     'Shelf': '9', 'Category': 'Home economics', 'Subject': 'History'})
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['sadsadksadjakjkv'])
    def test_search_category_random_input_subject(self, mock_input):
        books_file = ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L',
                       'Shelf': '12', 'Category': 'Architecture', 'Subject': '20th Century'},
                      {'Author': 'Sinclair', 'Title': 'Morrisseau', 'Publisher': 'Editions Franco-Amerique',
                       'Shelf': 'Reading', 'Category': 'Art', 'Subject': 'Canadian'},
                      {'Author': 'Gore', 'Title': '2001 Household Hints & Dollar Stretchers',
                       'Publisher': 'Hanover House',
                       'Shelf': '9', 'Category': 'Home economics', 'Subject': 'History'})
        actual = search_category(books_file, "Subject")
        expected = ()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['ar'])
    def test_search_category_multiple_input_results(self, mock_input):
        books_file = ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L',
                       'Shelf': '12', 'Category': 'Architecture', 'Subject': '20th Century'},
                      {'Author': 'Sinclair', 'Title': 'Morrisseau', 'Publisher': 'Editions Franco-Amerique',
                       'Shelf': 'Reading', 'Category': 'Art', 'Subject': 'Canadian'},
                      {'Author': 'Gore', 'Title': '2001 Household Hints & Dollar Stretchers',
                       'Publisher': 'Hanover House',
                       'Shelf': '9', 'Category': 'Home economics', 'Subject': 'History'})
        actual = search_category(books_file, "Category")
        expected = ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L',
                     'Shelf': '12', 'Category': 'Architecture', 'Subject': '20th Century'},
                    {'Author': 'Sinclair', 'Title': 'Morrisseau', 'Publisher': 'Editions Franco-Amerique',
                     'Shelf': 'Reading', 'Category': 'Art', 'Subject': 'Canadian'},)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['Garbage Bin'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_category_invalid_shelf_message(self, mock_output, mock_input):
        books_file = ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L',
                       'Shelf': '12', 'Category': 'Architecture', 'Subject': '20th Century'},
                      {'Author': 'Sinclair', 'Title': 'Morrisseau', 'Publisher': 'Editions Franco-Amerique',
                       'Shelf': 'Reading', 'Category': 'Art', 'Subject': 'Canadian'},
                      {'Author': 'Gore', 'Title': '2001 Household Hints & Dollar Stretchers',
                       'Publisher': 'Hanover House',
                       'Shelf': '9', 'Category': 'Home economics', 'Subject': 'History'})
        search_category(books_file, "Shelf")
        printed_actual = mock_output.getvalue()
        expected = "\n" \
                   "Searching by Shelf..." \
                   "\n\n\n" \
                   "Found 0 result(s) for books with shelf 'Garbage Bin': " \
                   "\n\n"
        self.assertEqual(expected, printed_actual)

    @patch('builtins.input', side_effect=['Skyscraper'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_category_valid_title_message(self, mock_output, mock_input):
        books_file = ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L',
                       'Shelf': '12', 'Category': 'Architecture', 'Subject': '20th Century'},
                      {'Author': 'Sinclair', 'Title': 'Morrisseau', 'Publisher': 'Editions Franco-Amerique',
                       'Shelf': 'Reading', 'Category': 'Art', 'Subject': 'Canadian'},
                      {'Author': 'Gore', 'Title': '2001 Household Hints & Dollar Stretchers',
                       'Publisher': 'Hanover House',
                       'Shelf': '9', 'Category': 'Home economics', 'Subject': 'History'})
        search_category(books_file, "Title")
        printed_actual = mock_output.getvalue()
        book = {'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L',
                'Shelf': '12', 'Category': 'Architecture', 'Subject': '20th Century'}
        expected = f"\n" \
                   f"Searching by Title..." \
                   f"\n\n\n" \
                   f"Found 1 result(s) for books with title 'Skyscraper': " \
                   f"\n\n" \
                   f"1. {book}" \
                   f"\n"
        self.assertEqual(expected, printed_actual)

    @patch('builtins.input', side_effect=['Ar'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_category_multiple_results_message(self, mock_output, mock_input):
        books_file = ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L',
                       'Shelf': '12', 'Category': 'Architecture', 'Subject': '20th Century'},
                      {'Author': 'Sinclair', 'Title': 'Morrisseau', 'Publisher': 'Editions Franco-Amerique',
                       'Shelf': 'Reading', 'Category': 'Art', 'Subject': 'Canadian'},
                      {'Author': 'Gore', 'Title': '2001 Household Hints & Dollar Stretchers',
                       'Publisher': 'Hanover House',
                       'Shelf': '9', 'Category': 'Home economics', 'Subject': 'History'})
        search_category(books_file, "Category")
        printed_actual = mock_output.getvalue()
        book_1 = {'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L',
                  'Shelf': '12', 'Category': 'Architecture', 'Subject': '20th Century'}
        book_2 = {'Author': 'Sinclair', 'Title': 'Morrisseau', 'Publisher': 'Editions Franco-Amerique',
                  'Shelf': 'Reading', 'Category': 'Art', 'Subject': 'Canadian'}
        expected = f"\n" \
                   f"Searching by Category..." \
                   f"\n\n\n" \
                   f"Found 2 result(s) for books with category 'Ar': " \
                   f"\n\n" \
                   f"1. {book_1}" \
                   f"\n"\
                   f"2. {book_2}" \
                   f"\n"
        self.assertEqual(expected, printed_actual)
