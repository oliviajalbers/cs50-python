# Contact Book
#### Video Demo:  <https://youtu.be/nEko-8aTN_4>
#### Description:
Contact book is a python program that allows users to create a contact book of names and phone numbers similar to what you may keep in your phone.

There are 4 actions that the users can execute. These include adding a new contact, removing an existing contact, updating an existing contact, and exiting their contact book.

After starting the program, users are prompted to choose one of the 4 actions available. If they do not choose one of the 4 available options, they are given an 'invalid entry' message and prompted repeatedly until they choose a valid entry. The program will change all entries to lowercase and trim any spaces before or after the entry.

Adding a new contact:
The first available action is adding a new contact. When the user enters 'add', they are then prompted for the name and number of the contact they would like to add. The name and number is saved in a dictionary called person and then that dictionary is added to the list called contact_book. Then the contact book is sorted and then printed as a table for the user to see.

Removing an existing contact:
The next available action is removing an existing contact. When the user enters 'remove', they are then prompted for the name of the contact they would like to remove. The remove function then loops through the contact book until it finds the given name and then deletes that person's name and number from the contact book. Then the updated contact book is printed as a table for the user. If the name entered is not in the current contact book, then the user receives a message that says 'name not in contacts'.

Updating an existing contact:
Users are also able to update an existing contact in their contact book. When users enter 'update', they are then prompted for the current name of the contact they would like to update. Then they are able to enter the new name and new number for the contact they would like to update. The program then loops through the contact book until it finds the current name and then updates both the name and number for that contact. Finally, the contact book is re-sorted and then printed as a table for the user to see. If the name entered is not in the current contact book, then the user receives a message that says 'name not in contacts'.

Exiting the book:
The final available action is to exit the contact book. WHen the user enters 'exit', they end the program and are no longer prompted for the action they would like to do.


**Files**


**project.py** - This file contains the python code for the contact book program. It includes a main function as well as 4 other functions: add, remove, update, sort_book, and make_table.

**test_project.py** - This file contains tests for the add, remove, update, and sort_book functions.

**requirements.txt** - This file includes a list of required libraries.


