''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
import json
# Import Flask, render_template, request from the flask pramework package
from flask import Flask, render_template, request
# Import the emotion_detector function from the package created
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask(__name__)

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''

    text_to_analyze = request.args.get('textToAnalyze')
    #if text_to_analyze == '' or text_to_analyze is None:
    #    return 'No text given! Please provide text to be analyzed.'
    output_str = emotion_detector(text_to_analyze).replace("'", '"')
    print(output_str)
    output_json = json.loads(output_str)
    print(f'{type(output_json)=} : {output_json}  ')
    dominant_emotion = output_json.pop("dominant_emotion")
    formatted_output = f'For the given statement, the system response is '
    for k, v in output_json.items():
        formatted_output = formatted_output + f"'{k}': {v}, "
    formatted_output = formatted_output + f'. The dominant emotion is <b>{dominant_emotion}<b>'
    return formatted_output


if __name__ == "__main__":
    # This functions executes the flask app and deploys it on localhost:5000

    app.run()