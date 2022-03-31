""" Test commission calculate """
import sys

sys.path.append('./')
from commission import get_commission
import pytest


def test_commission():
    high_season_date = '2021-03-21'
    low_season_date = '2021-07-12'

    assert get_commission(high_season_date) == 0.10
    assert get_commission(low_season_date) == 0.15

def test_format_date():
    date = '2021/03/21'

    with pytest.raises(ValueError):
        get_commission(date)
