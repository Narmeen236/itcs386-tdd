import pytest
from leap import is_leap


# --- Step 0.1 ---
def test_2024_is_a_leap_year():
    assert is_leap(2024)


# --- Step 0.2 ---
def test_1900_is_not_a_leap_year():
    assert not is_leap(1900)


# --- Step 0.3 (One test, many inputs) ---
@pytest.mark.parametrize(
    "year, expected",
    [
        (2000, True),   # divisible by 400
        (1900, False),  # divisible by 100 but not by 400
        (2024, True),   # divisible by 4 but not by 100
        (2023, False),  # not divisible by 4
        (1600, True),   # divisible by 400 (add by me 1)
        (2021, False),  # not divisible by 4 (add by me 2)
    ],
)
def test_is_leap(year, expected):
    assert is_leap(year) == expected