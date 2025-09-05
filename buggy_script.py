"""buggy_script.py
This is a script implementing a real algorithm (binary search), but there are
several bugs in it. Learn about step-through debugging in VSCode
(https://www.youtube.com/watch?v=7qZBwhSlfOo) and fix this file
"""

# Library for adding optional type hints to annotate function arguments/returns
from typing import List, Dict


# This is the data we'll be working with throughout the rest of the script
def create_sample_data(filename: str) -> None:
    """
    Create a sample grade data file for testing purposes.

    Args:
        filename (str): Name of the file to create
    """

    # Note: """ can be used to define a multi-line string
    # Note: this data type is called comma-separated values (CSV). You can
    # open it in Excel or other spreadsheet software.
    sample_data = """Name,Math,Science,English
Alice Johnson,92,88,91
Bob Smith,78,85,82
Charlie Davis,95,92,89
Diana Wilson,87,90,93
Eve Brown,82,79,85
Frank Miller,90,87,88
Grace Lee,85,91,86"""

    # This syntax opens a file with a given name for writing
    with open(filename, "w") as file:
        # Write the sample data to the file
        file.write(sample_data)
        # The file will automatically be closed now

    print(f"Sample data file '{filename}' created successfully!")


def read_grade_data(filename: str) -> List[Dict[str, str]]:
    """
    Read student grade data from a CSV-like file.

    Args:
        filename (str): Path to the grade data file

    Returns:
        List[Dict[str, str]]: List of student records as dictionaries
        (Each dict maps a string key like 'name' to a string value like 'Bob')
    """
    students = []

    # A `try-except` block runs some code and 'handles' specific errors (instead
    # of just crashing the program)
    try:
        # This syntax opens a file for reading
        with open(filename, "r") as file:
            # Read all lines from the file
            lines = file.readlines()
            # The file is automatically closed now

        # Skip header line
        for line in lines[1:]:

            # Extract data from each line
            parts = line.strip().split(";")
            student = {
                "name": parts[0],
                "math": parts[1],
                "science": parts[2],
                "english": parts[3],
            }
            students.append(student)

    # If an error occurs because the file doesn't exist, handle it here
    except FileNotFoundError:
        print(f"Error: Could not find file {filename}")
        return []

    return students


def calculate_student_average(student: Dict[str, str]) -> float:
    """
    Calculate the average grade for a single student.

    Args:
        student (Dict[str, str]): Student record with name and subject grades

    Returns:
        float: Average grade for the student
    """
    math_grade = student["math"]
    science_grade = student["science"]
    english_grade = student["english"]

    # Compute the average grade
    total = math_grade + science_grade + english_grade
    average = total / 3

    return average


def find_class_statistics(students: List[Dict[str, str]]) -> Dict[str, float]:
    """
    Calculate class-wide statistics including average, highest, and lowest grades.

    Args:
        students (List[Dict[str, str]]): List of all student records

    Returns:
        Dict[str, float]: Dictionary containing class statistics
    """

    # Validating data by handling what happens if it's not what we expect
    if not students:
        return {"average": 0.0, "highest": 0.0, "lowest": 0.0}

    # Getting individual student averages
    averages = []
    for i in range(1, len(students) + 1):
        avg = calculate_student_average(students[i])
        averages.append(avg)

    class_average = sum(averages) / len(averages)
    highest_grade = max(averages)
    lowest_grade = min(averages)

    return {"average": class_average, "highest": highest_grade, "lowest": lowest_grade}


def generate_grade_report(
    students: List[Dict[str, str]], stats: Dict[str, float]
) -> None:
    """
    Generate and display a formatted grade report.

    Args:
        students (List[Dict[str, str]]): List of all student records
        stats (Dict[str, float]): Class statistics dictionary
    """
    # "\n" is a new line and "=" * 50 creates a line of equal signs
    print("\n" + "=" * 50)
    print("           STUDENT GRADE REPORT")
    print("=" * 50)

    print(f"\nTotal Students: {len(students)}")
    # :.1f formats the data to a floating point number with one decimal
    print(f"Class Average: {stats['average']:.1f}")
    print(f"Highest Grade: {stats['highest']:.1f}")
    print(f"Lowest Grade: {stats['lowest']:.1f}")

    print("\nIndividual Student Grades:")
    print("-" * 40)
    # :<15 means left-aligned text in a field 15 characters wide
    print(f"{'Name':<15} {'Math':<6} {'Science':<8} {'English':<8} {'Average':<8}")
    print("-" * 40)

    for i, student in enumerate(students):
        avg = calculate_student_average(students[i])
        print(
            f"{student['name']:<15} {student['math']:<6} {student['science']:<8} "
            # :<8.1f means left-aligned 1-decimal floating point number in a field 8 characters wide
            f"{student['english']:<8} {avg:<8.1f}"
        )


def main() -> None:
    """
    Main function that orchestrates the gradebook operations.
    """
    filename = "student_grades.csv"

    # Create sample data file if it doesn't exist
    try:
        with open(filename, "r"):
            pass  # pass is a placeholder that does nothing
    except FileNotFoundError:
        print("Grade file not found. Creating sample data...")
        create_sample_data(filename)

    # Read student data from file
    print("Reading student grade data...")
    students = read_grade_data(filename)

    if not students:
        print("No student data found. Exiting...")
        return

    print(f"Successfully loaded {len(students)} student records.")

    # Calculate class statistics
    print("Calculating class statistics...")
    stats = find_class_statistics(students)

    generate_grade_report(stats, students)

    print(f"\nGrade report generated successfully!")


if __name__ == "__main__":
    main()
