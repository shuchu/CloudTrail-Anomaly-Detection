# -*- coding: utf-8 -*-

from typing import Any

def flatten_json(
    in_json: dict[str, Any],
    prefix: str,
    out_json: dict[str, Any],
    divider: str = ".",
) -> None:
    for key in in_json:
        if isinstance(in_json[key], dict):
            # A nested object
            if prefix:
                flatten_json(in_json[key], prefix + divider + key, out_json)
            else:
                flatten_json(in_json[key], key, out_json)
        else:
            if prefix:
                new_key = prefix + divider + key
                out_json[new_key] = in_json[key]
            else:
                out_json[key] = in_json[key]

def extract_fea(fields: list[str], data: list[dict[str, Any]]) -> list[dict[str, Any]]:
    # Extract features from the data
    flatten_data = []
    for d in data:
        dd = {}
        flatten_json(d, "", dd)
        flatten_data.append(dd)

    fea = []
    for d in flatten_data:
        fea.append([d[f] for f in fields])
    
    return fea
        

