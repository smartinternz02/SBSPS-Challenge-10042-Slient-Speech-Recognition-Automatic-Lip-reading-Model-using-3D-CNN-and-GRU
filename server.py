from flask import Flask, render_template, request
import loads, model, tensorflow as tf
import matplotlib.pyplot as plt

app = Flask(__name__, template_folder='templates/')

@app.route('/', methods=['GET'])
def landing_page():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    video_file = request.files['videoFile']
    path = 'videos/' + video_file.filename
    video_file.save(path)

    video = loads.load_video(path)

    DLmodel = model.load_model()
    yhat = DLmodel.predict(tf.expand_dims(video, axis=0))
    decoder = tf.keras.backend.ctc_decode(yhat, [75], greedy=True)[0][0].numpy()
    
    prediction = tf.strings.reduce_join(loads.num_to_char(decoder)).numpy().decode('utf-8')

    print(prediction)


    return render_template('index.html')


if __name__ == '__main__':
    app.run() 