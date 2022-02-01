from google_sheet_client_service import client


def convert_to_json(header, array):
    json = {}

    for i in range(len(header)):
        try:

            json["{}".format(header[i]).strip()] = array[i]

        except Exception as e:
            json["{}".format(header[i]).strip()] = ""
    # TODO: rethink to map and use only values that you are need - OPTIMIZATION
    return json


def get_list_of_clients():
    """ Get array of clients """
    sheet = client.open("GeneratorTreninga")
    values = sheet.values_get(range="GeneratorTreningaForma")["values"]
    header = values[0]
    data = sheet.values_get(range="GeneratorTreningaForma")["values"][1:]

    worksheet = sheet.get_worksheet(0)
    cell = worksheet.find("s.vericaa@gmail.com")
    # print('CELL:', cell, cell.row)
    worksheet.get_values()

    array = []
    for value in data:
        json = convert_to_json(header, value)
        array.append(json)

    return array

