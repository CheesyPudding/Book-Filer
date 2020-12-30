from unittest import TestCase
from books import quit_books


class Test(TestCase):
    def test_quit_books_minimum_2_line_file(self):
        books_file = ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L',
                       'Shelf': '12', 'Category': 'Architecture', 'Subject': '20th Century'},
                      {'Author': 'Sinclair', 'Title': 'Morrisseau', 'Publisher': 'Editions Franco-Amerique',
                       'Shelf': 'Reading', 'Category': 'Art', 'Subject': 'Canadian'})
        open("Mock_Books_Tester.txt", 'w').close()
        quit_books(books_file, "Mock_Books_Tester.txt")
        actual_file = open("Mock_Books_Tester.txt", 'r', encoding='utf-16')
        actual = actual_file.read()
        expected_file = open("Mock_Books_1.txt", 'r', encoding='utf-16')
        expected = expected_file.read()
        self.assertEqual(expected, actual)

    def test_quit_books_5_line_file(self):
        books_file = ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L',
                       'Shelf': '12', 'Category': 'Architecture', 'Subject': '20th Century'},
                      {'Author': 'Sinclair', 'Title': 'Morrisseau', 'Publisher': 'Editions Franco-Amerique',
                       'Shelf': 'Reading', 'Category': 'Art', 'Subject': 'Canadian'},
                      {'Author': 'Sawyer', 'Title': 'The Terminal Experiment', 'Publisher': 'Harper Prism',
                       'Shelf': '10', 'Category': 'Fiction', 'Subject': 'SF'},
                      {'Author': 'Silverberg', 'Title': "At Winter's End", 'Publisher': 'Warner Books',
                       'Shelf': '18', 'Category': 'Fiction', 'Subject': 'SF'})
        open("Mock_Books_Tester.txt", 'w').close()
        quit_books(books_file, "Mock_Books_Tester.txt")
        actual_file = open("Mock_Books_Tester.txt", 'r', encoding='utf-16')
        actual = actual_file.read()
        expected_file = open("Mock_Books_5.txt", 'r', encoding='utf-16')
        expected = expected_file.read()
        self.assertEqual(expected, actual)
