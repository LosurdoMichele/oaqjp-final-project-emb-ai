import json
import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    @staticmethod
    def get_dominant_emotion(search_str):
        result_str = emotion_detector(search_str).replace('\n', '').replace('{', '').replace('}', '')
        # print(result_str)
        result_lst = result_str.split(',')
        # print(result_lst)
        dominant_str = result_lst[-1].split(':')[-1].strip().replace("'", '')
        # print(dominant_str)
        return dominant_str

    def test_emotion_detection(self):
        input_str_dict = {'joy': 'I am glad this happened', 
        'anger': 'I am really mad about this', 
        'disgust': 'I feel disgusted just hearing about this',
        'sadness': 'I am so sad about this',
        'fear': 'I am really afraid that this will happen'
        }
        for k, v in input_str_dict.items():
            print(v)
            result_str = self.get_dominant_emotion(v)
            self.assertEqual(result_str, k)


if __name__ == '__main__':
    unittest.main()