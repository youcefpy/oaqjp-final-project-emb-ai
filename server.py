"""
The server run the emotion detector package where 
it allows to know the immotion from the text input 
"""

#imports
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# init the app
app = Flask(__name__)

@app.route('/emotionDetector')
def emotion_detector_root():
    """
    Route for calling the emotion_detector method from the package EmotionDetection 
    it uses on index input field for triger the function
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    if response.get('dominant_emotion') is None:
        return "Invalid text! Please try again!."

    # Extract emotions and them scores
    return f"""For the given statement, the system response is anger: {response.get('anger')},
    'disgust': {response.get('disgust')}, 'fear': {response.get('fear')}, 
    'joy': {response.get('joy')} and 'sadness': {response.get('sadness')}. 
    The dominant emotion is {response.get('dominant_emotion')}"""


@app.route("/")
def render_index_page():
    """
    index page 
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
