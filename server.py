from flask import Flask, render_template, jsonify, request
import loads, model, tensorflow as tf
import os

app = Flask(__name__, template_folder='templates/')
app.static_folder = 'static'

@app.route('/')
def landing_page():
    return render_template('index.html')


@app.route('/model.html')
def model_page():
    video_list = get_video_list()
    video_texts = get_video_texts()
    prediction = process_selected_video()
    return render_template('model.html', video_list=video_list, video_texts=video_texts, prediction=prediction)

def get_video_list():
    video_folder = 'static/data/s1'
    video_list = [filename for filename in os.listdir(video_folder) if filename.endswith('.mp4')]
    return video_list

def get_video_texts():
    video_texts = {}
    align_list = [filename for filename in os.listdir('static/data/alignments/s1') if filename.endswith('.align')]

    for align in align_list:
        with open(f'static/data/alignments/s1/{align}') as file:
            words = file.read().splitlines()
            words = words[1:-1]
            final = []
            for word in words:
                temp = word.split(" ")
                final.append(temp[-1])
            stri = ""
            for wordss in final:
                stri += wordss
                stri += " "
            video_texts[align] = stri[:-1]

    return video_texts

@app.route('/process_selected_video', methods=['POST'])
def process_selected_video():
    data = request.json
    selected_video = data.get('video').split('.')[0]
    path = 'static/data/s1/' + selected_video + '.mpg'
    video = loads.load_video(path)

    DLmodel = model.load_model()
    yhat = DLmodel.predict(tf.expand_dims(video, axis=0))
    decoder = tf.keras.backend.ctc_decode(yhat, [75], greedy=True)[0][0].numpy()

    prediction = tf.strings.reduce_join(loads.num_to_char(decoder)).numpy().decode('utf-8')

    response_data = {'message': 'Video received successfully'}
    return jsonify(response_data)


if __name__ == '__main__':
    app.run(debug=True) 