"""
COMP 1510
Assignment 2 Lab 4
Book collection manager
Jasper Zhou
A01235376
"""

import doctest


def get_info(file_name: str) -> tuple:
    """Convert .txt file contents into a tuple of dictionaries.

    Given Books.txt, convert each line in the file into a dictionary, where each spaced out piece of text in the
    first line is the key and the proceeding lines are the values for the key it lines up with. Each dictionary in
    the tuple represents each book specified in each line of the text file.

    :param:file_name: name of the text file (.txt) that exists in the same directory as this file.
    :precondtion: text file Books.txt must exist in the same directory as books.py and consist of at least three lines
    to generate a tuple of at least two dictionaries. Each item in each line is distinguished with a tab between text.
    :postcondition: always returns a tuple which only consists of dictionaries with the same keys.
    :return: tuple representing contents of the text file

    >>> get_info("Mock_Books_1.txt")
    ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L', 'Shelf': '12', 'Category': 'Architecture', \
'Subject': '20th Century'}, {'Author': 'Sinclair', 'Title': 'Morrisseau', 'Publisher': \
'Editions Franco-Amerique', 'Shelf': 'Reading', 'Category': 'Art', 'Subject': 'Canadian'})
    >>> get_info("Mock_Books_4.txt")
    ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': None, 'Shelf': '12', 'Category': 'Architecture', \
'Subject': '20th Century'}, {'Author': 'Sinclair', 'Title': 'Morrisseau', 'Publisher': None, 'Shelf': 'Reading', \
'Category': 'Art', 'Subject': 'Canadian'})
    """
    books_tuple = []
    categories = []

    with open(file_name, encoding='utf-16') as text_object:
        for line in text_object:
            line = line.strip('\t').strip('\n').split('\t')
            if categories:  # all other lines become values with the same keys
                book_dict = {category: line[categories.index(category)] for category in categories}
                for key, value in book_dict.items():
                    if value == '':
                        book_dict[key] = None
                books_tuple.append(book_dict)
            else:  # first line of file becomes the keys in the dict
                categories = [category for category in line]
    return tuple(books_tuple)


def search_category(books_file: tuple, category: str) -> tuple:
    """Search through tuple and find all dictionaries with user keyword input and print results with keyword.

    Helper function for all options in menu() except quit. Given books_file, checks for specified key in all
    dictionaries that contain user keyword input. Prints number of results and all dictionaries with the matching
    user input.

    :param:books_list: tuple of dictionaries containing all books.
    :param:category: string specified in the menu that determines which category (key) to search by.
    :postcondition: always prints a message with all the dictionaries that contain the user input keyword.
    :return: tuple of all dictionaries with matching user input keyword.

    doctests inapplicable (see test_search_category.py)
    """
    results = 0
    filtered_books_file = []

    print(f"\nSearching by {category}...\n")
    keyword = input(f"Enter *case-sensitive* keyword to search in all book {category.lower()}s: ")

    for book in books_file:
        if (keyword.capitalize() == "None") and (book[category] is None):
            results += 1
            filtered_books_file.append(book)
        elif (keyword in book[category]) or (keyword.capitalize() in book[category]):
            results += 1
            filtered_books_file.append(book)

    print(f"\nFound {results} result(s) for books with {category.lower()} '{keyword}': \n")
    for result in filtered_books_file:
        print(f"{filtered_books_file.index(result) + 1}. {result}")

    return tuple(filtered_books_file)


def select_new_shelf(books_list: tuple) -> str or None:
    """Prompt and return a shelf value from the existing shelf values.

    Helper function for change_shelf(). Prints all existing unique shelf values in books_list and prompts user to select
    one from the ordered list. The selected value is then returned to be used for change_shelf().

    :param:books_list: existing books_list tuple of dictionaries, to be extracted of its key values.
    :precondition: books_list must have dictionaries with key 'shelf' and values for user to view and select an option.
    :postcondition: if user has failed to select an option, return nothing and returns user to menu().
    :return: string of the key value.

    doctests inapplicable (see test_new_shelf.py)
    """
    shelf_list = []
    print("\nSelect a new shelf location for the selected book:")
    for book in books_list:  # generate list of all unique shelf values
        if book['Shelf'] not in shelf_list:
            shelf_list.append(book['Shelf'])

    shelf_list.sort()
    for shelf in shelf_list:  # print ordered list of all shelf values
        print(f"{shelf_list.index(shelf) + 1}. {shelf}")

    try:
        choice = int(input("\nOption:")) - 1
        if 0 <= choice:
            return shelf_list[choice]
    except (IndexError, ValueError):
        return


