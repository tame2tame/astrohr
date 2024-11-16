import requests
import json
import sys


sys.stdout.reconfigure(encoding='utf-8')

def make_cosmogram(data: str):
    with open('prompts\cosmogram.json', 'r', encoding='utf-8') as file:
        prompt = json.load(file)

    prompt['messages'][1]["text"] = data

    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-Key AQVNwCyoamDBxCbzQ4Yt6x-jr8feyaOkK88477Oc"
    }

    response = requests.post(url, headers=headers, json=prompt)
    result = response.json()
    text1 = result["result"]["alternatives"][0]["message"]["text"]

    return text1


def make_description(cosmogram: str):
    with open('prompts\description.json', 'r', encoding='utf-8') as file:
        prompt = json.load(file)

    prompt['messages'][1]["text"] = cosmogram
    
    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-Key AQVNwCyoamDBxCbzQ4Yt6x-jr8feyaOkK88477Oc"
    }

    response = requests.post(url, headers=headers, json=prompt)
    result = response.json()
    text1 = result["result"]["alternatives"][0]["message"]["text"]

    return text1


def calculate_relationship(cosmogram_1: str, cosmogram_2: str):
    with open("prompts/relationships.json", 'r', encoding='utf-8') as file:
        prompt = json.load(file)

    prompt['messages'][1]["text"] = cosmogram_1 + cosmogram_2
    
    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-Key AQVNwCyoamDBxCbzQ4Yt6x-jr8feyaOkK88477Oc"
    }

    response = requests.post(url, headers=headers, json=prompt)
    result = response.json()
    text1 = result["result"]["alternatives"][0]["message"]["text"]

    return text1

