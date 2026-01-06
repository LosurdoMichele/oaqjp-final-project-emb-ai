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
        ordered_emotions['dominant_emotion'] = dominant_emotion
        result_formatted ="{\n" 
        for k,v in ordered_emotions.items():
            if isinstance(v, float):
                result_formatted = result_formatted + f"'{k}': {v},\n"
            else:
                result_formatted = result_formatted + f"'{k}': '{v}',\n"
    if response.status_code == 400:
        result_formatted = result_formatted + '"anger": None,' + \
                            ' "disgust": None, "fear": None, "joy": None,' + \
                            ' "sadness":None, "dominant_emotion": None'
    result_formatted = result_formatted.rsplit(",", 1)[0] + "\n}"
    return result_formatted