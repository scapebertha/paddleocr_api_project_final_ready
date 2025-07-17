
from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import numpy as np
import gc
from app.ocr_utils import run_ensemble_ocr
from app.preprocessing import resize_if_large

app = Flask(__name__)
CORS(app)

@app.route('/ocr/structured', methods=['POST'])
def ocr_structured():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file part'}), 400
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        img_bytes = file.read()
        nparr = np.frombuffer(img_bytes, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        image = resize_if_large(image)
        result = run_ensemble_ocr(image)
    except Exception as e:
        return jsonify({'error': 'OCR failed', 'details': str(e)}), 500
    finally:
        del image
        gc.collect()

    return jsonify(result)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})
