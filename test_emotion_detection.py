import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_joy(self):
        result = emotion_detector("I am so happy today!")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_emotion_anger(self):
        result = emotion_detector("I am furious and angry!")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_emotion_disgust(self):
        result = emotion_detector("This is disgusting and gross.")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_emotion_sadness(self):
        result = emotion_detector("I am feeling very sad and depressed.")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_emotion_fear(self):
        result = emotion_detector("I am terrified and scared.")
        self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()