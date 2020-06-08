#!/home/mholinka/projects/python_academy/env/bin/python
"""Lekce #15 - Uvod do programovani, web scraping"""

import csv

import requests
from bs4 import BeautifulSoup

URL = "http://heroes3.cz/hraci"


def main():
    response = get_response()
    parsed = parse_content(response)

    table = find_table(parsed)
    rows = find_rows(table)

    results = [get_data(row) for row in rows if get_data(row) != None]
    write_into_csv(results)


def get_response() -> requests.models.Response:
    return requests.get(URL)


def parse_content(resp: requests.models.Response):
    return BeautifulSoup(resp.text, "html.parser")


def find_table(cont):
    return cont.find("table", {"class": "tab_top"})


def find_rows(tabl) -> list:
    return tabl.find_all("tr")[1:]  # set up the filter --> [1:]


def get_data(tr):
    """
    Do funkce vstupuje promenna "row" --> bs4.element.tag.obj. 

    Prochazime nejprve elementy "tr" --> radky tabulky. Potom prochazime
    sloupce "td" a nacitame jejich obsah "text".

    Ziskana data spojime do tuplu a vracime z funkce.
    """
    try:
        player = tr.find_all("td")[2].text
        placement = tr.find_all("td")[0].text
        total_games = tr.find_all("td")[6].text
        total_wins = tr.find_all("td")[5].text
        rating = tr.find_all("td")[7].text

        return (player, placement, total_games, total_wins, rating)

    except AttributeError:
        print("Assignment fails!")
    # except IndexError:  # other possibility how to protect our spider
    #     print("Index out of range! Still trying to get data...")


def write_into_csv(data):
    with open("players.csv", "w", newline="") as csv_f:
        writer = csv.writer(csv_f)
        writer.writerows(data)


if __name__ == "__main__":
    main()
