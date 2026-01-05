'''
This module offers functionality for sentiment analysis/detection.
It sends the text to be analyzed to the watson AI.
'''
import json
import requests

def emotion_detector(text_to_analyse):
    '''
    Sentiment detection
    Params:
        text_to_analyse: str
    Returns:
        dict
    '''
    result_dict = None
    predicted_emotions = {}
    result_formatted = None
    url = 'https://sn-watson-emotion.labs.skills.network/' +  \
        'v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json=myobj, headers=header, timeout=30)
    if response.status_code == 200:
        #print(response.text)
        result_dict = json.loads(response.text)
        predicted_emotions = result_dict['emotionPredictions'][0]['emotion']
        dominant_emotion = sorted(predicted_emotions.items(), key=lambda e: e[1],
         reverse=True )[0][0]
        ordered_emotions = dict(sorted(predicted_emotions.items(), key=lambda item: item[0]))
        ordered_emotions['dominat'] = dominant_emotion
        result_formatted ="{\n" + ",\n".join(
               f"{key}: {value:.4f}" if isinstance(value, float) else f"{key}: {value}"
                for key, value in ordered_emotions.items()) + "\n}"
    return result_formatted