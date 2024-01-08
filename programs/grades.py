import sys

if __name__ == '__main__':
    # Conversion of Norwegian grades to numerical values for calculation
    # Norwegian grading scale: A=5, B=4, C=3, D=2, E=1, F=0 (F is fail and not considered in average)

    grades = {
        'A': 5,
        'B': 4,
        'C': 3,
        'D': 2,
        'E': 1
    }

    # List of grades provided
    grade_list = ['B', 'A', 'D', 'A', 'E', 'C', 'A', 'E', 'C', 'C', 'B', 'C']

    # Calculating the numerical average
    average_grade = sum(grades[grade] for grade in grade_list) / len(grade_list)

    # Output the average grade
    print("The average grade is:", average_grade)
    # The average grade is: 3.25

    sys.exit()

