"""Lekce #16 - Uvod do programovani, API intro"""

import gspread
from oauth2client.service_account import ServiceAccountCredentials


SCOPE = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]
CREDENTIALS = ServiceAccountCredentials.from_json_keyfile_name("creds.json", SCOPE)
CLIENT = gspread.authorize(CREDENTIALS)


def zapisovac(index: int, data: tuple) -> None:
    sheet = otevri_drive_sheet()
    # print(sheet.cell(16, 1).value)
    vloz_data_na_radek(sheet, data, index)


def otevri_drive_sheet():
    return CLIENT.open("pokus_eng").sheet1


def vloz_data_na_radek(gsheet, data, row):
    return gsheet.insert_row(data, row)


def kontrola_stavajiciho():
    return CLIENT.row_count
