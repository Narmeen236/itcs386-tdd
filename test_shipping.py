# test_shipping.py
import pytest
from shipping import shipping_fee


# Rule 1: weight must be more than 0 kg
def test_rule1_weight_greater_than_zero():
    with pytest.raises(ValueError, match="weight must be more than 0 kg"):
        shipping_fee(0)  # BUG 1: weight = 0 should raise ValueError


# Rule 2: up to 1 kg costs 40 baht
# Rule 3: more than 1 kg and up to 5 kg costs 60 baht
# Rule 4: more than 5 kg costs 60 + 10 for every started kg
@pytest.mark.parametrize(
    "weight, expected_fee",
    [
        (0.5, 40),  # inside Rule 2
        (1.0, 40),  # BUG 2: exactly 1 kg should be 40 baht (boundary)
        (2.0, 60),  # inside Rule 3
        (5.0, 60),  # edge of Rule 3
        (6.0, 70),  # exactly 6 kg (started 1 kg above 5)
        (5.2, 70),  # BUG 3: 5.2 kg is a started kg, must be 70 baht
    ],
)
def test_shipping_fee_rules(weight, expected_fee):
    assert shipping_fee(weight) == expected_fee