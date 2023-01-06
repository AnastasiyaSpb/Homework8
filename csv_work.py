import pandas


def csv_format (data_dict):
    contacts = pandas.DataFrame(data=data_dict)
    contacts.to_csv('data.csv', index=False, sep=';')

def print_csv():
    df = pandas.read_csv('data.csv', sep=';')
    print(df)

