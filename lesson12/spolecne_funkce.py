#!/usr/local/bin/python3.8
"""Lekce #12 - Uvod do programovani, csv/json - spolecne funkce"""


def uprav_obsah(jsony: dict):
    zamestnanci = dict()

    for index, jeden_json in enumerate(jsony, 1):
        zamestnanci[f"por_c{index}"] = {
            "ID": jeden_json["id"],
            "EMAIL": jeden_json["email"],
            "GENDER": jeden_json["gender"],
        }

    return zamestnanci
