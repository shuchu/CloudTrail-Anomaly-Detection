# -*- coding: utf-8 -*-

from datetime import datetime
import numpy as np



class UserActivityAD:

    def __init_(self,):
        pass

    def train(self, data: list[str]) -> None:
        pass

    def predict(self, datum: str) -> bool:
        pass

    def fea_eng(self, datum: list[str]) -> list[int]:
        """ Feature engineering. Transfer one date time to a vector.
        One week has seven days and 24 hours. It's a length 168 vector.

        Args:
            datum: has content [eventID, eventTime].

        Returns:
            a one-hot vector embedding of the eventTime. 
        """
        fea = [0]*7*24

        event_time = datum[1]  
        dt = datetime.fromisoformat(event_time)

        weekday = dt.weekday  #[0, 6]
        hour = dt.hour

        idx = weekday*24 + hour
        fea[idx] = 1

        return fea

    def save(self, fpath: str) -> None:
        pass

    def load(self, fpath: str) -> None:
        pass