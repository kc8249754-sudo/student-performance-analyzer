"""Student data model and performance calculations."""

from dataclasses import dataclass


@dataclass
class Student:
    """A student's identity and marks in the three project subjects."""

    student_id: str
    name: str
    python_marks: float
    mathematics_marks: float
    aiml_marks: float

    @property
    def marks(self) -> tuple[float, float, float]:
        """Return marks in a consistent subject order."""
        return (self.python_marks, self.mathematics_marks, self.aiml_marks)

    def calculate_average(self) -> float:
        """Return the mean of this student's three marks."""
        return sum(self.marks) / len(self.marks)

    def calculate_grade(self) -> str:
        """Return a grade based on the student's average."""
        average = self.calculate_average()
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        elif average >= 40:
            return "E"
        return "F"

    def to_dict(self) -> dict[str, str | float]:
        """Convert the object to a JSON-friendly dictionary."""
        return {
            "student_id": self.student_id,
            "name": self.name,
            "python_marks": self.python_marks,
            "mathematics_marks": self.mathematics_marks,
            "aiml_marks": self.aiml_marks,
        }

    @classmethod
    def from_dict(cls, record: dict) -> "Student":
        """Build a Student object from a stored record."""
        return cls(
            student_id=str(record["student_id"]),
            name=str(record["name"]),
            python_marks=float(record["python_marks"]),
            mathematics_marks=float(record["mathematics_marks"]),
            aiml_marks=float(record["aiml_marks"]),
        )
