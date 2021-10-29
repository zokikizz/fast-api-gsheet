import gspread
# import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

def convert_to_json(header, array):
    json = {}

    for i in range(len(header)):
        try:

            json["{}".format(header[i]).strip()] = array[i]

        except Exception as e:
            json["{}".format(header[i]).strip()] = ""





    return json

    # return {
    #     'timestemp': array[0],
    #     'id': array[1],
    #     'full_name': array[2],
    #     'health_issues': array[3],
    #     'email': array[4],
    #     'phone': array[5],
    #     'birthday': array[6],
    #     'weight': array[7],
    #     'height': array[8],
    #     'how_long_you_have_been_running': array[9],
    #     'pulse': array[10],
    #     'pressure': array[11],
    #
    #
    # }


scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
client = gspread.authorize(creds)

def read_all():
    sheet = client.open_by_key(key="1u9_oypyiB4pivFJ3jAcHhy3r_phB-CARMncEiJJrY_c")
    values = sheet.values_get(range="Sheet1")["values"]
    header = values[0]
    data = sheet.values_get(range="Sheet1")["values"][1:]

    worksheet = sheet.get_worksheet(0)
    cell = worksheet.find("s.vericaa@gmail.com")
    print('CELL:', cell, cell.row)
    worksheet.get_values()

    array = []
    for value in data:
        json = convert_to_json(header, value)
        array.append(json)

    return array

