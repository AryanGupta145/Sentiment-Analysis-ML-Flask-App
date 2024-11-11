Sentiment Analysis ML Flask App
Author: Aryan Gupta

This project is a Flask web application for Sentiment Analysis on Restaurant Reviews. It allows users to input restaurant reviews and receive sentiment predictions (positive, negative, or neutral). The backend integrates a novel Hybrid model combining RoBERTa and Electra models, achieving 78% accuracy, trained specifically for sentiment analysis on restaurant reviews.

Project Overview
The goal of this project is to analyze and classify restaurant reviews based on sentiment, using a custom hybrid model of RoBERTa and Electra. This is part of a capstone project for my final year of B.Tech in Information Technology.

Key Features
Hybrid Model: Combines the strengths of RoBERTa and Electra for improved sentiment prediction accuracy.
Flask Web App: A simple interface for users to input restaurant reviews and receive sentiment predictions.
Twitter Dataset: Trained on a custom dataset of restaurant reviews from Twitter, focusing on polarity (positive, negative, or neutral).
Frontend Integration: Developed using HTML, CSS, and JavaScript in VS Code, integrated with Flask for a seamless user experience.


Project Structure


Sentiment-Analysis-ML-Flask-App/
├── app.py                     # Main Flask app for handling requests
├── SentimentAnalysisOnRestaurantReview.ipynb  # Jupyter notebook for model training and experimentation
├── requirements.txt           # Dependencies required for the project
├── model/                     # Folder containing saved models
│   ├── hybrid
├── static/                    # Static files (CSS, JavaScript)
├── templates/                 # HTML templates for the web app
└── README.md                  # Project description and instructions


Usage
Open the web app in your browser.
Enter a restaurant review in the provided text box.
Click Submit to analyze the sentiment.
The app will return the sentiment of the review as either Positive, Negative, or Neutral.
Model Training and Development
This project involved developing a custom hybrid model to improve sentiment prediction accuracy by combining:

RoBERTa: Robustly optimized BERT approach.
Electra: Efficiently learns representations by predicting replaced token detection.
Both models were trained in the Jupyter notebook (SentimentAnalysisOnRestaurantReview.ipynb) and saved for deployment with Flask.

Future Improvements
Aspect-Based Sentiment Analysis: Extend the model to detect specific aspects of sentiment.
Deploy on Cloud: Use cloud hosting (e.g., AWS or Heroku) for production deployment.
Enhanced UI: Improve the frontend design for a better user experience.
Contributing
Feel free to open issues or submit pull requests if you’d like to improve this project. Contributions, suggestions, and feedback are welcome.

License
This project is open-source and available under the MIT License.