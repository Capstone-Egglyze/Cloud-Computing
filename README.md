# 🥚 Egglyze: Backend Flask API

## 🧠 Overview

This project focuses on building a Flask-based backend API that serves as a bridge between a machine learning (ML) model and a mobile application.
It enables real-time egg quality prediction based on shell analysis.

The backend is deployed on Google Cloud Compute Engine, integrated with Google Cloud Firestore for data management, and tested using Postman API.

## ☁️ Cloud Architecture

Below is the system architecture illustrating the cloud components and API interaction flow:
(!egglyze-diagram.png)

## ⚙️ Tech Stack

Backend Framework: Flask (Python)

Cloud Platform: Google Cloud Compute Engine

Database: Google Cloud Firestore

API Testing: Postman

Libraries: TensorFlow, Requests, Werkzeug

## 🚀 Getting Started

Follow these steps to set up and run the backend locally:

1. Clone this repository
git clone https://github.com/yourusername/egglyze-backend.git
cd egglyze-backend

2. Create a virtual environment
python -m venv venv

3. Activate the virtual environment

Windows:

.\venv\Scripts\activate


Linux / macOS:

source venv/bin/activate

4. Install dependencies
pip install flask tensorflow requests werkzeug

5. Run the backend API
python backend_API.py

6. (Optional) Test the API

You can test the API using:

Postman, or

Run the provided test script:

python test_backend.py

## 🧩 Notes

test_backend.py is an optional script for local API testing.

For production, the backend is hosted on Google Cloud Compute Engine, ensuring scalability and real-time performance.
