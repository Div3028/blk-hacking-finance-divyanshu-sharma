# Test Type: Unit Test
# Validation: round up logic
# Run: pytest

from app.utils import round_up_100

def test_round():
    ceiling, rem = round_up_100(1519)
    assert ceiling == 1600
    assert rem == 81