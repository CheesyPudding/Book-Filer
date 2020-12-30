from unittest import TestCase
import io
from unittest.mock import patch
from books import got_options


class Test(TestCase):
    @patch('builtins.input', side_effect=['0'])
    def test_got_options_invalid_choice_out_of_range_return(self, mock_input):
        books_file = ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L',
                       'Shelf': '12', 'Category': 'Architecture', 'Subject': '20th Century'},
                      {'Author': 'Sinclair', 'Title': 'Morrisseau', 'Publisher': 'Editions Franco-Amerique',
                       'Shelf': 'Reading', 'Category': 'Art', 'Subject': 'Canadian'},
                      {'Author': 'Gore', 'Title': '2001 Household Hints & Dollar Stretchers',
                       'Publisher': 'Hanover House',
                       'Shelf': '9', 'Category': 'Home economics', 'Subject': 'History'})
        actual = got_options(books_file, True, True)
        expected = (-1, "")
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['1'])
    def test_got_options_valid_input_choice_return(self, mock_input):
        books_file = ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L',
                       'Shelf': '12', 'Category': 'Architecture', 'Subject': '20th Century'},
                      {'Author': 'Sinclair', 'Title': 'Morrisseau', 'Publisher': 'Editions Franco-Amerique',
                       'Shelf': 'Reading', 'Category': 'Art', 'Subject': 'Canadian'},
                      {'Author': 'Gore', 'Title': '2001 Household Hints & Dollar Stretchers',
                       'Publisher': 'Hanover House',
                       'Shelf': '9', 'Category': 'Home economics', 'Subject': 'History'})
        actual = got_options(books_file, True, True)
        expected = (0, "Author")
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['9'])
    def test_got_options_invalid_choice_out_of_range_return(self, mock_input):
        books_file = ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L',
                       'Shelf': '12', 'Category': 'Architecture', 'Subject': '20th Century'},
                      {'Author': 'Sinclair', 'Title': 'Morrisseau', 'Publisher': 'Editions Franco-Amerique',
                       'Shelf': 'Reading', 'Category': 'Art', 'Subject': 'Canadian'},
                      {'Author': 'Gore', 'Title': '2001 Household Hints & Dollar Stretchers',
                       'Publisher': 'Hanover House',
                       'Shelf': '9', 'Category': 'Home economics', 'Subject': 'History'})
        actual = got_options(books_file, True, True)
        expected = (-1, "")
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['6'])
    def test_got_options_valid_input_no_move_or_quit_return(self, mock_input):
        books_file = ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L',
                       'Shelf': '12', 'Category': 'Architecture', 'Subject': '20th Century'},
                      {'Author': 'Sinclair', 'Title': 'Morrisseau', 'Publisher': 'Editions Franco-Amerique',
                       'Shelf': 'Reading', 'Category': 'Art', 'Subject': 'Canadian'},
                      {'Author': 'Gore', 'Title': '2001 Household Hints & Dollar Stretchers',
                       'Publisher': 'Hanover House',
                       'Shelf': '9', 'Category': 'Home economics', 'Subject': 'History'})
        actual = got_options(books_file, False, False)
        expected = (5, "Subject")
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['7'])
    def test_got_options_invalid_input_no_move_or_quit_return(self, mock_input):
        books_file = ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L',
                       'Shelf': '12', 'Category': 'Architecture', 'Subject': '20th Century'},
                      {'Author': 'Sinclair', 'Title': 'Morrisseau', 'Publisher': 'Editions Franco-Amerique',
                       'Shelf': 'Reading', 'Category': 'Art', 'Subject': 'Canadian'},
                      {'Author': 'Gore', 'Title': '2001 Household Hints & Dollar Stretchers',
                       'Publisher': 'Hanover House',
                       'Shelf': '9', 'Category': 'Home economics', 'Subject': 'History'})
        actual = got_options(books_file, False, False)
        expected = (-1, "")
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_got_options_valid_input_choice_print(self, mock_output, mock_input):
        books_file = ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L',
                       'Shelf': '12', 'Category': 'Architecture', 'Subject': '20th Century'},
                      {'Author': 'Sinclair', 'Title': 'Morrisseau', 'Publisher': 'Editions Franco-Amerique',
                       'Shelf': 'Reading', 'Category': 'Art', 'Subject': 'Canadian'},
                      {'Author': 'Gore', 'Title': '2001 Household Hints & Dollar Stretchers',
                       'Publisher': 'Hanover House',
                       'Shelf': '9', 'Category': 'Home economics', 'Subject': 'History'})
        got_options(books_file, True, True)
        printed_actual = mock_output.getvalue()
        string = "Select an option by entering a number:\n"
        expected = f"{string}" \
                   f"1. Search for books by: Author\n" \
                   f"2. Search for books by: Title\n" \
                   f"3. Search for books by: Publisher\n" \
                   f"4. Search for books by: Shelf\n" \
                   f"5. Search for books by: Category\n" \
                   f"6. Search for books by: Subject\n" \
                   f"7. Move a book from one shelf to another shelf\n" \
                   f"8. Quit\n"
        self.assertEqual(expected, printed_actual)

    @patch('builtins.input', side_effect=['6'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_got_options_valid_input_no_move_or_quit_print(self, mock_output, mock_input):
        books_file = ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L',
                       'Shelf': '12', 'Category': 'Architecture', 'Subject': '20th Century'},
                      {'Author': 'Sinclair', 'Title': 'Morrisseau', 'Publisher': 'Editions Franco-Amerique',
                       'Shelf': 'Reading', 'Category': 'Art', 'Subject': 'Canadian'},
                      {'Author': 'Gore', 'Title': '2001 Household Hints & Dollar Stretchers',
                       'Publisher': 'Hanover House',
                       'Shelf': '9', 'Category': 'Home economics', 'Subject': 'History'})
        got_options(books_file, False, False)
        printed_actual = mock_output.getvalue()
        string = "Select an option by entering a number:\n"
        expected = f"\nSearching for a book to rearrange its shelf location...\n\n" \
                   f"{string}" \
                   f"1. Search for books by: Author\n" \
                   f"2. Search for books by: Title\n" \
                   f"3. Search for books by: Publisher\n" \
                   f"4. Search for books by: Shelf\n" \
                   f"5. Search for books by: Category\n" \
                   f"6. Search for books by: Subject\n"
        self.assertEqual(expected, printed_actual)

    @patch('builtins.input', side_effect=['8'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_got_options_valid_input_choice_to_quit_print(self, mock_output, mock_input):
        books_file = ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L',
                       'Shelf': '12', 'Category': 'Architecture', 'Subject': '20th Century'},
                      {'Author': 'Sinclair', 'Title': 'Morrisseau', 'Publisher': 'Editions Franco-Amerique',
                       'Shelf': 'Reading', 'Category': 'Art', 'Subject': 'Canadian'},
                      {'Author': 'Gore', 'Title': '2001 Household Hints & Dollar Stretchers',
                       'Publisher': 'Hanover House',
                       'Shelf': '9', 'Category': 'Home economics', 'Subject': 'History'})
        got_options(books_file, True, True)
        printed_actual = mock_output.getvalue()
        string = "Select an option by entering a number:\n"
        expected = f"{string}" \
                   f"1. Search for books by: Author\n" \
                   f"2. Search for books by: Title\n" \
                   f"3. Search for books by: Publisher\n" \
                   f"4. Search for books by: Shelf\n" \
                   f"5. Search for books by: Category\n" \
                   f"6. Search for books by: Subject\n" \
                   f"7. Move a book from one shelf to another shelf\n" \
                   f"8. Quit\n"
        self.assertEqual(expected, printed_actual)

    @patch('builtins.input', side_effect=['9'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_got_options_invalid_choice_out_of_range_print(self, mock_output, mock_input):
        books_file = ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L',
                       'Shelf': '12', 'Category': 'Architecture', 'Subject': '20th Century'},
                      {'Author': 'Sinclair', 'Title': 'Morrisseau', 'Publisher': 'Editions Franco-Amerique',
                       'Shelf': 'Reading', 'Category': 'Art', 'Subject': 'Canadian'},
                      {'Author': 'Gore', 'Title': '2001 Household Hints & Dollar Stretchers',
                       'Publisher': 'Hanover House',
                       'Shelf': '9', 'Category': 'Home economics', 'Subject': 'History'})
        got_options(books_file, True, True)
        printed_actual = mock_output.getvalue()
        string = "Select an option by entering a number:\n"
        expected = f"{string}" \
                   f"1. Search for books by: Author\n" \
                   f"2. Search for books by: Title\n" \
                   f"3. Search for books by: Publisher\n" \
                   f"4. Search for books by: Shelf\n" \
                   f"5. Search for books by: Category\n" \
                   f"6. Search for books by: Subject\n" \
                   f"7. Move a book from one shelf to another shelf\n" \
                   f"8. Quit\n" \
                   f"Invalid option: Please enter a valid number choice.\n"
        self.assertEqual(expected, printed_actual)
