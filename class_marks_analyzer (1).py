import numpy as np

def get_marks():
    marks = []
    for value in input("Enter marks separated by spaces: ").split():
        try:
            marks.append(float(value))
        except ValueError:
            print(f"Invalid marks '{value}'. Enter numbers only.")
            return None

    if not marks:
        print("Enter at least one mark.")
        return None
    if any(mark < 0 or mark > 100 for mark in marks):
        print("Marks must be between 0 and 100.")
        return None
    return np.array(marks)


def analyze_marks(marks):
    average = np.mean(marks)
    passed = np.sum(marks >= 40)

    print(f"Mean: {average:.2f} | Median: {np.median(marks):.2f}")
    print(f"Max: {np.max(marks):g} | Min: {np.min(marks):g} | Std Dev: {np.std(marks):.2f}")
    print(f"Passed: {passed} of {len(marks)}")
    if passed < len(marks):
        print(f"Failed: {len(marks) - passed} | Pass percentage: {passed / len(marks) * 100:.2f}%")
        print(f"Above average: {np.sum(marks > average)} students")


marks = get_marks()
if marks is not None:
    analyze_marks(marks)
