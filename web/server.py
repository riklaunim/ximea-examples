import flask

from cameras import ximea

xiC = ximea.XiCMonoConfig()
camera = ximea.XimeaCamera(xiC.get_instance())
app = flask.Flask(__name__)


@app.route('/')
def main_page():
    max_exposure = min([xiC.max_exposure(), 1000000])
    return flask.render_template(
        'index.html', min_exposure=xiC.min_exposure(), max_exposure=max_exposure,
        min_gain=xiC.min_gain(), max_gain=xiC.max_gain(),
    )


@app.route('/set-exposure/', methods=['POST'])
def set_exposure():
    camera.set_exposure(float(flask.request.form['value']))
    return 'ok'


@app.route('/set-gain/', methods=['POST'])
def set_gain():
    camera.set_gain(float(flask.request.form['value']))
    return 'ok'


@app.route('/capture-frame/', methods=['POST'])
def capture_frame():
    image = camera.get_frame()
    image.save('static/preview.bmp')
    return 'ok'
