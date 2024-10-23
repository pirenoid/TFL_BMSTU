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
            return json_response['response']
        else:
            print("Field 'response' wasn't found in response")
    else:
        print(f"Error {response.status_code}: {response.text}")
    return ''
