from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
import json

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    text_to_analyze = request.args.get('textToAnalyze')
 
    emotion_dict = emotion_detector(text_to_analyze)
    dominant_emotion = emotion_dict['dominant_emotion']
    return (
        "For the given statement, the system response is 'anger': {:.3f}, 'disgust': {:.3f}, "
        "'fear': {:.3f}, 'joy': {:.3f}, and 'sadness': {:.3f}. "
        "The dominant emotion is {}.".format(
            emotion_dict['anger'],
            emotion_dict['disgust'],
            emotion_dict['fear'],
            emotion_dict['joy'],
            emotion_dict['sadness'],
            dominant_emotion
        )
    )

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
