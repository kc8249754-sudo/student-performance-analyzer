"""Business operations for creating and managing students."""

from models.student import Student
from utils.file_handler import load_students, save_students
from utils.validation import ValidationError, validate_marks, validate_name, validate_student_id


class StudentService:
    """Manage student records and keep the JSON file in sync."""

    def __init__(self, file_path=None):
        self.file_path = file_path
        self.students: list[Student] = []
        self.refresh()

    def refresh(self) -> None:
        """Reload the records from persistent storage."""
        records = load_students(self.file_path) if self.file_path else load_students()
        self.students = [Student.from_dict(record) for record in records]

    def _save(self) -> None:
        records = [student.to_dict() for student in self.students]
        if self.file_path:
            save_students(records, self.file_path)
        else:
            save_students(records)

    def add_student(self, student_id: str, name: str, python_marks, mathematics_marks, aiml_marks) -> Student:
        """Validate and add a unique student record."""
        student_id = validate_student_id(student_id)
        if any(item.student_id.casefold() == student_id.casefold() for item in self.students):
            raise ValidationError(f"Student ID '{student_id}' already exists.")
        student = Student(
            student_id,
            validate_name(name),
            validate_marks(python_marks),
            validate_marks(mathematics_marks),
            validate_marks(aiml_marks),
        )
        self.students.append(student)
        self._save()
        return student

    def get_all_students(self) -> list[Student]:
        """Return a copy so callers cannot accidentally alter the internal list."""
        return self.students.copy()

    def search_student(self, student_id: str) -> Student | None:
        """Find a student by ID, ignoring letter case."""
        wanted_id = validate_student_id(student_id).casefold()
        return next((item for item in self.students if item.student_id.casefold() == wanted_id), None)

    def update_student(self, student_id: str, *, name=None, python_marks=None,
                       mathematics_marks=None, aiml_marks=None) -> Student:
        """Update supplied fields while leaving omitted fields unchanged."""
        student = self.search_student(student_id)
        if student is None:
            raise ValidationError(f"No student found with ID '{student_id}'.")
        if name is not None:
            student.name = validate_name(name)
        if python_marks is not None:
            student.python_marks = validate_marks(python_marks)
        if mathematics_marks is not None:
            student.mathematics_marks = validate_marks(mathematics_marks)
        if aiml_marks is not None:
            student.aiml_marks = validate_marks(aiml_marks)
        self._save()
        return student

    def delete_student(self, student_id: str) -> bool:
        """Delete a matching student; return False if the ID is not found."""
        student = self.search_student(student_id)
        if student is None:
            return False
        self.students.remove(student)
        self._save()
        return True
