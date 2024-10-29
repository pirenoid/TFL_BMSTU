import requests


def check_word(word):
    url = "http://0.0.0.0:8095/checkWord"
    data = {
        "word": word
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        json_response = response.json()
        if "response" in json_response:
            if json_response['response']:
                return '1'
            else:
                return '0'
        else:
            print("Field 'response' wasn't found in response")
    else:
        print(f"Error {response.status_code}: {response.text}")
    return ''
