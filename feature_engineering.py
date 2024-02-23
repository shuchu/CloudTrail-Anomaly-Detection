# -*- coding: utf-8 -*-

from datetime import datetime


def fea_datetime(datetime_str: str) -> list[int]:
    """ Feature engineering. Transfer one date time to a vector.
    One week has seven days and 24 hours. It's a length 168 vector.

    Args:
        datetime_str: string format of datetime object.

    Returns:
        a one-hot vector embedding of the eventTime. 
    """
    fea = [0]*7*24
 
    dt = datetime.fromisoformat(datetime_str)

    weekday = dt.weekday()  #[0, 6]
    hour = dt.hour

    idx = weekday*24 + hour
    fea[idx] = 1

    return fea