'''
This module offers functionality for sentiment analysis/detection.
It sends the text to be analyzed to the watson AI.
'''
import json
import requests

def sentiment_detection(text_to_analyse):
    '''
    Sentiment detection
    Params:
        text_to_analyse: str
    Returns:
        dict
    '''
    result = None
    url = 'https://sn-watson-emotion.labs.skills.network/' +  \
        'v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json=myobj, headers=header, timeout=30)
    if response.status_code == 200:
        print(response.text)
        result = response.text

    return result