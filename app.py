import subprocess
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
from cnnClassifier.utils.common import decodeImage
from cnnClassifier.pipeline.prediction import PredictionPipeline
from cnnClassifier import logger

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = 'inputImage.jpg'
        self.classifier = PredictionPipeline(self.filename)


@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/train", methods=['GET', 'POST'])
@cross_origin()
def trainRoute():
    try:
        result = subprocess.run(
            ['dvc', 'repro'],
            capture_output=True,
            text=True,
            check=True
        )
        logger.info(result.stdout)
        return jsonify({'status': 'success', 'message': 'Training completed successfully'})
    except subprocess.CalledProcessError as e:
        logger.error(f"Training failed: {e.stderr}")
        return jsonify({'status': 'error', 'message': 'Training failed', 'details': e.stderr}), 500

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    payload = request.get_json(silent=True)
    if not payload or 'image' not in payload:
        return jsonify({'status': 'error', 'message': 'Missing "image" field in request body'}), 400

    try:
        decodeImage(payload['image'], clApp.filename)
        result = clApp.classifier.predict()
        return jsonify(result)
    except Exception as e:
        logger.exception("Prediction failed")
        return jsonify({'status': 'error', 'message': 'Prediction failed'}), 500

if __name__ == '__main__':
    clApp = ClientApp()
    app.run(host='0.0.0.0', port=8000)
