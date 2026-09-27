"""Menu-driven entry point for Student Performance Analyzer."""

from analysis.analyzer import analyze_students
from services.student_service import StudentService
from utils.validation import ValidationError


def display_students(students) -> None:
    """Print student rows in a compact table."""
    if not students:
        print("No student records found.")
        return
    print(f"{'ID':<12} {'Name':<22} {'Python':>8} {'Math':>8} {'AI/ML':>8} {'Average':>9} {'Grade':>6}")
    print("-" * 78)
    for student in students:
        print(f"{student.student_id:<12} {student.name:<22} {student.python_marks:>8.1f} "
              f"{student.mathematics_marks:>8.1f} {student.aiml_marks:>8.1f} "
              f"{student.calculate_average():>9.2f} {student.calculate_grade():>6}")


def read_mark(subject: str):
    """Read a mark; let the service validate its numeric range."""
    return input(f"{subject} marks (0-100): ").strip()


def show_analysis(students) -> None:
    """Display the dataset summary returned by the analysis package."""
    summary = analyze_students(students)
    print(f"\nStudents: {summary['student_count']}")
    print(f"Overall average: {summary['overall_average']:.2f}")
    print(f"Pass (average >= 40): {summary['pass_count']} | Fail: {summary['fail_count']}")
    print("\nSubject statistics:")
    for subject, stats in summary["subjects"].items():
        print(f"  {subject}: average {stats['average']:.2f}, highest {stats['highest']:.1f}, "
              f"lowest {stats['lowest']:.1f}, std dev {stats['standard_deviation']:.2f}")
    print(f"Grade distribution: {summary['grade_distribution'] or 'No grades yet'}")


def main() -> None:
    """Run the application's interactive menu."""
    service = StudentService()
    actions = {
        "1": "Add a student", "2": "View all students", "3": "Search for a student",
        "4": "Update student information", "5": "Delete a student",
        "6": "Calculate individual student average", "7": "Calculate individual student grade",
        "8": "Overall dataset analysis", "9": "Exit",
    }
    while True:
        print("\n=== Student Performance Analyzer ===")
        for choice, label in actions.items():
            print(f"{choice}. {label}")
        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                student = service.add_student(
                    input("Student ID: "), input("Name: "), read_mark("Python"),
                    read_mark("Mathematics"), read_mark("AI/ML"),
                )
                print(f"Added {student.name} (grade {student.calculate_grade()}).")
            elif choice == "2":
                display_students(service.get_all_students())
            elif choice == "3":
                student = service.search_student(input("Student ID to search: "))
                display_students([student] if student else [])
            elif choice == "4":
                student_id = input("Student ID to update: ")
                current = service.search_student(student_id)
                if current is None:
                    print("Student not found.")
                    continue
                print("Press Enter to keep the current value.")
                name = input(f"Name [{current.name}]: ").strip() or None
                python_marks = read_mark("Python") or None
                mathematics_marks = read_mark("Mathematics") or None
                aiml_marks = read_mark("AI/ML") or None
                service.update_student(student_id, name=name, python_marks=python_marks,
                                       mathematics_marks=mathematics_marks, aiml_marks=aiml_marks)
                print("Student updated.")
            elif choice == "5":
                if service.delete_student(input("Student ID to delete: ")):
                    print("Student deleted.")
                else:
                    print("Student not found.")
            elif choice == "6":
                student = service.search_student(input("Student ID: "))
                if student is None:
                    print("Student not found.")
                else:
                    print(f"{student.name}: average {student.calculate_average():.2f}.")
            elif choice == "7":
                student = service.search_student(input("Student ID: "))
                if student is None:
                    print("Student not found.")
                else:
                    print(f"{student.name}: grade {student.calculate_grade()}.")
            elif choice == "8":
                show_analysis(service.get_all_students())
            elif choice == "9":
                print("Goodbye!")
                break
            else:
                print("Please choose a number from 1 to 9.")
        except (ValidationError, OSError) as error:
            print(f"Input or storage error: {error}")
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()
