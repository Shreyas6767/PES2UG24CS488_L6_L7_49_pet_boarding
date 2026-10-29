import pytest
from pet_boarding import boarding_fee, admission_ok, checkout_status

# Example test cases:
def test_within_included_days():
    assert boarding_fee("dog", 1, False) == 0

def test_admission_ok():
    assert admission_ok(4, 2, False) is True

# Write the rest of the test cases so that the code is 90-100% covered.

def test_invalid_pet():
    with pytest.raises(ValueError):
        boarding_fee("bird", 5, False)


def test_negative_days():
    with pytest.raises(ValueError):
        boarding_fee("cat", -1, False)


def test_premium_cat():
    assert boarding_fee("cat", 5, True) == 20


def test_dog_extra_days():
    assert boarding_fee("dog", 5, False) == 90


def test_long_dog_stay():
    assert boarding_fee("dog", 15, False) == 585


def test_long_cat_stay():
    assert boarding_fee("cat", 15, False) == 360


def test_senior_admission():
    assert admission_ok(10, 3, True) is True


def test_young_pet():
    assert admission_ok(0, 3, False) is False


def test_long_stay_checkout():
    assert checkout_status(35, True, False) == "open"


def test_weekend_checkout():
    assert checkout_status(20, False, True) == "late"


def test_closed_checkout():
    assert checkout_status(-1, False, False) == "closed"

