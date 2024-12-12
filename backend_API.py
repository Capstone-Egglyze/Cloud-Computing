from flask import Flask, request, jsonify
from model_prediction import load_model_and_predict
from firestore_util import save_prediction_to_firestore  # Import fungsi Firestore

app = Flask(__name__)

@app.route('/')
def index():
    return "Image Classification API is running!"

# Route untuk mengupload gambar dan memprosesnya
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        # Melakukan prediksi model
        predicted_class, confidence = load_model_and_predict(file)

        # Simpan hasil prediksi ke Firestore
        save_prediction_to_firestore(predicted_class, confidence)

        # Kembalikan hasil prediksi dalam format JSON
        return jsonify({
            'message': 'File processed successfully',
            'prediction': {
                'predicted_class': predicted_class,
                'confidence': f"{confidence:.2f}%"
            }
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)