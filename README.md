
# Backend Flask API
1. Clone this repository.
2. Navigate to your project directory.
3. Create a virtual environment. <br>
   `python -m venv venv`
4. Activate the virtual environment. <br>
   `.\venv\Scripts\activate` (windows) <br>
   `source venv/bin/activate` (linux/macOS)
6. Install Flask and dependencies. <br>
   `pip install flask` <br>
   `pip install tensorflow requests werkzeug`
7. Open new terminal and run the following commands on each terminal. <br>
   `python backend_API.py` <br>
   `python test_backend.py` (opsional, for testing the API. If you decide to use postman, no need to run this script)

NB: 
1. test_backend.py is used to test the backend API, actually you can also use postman to test it.
2. In this project, We use Google Cloud Compute Engine to host the backend API. 