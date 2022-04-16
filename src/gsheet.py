from src.google_sheet_client_service import client


def convert_to_json(header, array, row=1):
    json = {'row': row}
    id: int = 0

    for i in range(len(header)):
        try:
            if header[i]:
                json["{}".format(header[i]).strip()] = array[i]
            else:
                json["empty_header_value-{}".format(id).strip()] = array[i]
                id += 1

        except Exception as e:
            json["{}".format(header[i]).strip()] = ""
    # TODO: rethink to map and use only values that you are need - OPTIMIZATION
    return json


def get_data_from_sheet(title, worksheet_title, validation_function=None, start_row=1):
    """
    :param title: title of google sheet document
    :param worksheet_title: title of worksheet
    :param validation_function: should be function that accepts only only one arg and should return boolean,
        default there is no validation, use validation if you want to exclude some results
    :param start_row: start row, default it start from second row (index 1)
    :return: array of data serialized by custom serializer - convert_to_json function
    """

    try:
        sheet = client.open(title)
        values = sheet.values_get(range=worksheet_title)["values"]
        header = values[0]
        data = sheet.values_get(range=worksheet_title)["values"][start_row:]
    except Exception as e:
        raise Exception({
            'message': 'Something went wrong while fetching data'
        })

    array = []
    index: int = start_row + 1
    for value in data:
        if validation_function is None or validation_function(value):
            json = convert_to_json(header, value)
            # add row attribute for referencing in update for comment
            json['row'] = index
            array.append(json)
        index += 1

    return array


def get_list_of_clients():
    """ Get array of clients """
    return get_data_from_sheet(
        title='GeneratorTreninga',
        worksheet_title='GeneratorTreningaForma',
    )


def list_of_sheets():
    return client.list_spreadsheet_files()


def get_training_list(title):
    worksheet = 'Treninzi'
    start_row = 2
    return get_data_from_sheet(
        title=title,
        worksheet_title=worksheet,
        validation_function=lambda value: value[0] and len(value) > 3,
        start_row=start_row
    )


def get_payment_list(title):
    worksheet = 'Uplate po nedeljama'
    return get_data_from_sheet(
        title=title,
        worksheet_title=worksheet,
        validation_function=lambda value: len(value) > 0
    )


def get_meals_plan(title):
    worksheet = 'Plan ishrane'
    return get_data_from_sheet(
        title=title,
        worksheet_title=worksheet,
        validation_function=lambda value: len(value) > 0 and value[2]
    )


def update_data_in_sheet(title, worksheet_title, row=1, comment=''):
    try:
        sheet = client.open(title)
        worksheet = sheet.worksheet(worksheet_title)
        worksheet.update_cell(row, 7, comment)
    except Exception as e:
        raise Exception({
            'message': 'Something went wrong while fetching data'
        })

    return {'message': 'Comment successfully updated.'}


def update_comment_for_training(title, row, comment):
    worksheet = 'Treninzi'
    return update_data_in_sheet(
        title=title,
        worksheet_title=worksheet,
        row=row,
        comment=comment
    )