def change_shelf(books_list: tuple, select_books_list: tuple) -> tuple:
    """Change a given dictionary key 'Shelf' value in the books_list tuple to a new value.

    Helper function of menu() and follower function after search_category(). Given a filtered tuple with the user search
    results, prompt user for a specific book and the new shelf they want to relocate it to. Function then updates and
    returns books_list with the modified key values.

    :param:books_list: existing books_list tuple of dictionaries, to be modified and returns.
    :param:searched_list: tuple of dictionaries will only the dictionaries that match the user input criteia items
    :precondition: select_books_list must only consist of items from books_list.
    :postcondition: returned tuple will be the updated books_list, but will return the same tuple if user fails to enter
    input correctly.
    :return: updated books_list
    """
    try:
        choice = int(input("\nSelect a book by entering a number to rearrange its shelf location:")) - 1
    except (IndexError, ValueError):
        print("Invalid option: number outside range of possible choice. Please enter a valid number choice.")
        return books_list

    if 0 <= choice < len(select_books_list):
        select_book = select_books_list[choice]  # obtain one dictionary from books_list
        new_shelf = select_new_shelf(books_list)  # helper function obtains a new shelf value
        if new_shelf:  # user has selected a book
            print(f"\nSelected '{select_book['Title']}' to rearrange its shelf location..\nCurrent book: {select_book}")
            for book in books_list:
                if select_books_list[choice] == book:
                    book['Shelf'] = new_shelf
                    print(f"Updated book: {book}")
                    return books_list

    # user has failed to select a book at this point
    print("Invalid option: Please enter a valid number choice.")
    return books_list


def got_options(books_file: tuple, move_shelf_option: bool, quit_option: bool) -> tuple:
    """Menu printer and selector.

    Print all possible options for the user to the screen based on books_file contents. Then asks for a user option
    by prompting a number input. Helper function for menu().

    :param:books_file: tuple of dictionaries containing all books, which prints a menu based on its contents.
    :param:move_shelf_option: boolean that specifies whether to print and give the "move a book" option.
    :param:quit_option: boolean that specifies whether to print and give the "quit" option.
    :precondition: parameter conditions must all be met to correctly run the function.
    :postcondition: user must successfully enter a correct input choice to return a tuple, or else function fails and
    returns a tuple with values indicating other functions to pass.
    :return: tuple containing 2 items: (index number of the option, string of option), to be verified in menu().

    doctests inapplicable (see test_got_options.py)
    """
    options = []

    if (not move_shelf_option) and (not quit_option):
        print("\nSearching for a book to rearrange its shelf location...\n")
    print("Select an option by entering a number:")
    for index, category in enumerate(books_file[0]):
        print(f"{index + 1}. Search for books by: {category}")
        options.append(category)
    if move_shelf_option:
        print(f"{len(books_file[0]) + 1}. Move a book from one shelf to another shelf")
        options.append("Move a book from one shelf to another shelf")
    if quit_option:
        print(f"{len(books_file[0]) + 2}. Quit")
        options.append("Quit")

    try:
        choice = int(input("\nOption: ")) - 1
        return choice, options[choice]
    except (IndexError, ValueError):
        print("Invalid option: Please enter a valid number choice.")
        return -1, ""


def menu(books_file: tuple) -> tuple:
    """Loop main body of the books function until user prompts to end the while loop.

    User is given a list of choices to make (search a category, move book to another shelf, quit) until they choose
    to quit and terminate this function. Choices are generated based on the keys in books_list.

    :param:books_file: tuple of dictionaries containing all books, to be modified of its contents.
    :precondition: dictionary must have at least 1 key to have options in the menu (other than quit).
    :postcondition: function will end when user specifies to quit and exit this function.
    :return: same books_file tuple or tuple with modified values in the dictionaries.
    """
    while True:
        print("\n////////////////////////\n|  BOOKS.PY MAIN MENU  |\n////////////////////////\n")

        option = got_options(books_file, True, True)  # print all menu options and select a choice

        if 0 <= option[0] < len(books_file[0]):  # search for books by 'category':
            search_category(books_file, option[1])

        elif option[0] == len(books_file[0]):  # move a book from one shelf to another shelf
            option = got_options(books_file, False, False)
            if 0 <= option[0] < len(books_file[0]):
                select_books_file = search_category(books_file, option[1])
                if select_books_file:  # if the user has successfully searched for a tuple of books
                    books_file = change_shelf(books_file, select_books_file)

        elif option[0] == (len(books_file[0]) + 1):  # quit menu
            return books_file

        print("\nNow returning to main menu...\n")
        continue


def quit_books(books_file: tuple, book_file: str) -> None:
    """Dump all the data into a plaintext file.

    Before ending the program, converts the tuple of dictionaries that represents a book list back into a plain text
    file unordered with each book in its own row, updating books.txt

    :books_file: final tuple of dictionaries to be converted of each dictionary into a line in Books.txt
    :book_file: string name of the .txt file that will store all the contents of books_file
    :precondtion: Books.txt must exist in the same directory as books.py and must run get_info() before this function.
    :postcondition: updates the file Books.txt
    """
    open(book_file, 'w').close()
    with open(book_file, 'w', encoding='utf-16') as file_object:
        string = ""
        for key in books_file[0]:
            string += f"{key}\t"
        string = string.rstrip()
        file_object.write(string)

        for book in books_file:
            file_object.write("\n")
            string = ""
            for key in book:
                string += f"{book[key]}\t"
            string = string.rstrip()
            file_object.write(string)

    return


def books() -> None:
    """Runs Books.py from start to finish. To be used in the main() function."""
    print("Initiating books.py...")
    books_file = get_info("Books.txt")
    final_books = menu(books_file)  # main loop of the program
    print("\nUpdating text file...")
    quit_books(final_books, "Books.txt")
    print("Terminating books.py...")
    print("\nThank you for using Books.py!")
    print("     (;-_-)/")


def main():
    """Execute the Program"""
    doctest.testmod()
    books()


if __name__ == "__main__":
    main()
