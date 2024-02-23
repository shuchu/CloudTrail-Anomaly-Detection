# -*- coding: utf-8 -*-

from sklearn.ensemble import IsolationForest
import numpy as np



class UserActivityAD:

    def __init__(self,):
        self._model = IsolationForest(n_estimators=10)

    def train(self, data: np.ndarray) -> None:
        self._model.fit(data)

    def predict(self, datum: np.ndarray) -> list:
        pred = self._model.predict(datum)
        score = self._model.score_samples(datum)

        return [pred, score]

    def save(self, fpath: str) -> None:
        pass

    def load(self, fpath: str) -> None:
        pass

