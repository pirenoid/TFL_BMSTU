import requests
from table import Table

url = "http://0.0.0.0:8095/checkTable"

table = Table()


while True:
    table_data = table.get_table()
    response = requests.post(url, json=table_data)
    if response.status_code == 200:
        if response.json()['response'] == 'true':
            print('WIN')
            break
        else:
            print('!!!!!!!!!!!!!!', response.json()['response'])
            table.add_contr_example(response.json()['response'])
            print(table_data)


