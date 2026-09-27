"""NumPy and Pandas summaries for the student dataset."""

import numpy as np
import pandas as pd

from models.student import Student

SUBJECT_COLUMNS = {
    "Python": "python_marks",
    "Mathematics": "mathematics_marks",
    "AI/ML": "aiml_marks",
}


def students_to_dataframe(students: list[Student]) -> pd.DataFrame:
    """Convert objects to a DataFrame with derived average and grade columns."""
    columns = ["student_id", "name", *SUBJECT_COLUMNS.values()]
    frame = pd.DataFrame([student.to_dict() for student in students], columns=columns)
    if not frame.empty:
        frame["average"] = frame[list(SUBJECT_COLUMNS.values())].mean(axis=1)
        frame["grade"] = frame["average"].apply(_grade_for_average)
    else:
        frame["average"] = pd.Series(dtype=float)
        frame["grade"] = pd.Series(dtype=str)
    return frame


def _grade_for_average(average: float) -> str:
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


def analyze_students(students: list[Student]) -> dict:
    """Calculate class counts and subject/overall performance statistics."""
    frame = students_to_dataframe(students)
    subject_stats = {}
    for subject, column in SUBJECT_COLUMNS.items():
        values = frame[column].to_numpy(dtype=float) if not frame.empty else np.array([], dtype=float)
        subject_stats[subject] = {
            "average": float(np.mean(values)) if values.size else 0.0,
            "highest": float(np.max(values)) if values.size else 0.0,
            "lowest": float(np.min(values)) if values.size else 0.0,
            "standard_deviation": float(np.std(values)) if values.size else 0.0,
        }
    averages = frame["average"].to_numpy(dtype=float)
    passed = int((averages >= 40).sum())
    return {
        "student_count": len(frame),
        "subjects": subject_stats,
        "overall_average": float(np.mean(averages)) if averages.size else 0.0,
        "pass_count": passed,
        "fail_count": len(frame) - passed,
        "grade_distribution": frame["grade"].value_counts().to_dict(),
    }
