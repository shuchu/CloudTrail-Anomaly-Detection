# -*- coding: utf-8 -*-

import json
import csv
import pandas as pd
from datetime import datetime


from utils import extract_fea
from feature_engineering import fea_datetime


data_fpath = "result-userIdentity.arn-root-dump.json"

data = []

with open(data_fpath, 'r') as f:
    data = json.load(f)

features = ["eventID", "eventTime"]

fea_raw = extract_fea(features, data)
fea_raw_sorted = [[k, datetime.fromisoformat(v)] for k, v in fea_raw]
fea_raw_sorted = sorted(fea_raw_sorted, key=lambda x: x[1], reverse=True,)

with open("fea_raw.csv", 'w') as f:
    mywriter = csv.writer(f)
    mywriter.writerows(fea_raw_sorted)

fea = [ [id] + fea_datetime(str(dt)) for id, dt in fea_raw]

with open("fea.csv", 'w') as f:
    mywriter = csv.writer(f)
    mywriter.writerows(fea)