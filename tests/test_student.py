"""Unit tests for student models, validation, and service behavior."""

import json
import tempfile
import unittest
from pathlib import Path

from models.student import Student
from services.student_service import StudentService
from utils.validation import ValidationError, validate_marks


class StudentTests(unittest.TestCase):
    def test_student_creation_and_dictionary(self):
        student = Student("S1", "Ada Lovelace", 90, 80, 70)
        self.assertEqual(student.to_dict()["name"], "Ada Lovelace")

    def test_average(self):
        self.assertAlmostEqual(Student("S1", "Ada", 90, 80, 70).calculate_average(), 80)

    def test_grade(self):
        self.assertEqual(Student("S1", "Ada", 90, 90, 90).calculate_grade(), "A")
        self.assertEqual(Student("S2", "Grace", 20, 30, 40).calculate_grade(), "F")

    def test_mark_validation(self):
        self.assertEqual(validate_marks("72.5"), 72.5)

    def test_invalid_marks(self):
        for value in ("abc", -1, 101):
            with self.subTest(value=value), self.assertRaises(ValidationError):
                validate_marks(value)

    def test_duplicate_id_is_rejected_and_records_persist(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "students.json"
            service = StudentService(path)
            service.add_student("S1", "Ada", 90, 80, 70)
            with self.assertRaises(ValidationError):
                service.add_student("s1", "Grace", 90, 80, 70)
            reloaded = StudentService(path)
            self.assertEqual(len(reloaded.get_all_students()), 1)
            self.assertEqual(json.loads(path.read_text(encoding="utf-8"))[0]["student_id"], "S1")

    def test_update_search_delete(self):
        with tempfile.TemporaryDirectory() as directory:
            service = StudentService(Path(directory) / "students.json")
            service.add_student("S1", "Ada", 90, 80, 70)
            updated = service.update_student("S1", name="Ada Lovelace", aiml_marks=95)
            self.assertEqual(updated.aiml_marks, 95)
            self.assertEqual(service.search_student("s1").name, "Ada Lovelace")
            self.assertTrue(service.delete_student("S1"))
            self.assertFalse(service.delete_student("S1"))


if __name__ == "__main__":
    unittest.main()
