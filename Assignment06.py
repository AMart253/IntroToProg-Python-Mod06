# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Python 3.12.1
# Change Log: (Who, When, What)
#   Alan Martin, 02/16/2024, Created Script from starter
#   Alan Martin, 02/18/2024, Tidied up code
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
menu_choice: str = " "  # Hold the choice made by the user.
students: list = []  # a table of student data


class FileProcessor:
    """
    Processing layer functions designed to interact with JSON files.

    Alan Martin, 02/16/2024, created class FileProcessor
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        A FileProcessing function designed to read JSON files into program.

        Alan Martin, 02/16/2024, created method read_data_from_file
        """
        file = " "
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There Was A Non-Specific Error!", e)
        finally:
            if not file.closed:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        A FileProcessing function designed write program data into JSON files.

        Alan Martin, 02/16/2024, created method write_data_from_file
        """
        file = " "
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
            print("\n-----Your Data has been saved-----\n")
        except Exception as e:
            IO.output_error_messages("Error: There was a problem with writing to the file", e)
        finally:
            if not file.closed:
                file.close()


class IO:
    """
    A collection of presentation layer functions that manage user input and output

    Alan Martin, 02/16/2024, Created IO Class
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        This function displays custom error messages to user

        Alan Martin, 02/16/2024, Created output_error_messages function
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """
        This function displays our constant MENU

        Alan Martin, 02/16/2024, Created output_menu function
        """
        print(menu)

    @staticmethod
    def input_menu_choice():
        """
        This function gets user input for the MENU of choices

        Alan Martin, 02/16/2024, Created input_menu_choice function
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages("Error: There was a Non-Specific Error", e)
        return choice

    @staticmethod
    def input_student_data(student_data):
        """
        This function that takes student first name, last name, and course

        Alan Martin, 02/16/2024, Created input_student_data function
        """
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student = {"FirstName": student_first_name,
                       "LastName": student_last_name,
                       "CourseName": course_name}
            student_data.append(student)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages("Error: There was a Value Error", e)
        except Exception as e:
            IO.output_error_messages("Error: There was a problem with your entered data.", e)
        return student_data

    @staticmethod
    def output_student_courses(student_data: list):
        """
        This function displays student first name, last name, and course in list

        Alan Martin, 02/16/2024, Created output_student_data function
        """
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

# End of Classes and their Methods

# Read the file data into a list of lists (table)


students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)


# Start the loop
while True:

    # Present the MENU
    IO.output_menu(menu=MENU)

    # Take user menu choice
    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(student_data=students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break

print("Program Ended")
