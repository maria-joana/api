import pendulum


def get_formated_date(date):
    """
    :param date: string in format: YYYY-MM-DD
    :return date as format DD/MM/YYYY:
    """
    formated_date = pendulum.parse(date)
    return formated_date.format('DD/MM/YYYY')
