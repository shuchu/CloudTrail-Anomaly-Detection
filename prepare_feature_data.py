# -*- coding: utf-8 -*-

import json
import csv

from utils import extract_fea


data_fpath = "result-userIdentity.arn-root-dump.json"

data = []

with open(data_fpath, 'r') as f:
    data = json.load(f)

features = ["eventID", "eventTime"]

fea = extract_fea(features, data)

with open("fea.csv", 'w') as f:
    mywriter = csv.writer(f)
    mywriter.writerows(fea)