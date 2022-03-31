""" Calculate commission """
from datetime import datetime

from loguru import logger


def get_commission(date: str) -> float:
    """ Get commission depending on the season

    Args:
        date (str): reference date

    Returns:
        float: commission percentage
    """
    try:
        date = datetime.strptime(date, "%Y-%m-%d").date()

    except ValueError:
        logger.error('The date format is incorrect!')
        raise

    date_month = date.month

    if 6 <= date_month <= 9:
        commission = 0.15

    else:
        commission = 0.1

    return commission
