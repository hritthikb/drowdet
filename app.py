from flask import Flask, render_template, Response, request
from camera import Video

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('./home.html')

def gen(camera):
    while True:
        frame=camera.get_frame()
        yield(b'--frame\r\n'
       b'Content-Type:  image/jpeg\r\n\r\n' + frame +
         b'\r\n\r\n')

@app.route('/Capture', methods = ['POST'])
def capture():
    if request.method == 'POST':
        x = str(request.form['check'])
        if x == 'OK':
            return Response(gen(Video()),
            mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run()