#-*- coding: utf-8 -*-


import click
from typing import Any
import os
import glob
import json
import random

from iam_analyzer import CTAnalyzer


@click.group()
def cli():
    pass


def _get_flatten_field_value_from_json(field:str, obj: dict) -> Any:
    fields = field.strip().split('.')
    myobj = obj
    for f in fields:
        if f in myobj:
            myobj = myobj[f]

    return myobj


@click.command(help="Count how many unique values of a specific field in the data.")
@click.argument("target")
@click.argument("directory", type=click.Path(exists=True))
def count(target, directory):
    click.echo(target)
    ct_analyzer = CTAnalyzer()

    try:
        for fname in glob.glob(os.path.join(directory, "*.json")):
            print(f"processing file: {fname}")
            with open(fname, 'r') as f:
                if target == "iam_user":
                    d = json.load(f)
                    ct_analyzer.count_iam_users(d["Records"])
                else:
                    continue
    except Exception as e:
        raise e
    
    with open(f"result-{target}.json", 'w') as f:
        json.dump(ct_analyzer.iam_users, f, indent=2)


@click.command(help="Dump records that match requirements.")
@click.argument("field")
@click.argument("value")
@click.argument("directory", type=click.Path(exists=True))
def extract(field, value, directory):
    res = []

    try:
        for fname in glob.glob(os.path.join(directory, "*.json")):
            print(f"processing file: {fname}, result records: {len(res)}")
            with open(fname, 'r') as f:
                d = json.load(f)
                d = d["Records"]
                print(f"Size of records: {len(d)}")
                for obj in d:
                    val = _get_flatten_field_value_from_json(field, obj)
                    if val == value:
                        res.append(obj)

    except Exception as e:
        raise e

    with open(f"result-{field}-dump.json", 'w') as f:
        json.dump(res, f, indent=2)


@click.command(help="A demo.")
@click.argument("fpath", type=click.File('r'))
def demo(fpath):
    import csv
    import numpy as np
    from user_activity_anomaly_detector import UserActivityAD

    #1. load the data
    data = []

    myreader = csv.reader(fpath)
    for row in myreader:
        data.append(row)

    # randomize the data
    random.shuffle(data)

    #2. split the trainn and testing 70-30
    tr_ratio = 0.7
    tr_end_idx = int(tr_ratio * len(data))

    tr_data = data[:tr_end_idx]
    te_data = data[tr_end_idx:]

    #3. train the model
    mymodel = UserActivityAD()

    # transfer the tr_data to numpy
    tr_data = [d[1:] for d in tr_data]
    tr_data_np = np.array(tr_data, dtype=np.float64)
    
    # add Guassian noise
    noise = np.random.normal(0.0, 0.001, size=tr_data_np.shape)
    tr_data_np = tr_data_np + noise

    mymodel.train(tr_data_np)
    
    #4. do prediction
    pred = {}
    cnt = 0
    for d in te_data:
        idx = d[0]
        d_array = d[1:]
        datum = np.array(d_array).reshape(1, -1)
       
        label, score = mymodel.predict(datum)

        if label[0] < 1:
            pred[idx] = {"label": int(label[0]), "score": float(score[0])}       
            cnt += 1 

    #5. save result
    with open("result/pred_result.json", 'w') as f:
        json.dump(pred, f, indent=2)

    # info
    print("Rate of anomaly: {}".format(cnt / len(te_data)))


@click.command()
def visualize():
    pass

if __name__ == '__main__':
    cli.add_command(count)
    cli.add_command(extract)
    cli.add_command(demo)
    cli()