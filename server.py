"""Flask web application for emotion detection analysis."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    """Analyze text for emotional content and return formatted results.
    
    Returns:
        str: Formatted analysis of emotional content or error message for invalid input.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    emotion_dict = emotion_detector(text_to_analyze)
    dominant_emotion = emotion_dict['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again."

    anger = emotion_dict['anger']
    disgust = emotion_dict['disgust']
    fear = emotion_dict['fear']
    joy = emotion_dict['joy']
    sadness = emotion_dict['sadness']

    return (
        f"For the given statement, the system response is 'anger': {anger:.3f}, "
        f"'disgust': {disgust:.3f}, 'fear': {fear:.3f}, 'joy': {joy:.3f}, and "
        f"'sadness': {sadness:.3f}. The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """Render the main index page.
    
    Returns:
        str: Rendered HTML template for the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
