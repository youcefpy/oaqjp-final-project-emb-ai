import requests 
import json

def emotion_detector(text_to_analyze):
    
    text_to_analyze = text_to_analyze
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
        }
    myobj = {
         "raw_document": { 
            "text": text_to_analyze 
            } 
        }

    response = requests.post(url, json = myobj, headers=headers)

    dict_dict_ = {}

    if response.status_code == 200:
        # Convert the response text into a dictionary using the json library functions. 
        response_obj = json.loads(response.text)
        
        # Extract the required set of emotions, including anger, disgust, fear, joy and sadness, along with their scores.
        emotions_info = response_obj.get('emotionPredictions')[0]
        
        emotions = emotions_info.get("emotion")
        
        # find the dominant emotion, which is the emotion with the highest score.
        dominant_emotion = max(emotions, key=emotions.get)

        # dict with all emotions including the dominant emotion
        dict_ = {
            'anger' : emotions['anger'],
            'disgust' : emotions['disgust'],
            'fear' : emotions['fear'],
            'joy' : emotions['joy'],
            'sadness' : emotions['sadness'],
            "dominant_emotion" : dominant_emotion
        }

        return dict_
    elif response.status_code == 400 :
        dict_ = {
            'anger' : None,
            'disgust' : None,
            'fear' : None,
            'joy' : None,
            'sadness' : None,
            "dominant_emotion" : None
        }
        return dict_
