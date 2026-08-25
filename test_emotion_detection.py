import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):

    def test_emotion_joy(self):
        self.assertEqual(emotion_detector('I am glad this happened').get('dominant_emotion'), 'joy')
    
    def test_emotion_anger(self):
        self.assertEqual(emotion_detector('I am really mad about this').get('dominant_emotion'), 'anger')
    
    def test_emotion_disgust(self):
        self.assertEqual(emotion_detector('I feel disgusted just hearing about this').get('dominant_emotion'), 'disgust')
    
    def test_emotion_sadness(self):
        self.assertEqual(emotion_detector('I am so sad about this').get('dominant_emotion'), 'sadness')
    
    def test_emotion_fear(self):
        self.assertEqual(emotion_detector('I am really afraid that this will happen').get('dominant_emotion'), 'fear')


if __name__ == "__main__" : 
    unittest.main() 