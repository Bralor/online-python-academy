import os
import pytest

EXPECTED_LESSONS = [
    "lesson01",
    "lesson02",
    "lesson03",
    "lesson04",
    "lesson05",
    "lesson06",
    "lesson07",
    "lesson08",
    "lesson09",
    "lesson10",
    "lesson11",
]


@pytest.mark.parametrize("exp_lessons", EXPECTED_LESSONS)
def test_number_of_lessons(exp_lessons):
    current_list = [lesson for lesson in os.listdir() if "lesson" in lesson]
    assert exp_lessons in current_list


@pytest.mark.parametrize("exp_lessons", EXPECTED_LESSONS)
def test_content_of_lesson_dirs(exp_lessons):
    assert len(os.listdir(exp_lessons)) != 0
