from google.cloud import firestore

# Inisialisasi Firestore client
db = firestore.Client()

def save_prediction_to_firestore(predicted_class, confidence):
    """
    Menyimpan hasil prediksi ke Firestore.
    """
    try:
        # Menyusun data yang akan disimpan
        prediction_data = {
            'predicted_class': predicted_class,
            'confidence': confidence,
            'timestamp': firestore.SERVER_TIMESTAMP  # Timestamp server
        }

        # Menyimpan data ke koleksi 'predictions'
        doc_ref = db.collection('predictions').add(prediction_data)
        print("Prediction saved successfully")
    except Exception as e:
        print(f"Error saving prediction: {e}")