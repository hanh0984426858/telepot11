from flask import Flask,render_template,Response
from camera import VideoCamera
from flask import json,request

app=Flask(__name__)

@app.route('/')
def index():
    # return ("chao")
    return render_template('index.html')

def gen(camera):
    while True:
        frame=camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n'+frame
               +b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
         mimetype='multipart/X-mixed-replace; boundary=frame')

# @app.route('/github',methods=['POST'])
# def api_gh_message():
#     if request.headers['Content=Type'] == 'application/json':
#         return json.dumps(request.json)

if __name__=='__main__':
    # app.run(host='0.0.0.0',port='5000',debug=True)
    app.run(host='http://hanh0984426858.github.io/telepot9',port='443'debug=True)
