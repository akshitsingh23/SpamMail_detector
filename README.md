![SpamEmailGIF](https://github.com/akshitsingh23/Spam_Mail_Detector/assets/95421808/823feb38-57d8-4f0a-90a2-c1eebf447fef)
# 📧 Spam Mail Detector

Welcome to the Spam Mail Detector project! This project aims to analyze user-provided email text and classify it as either Spam or Valid Mail using a Machine Learning model. The project consists of a React-based frontend for a user-friendly interface and a Flask backend for running the Python machine learning code.

## 🚀 Features

- **Interactive Frontend**: Built with React and its modules to provide an engaging user experience.
- **Flask Backend**: Powers the Python machine learning model and handles requests.
- **Machine Learning**: Uses a pre-trained model and vectorizer saved with the Pickle library.
- **Dataset**: Includes a dataset for training and testing purposes, attached in the backend.

## 🛠️ Technologies Used

- **Frontend**: React, Axios, Tailwind CSS (for styling)
- **Backend**: Flask, Pickle, scikit-learn
- **Environment Setup**: Virtualenv

## 📋 Installation and Setup

Follow these steps to set up the project on your local machine:

### Frontend Setup

1. Navigate to the `frontend` directory:
   ```
   cd frontend
   ```
2. Install dependencies:
  ```
  npm install
  ```
### backend Setup
1. Start the `Frontend/Developement` Server :
   ```bash
   cd backend
   ```

2. Set up a virtual environment:
   ```
   python -m venv venv
   ```

4. Activate the virtual environment:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```
  source venv/bin/activate
  ```

4. Install required packages:
  ```
  pip install -r requirements.txt
  ```
6. Start the Flask server:
  ```
  python app.py
  ```
**Now, the backend server should be up and running. You can proceed with setting up the frontend and testing the application.
**



---

## Design Flow

- **User Input**: Users input email text via the React frontend.
- **API Request**: Frontend sends the email text to the Flask backend.
- **Text Vectorization**: Backend vectorizes the text using TfidfVectorizer.
- **Prediction**: Pre-trained model predicts if the email is Spam or Valid.
- **Response**: Backend sends the prediction result to the frontend for display.

---

## Project Structure

Spam Mail Detector/
```
├── backend/
│   ├── venv/                   # Virtual environment directory
│   ├── app.py                  # Flask application file
│   ├── emailspamdetect.py      # Python script for email spam detection
│   ├── requirements.txt        # List of Python dependencies
│   ├── model.pkl               # Pre-trained machine learning model (Pickle file)
│   ├── vectorizer.pkl          # Text vectorizer (Pickle file)
│   └── mail_data.csv           # Dataset used for training and testing
└── frontend/
    ├── public/                 # Public assets directory for React app
    ├── src/                    # Source code directory for React app
    │   ├── components/         # React components directory
    │   │   └── SpamDetectorForm.js  # Component for email input and form
    │   ├── App.js              # Main React application component
    │   ├── index.css           # CSS file for styling
    │   └── index.js            # Entry point for React application
    ├── package.json            # npm package configuration file
    └── tailwind.config.js      # Tailwind CSS configuration file
```

---

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](#) for existing issues or open a new one.

---

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

## Contact

For questions or suggestions, contact [Akshit Singh](mailto:akshitsingh2352003@gmail.com).
Project Link: [GitHub Repository](https://github.com/akshitsingh23/Spam_Mail_Detector))

---

Feel free to enhance the project and happy coding! 😃😊💓
