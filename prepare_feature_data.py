# -*- coding: utf-8 -*-

import json
import csv
import pandas as pd


from utils import extract_fea
from feature_engineering import fea_datetime


data_fpath = "result-userIdentity.arn-root-dump.json"

data = []

with open(data_fpath, 'r') as f:
    data = json.load(f)

features = ["eventID", "eventTime"]

fea_raw = extract_fea(features, data)

with open("fea_raw.csv", 'w') as f:
    mywriter = csv.writer(f)
    mywriter.writerows(fea_raw)


fea = [ [id] + fea_datetime(dt) for id, dt in fea_raw]

with open("fea.csv", 'w') as f:
    mywriter = csv.writer(f)
    mywriter.writerows(fea)