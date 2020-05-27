import sys
import csv
import json
from pprint import pprint as pp


def hlavni() -> None:
    obsah_json = otevri_json(SOUBOR)
    upravene = uprav_obsah(obsah_json)
    vytvor_csv(upravene)


def otevri_json(jmeno_souboru) -> dict:
    try:
        with open(jmeno_souboru, "r") as json_soub:
            return json.load(json_soub)

    except FileNotFoundError:
        print("SOUBOR NEEXISTUJE!")

    except json.decoder.JSONDecodeError:
        print("JSON POTREBUJE JAKO VSTUPNI UDAJE JEDEN OBJEKT!")


def uprav_obsah(jsony):
    zamestnanci = dict()

    for index, jeden_json in enumerate(jsony, 1):
        zamestnanci[f"por_c{index}"] = {
            "ID": jeden_json["id"],
            "EMAIL": jeden_json["email"],
            "GENDER": jeden_json["gender"],
        }

    return zamestnanci


def vytvor_csv(upr_obsah) -> None:
    with open("zamestnanci.csv", "a", newline="") as csvfile:
        zahlavi = ["ID", "EMAIL", "GENDER"]
        writer = csv.DictWriter(csvfile, fieldnames=zahlavi)
        writer.writeheader()
        for zamestnanec in upr_obsah:
            writer.writerow(
                {
                    "ID": upr_obsah[zamestnanec]["ID"],
                    "EMAIL": upr_obsah[zamestnanec]["EMAIL"],
                    "GENDER": upr_obsah[zamestnanec]["GENDER"],
                }
            )


if __name__ == "__main__":
    SOUBOR = sys.argv[1]
    hlavni()
