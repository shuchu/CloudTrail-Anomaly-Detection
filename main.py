#-*- coding: utf-8 -*-


import click
from typing import Any
import os
import glob
import json

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


if __name__ == '__main__':
    cli.add_command(count)
    cli.add_command(extract)
    cli()