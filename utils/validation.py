"""Reusable input validation functions."""

import re


class ValidationError(ValueError):
    """Raised when user-provided student data is invalid."""


def validate_student_id(value: str) -> str:
    """Accept IDs containing letters, digits, hyphens, or underscores."""
    student_id = value.strip()
    if not student_id:
        raise ValidationError("Student ID cannot be empty.")
    if not re.fullmatch(r"[A-Za-z0-9_-]+", student_id):
        raise ValidationError("Student ID may contain only letters, numbers, '-' and '_'.")
    return student_id


def validate_name(value: str) -> str:
    """Require a name made of letters, spaces, apostrophes, or hyphens."""
    name = " ".join(value.split())
    if not name:
        raise ValidationError("Name cannot be empty.")
    if not re.fullmatch(r"[A-Za-z][A-Za-z '\u2019-]*", name):
        raise ValidationError("Name may contain letters, spaces, apostrophes, and hyphens.")
    return name


def validate_marks(value: object) -> float:
    """Convert a mark to a number and require a value from 0 through 100."""
    try:
        marks = float(value)
    except (TypeError, ValueError) as error:
        raise ValidationError("Marks must be a number.") from error
    if not 0 <= marks <= 100:
        raise ValidationError("Marks must be between 0 and 100.")
    return marks
