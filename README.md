# HSDRUML
A Flask-based web application that uses a fine-tuned RoBERTa model to detect hate speech across various categories, including abusive/offensive language, religious hate, sexism, and profanity. The app provides real-time analysis of text inputs with probability-based predictions and features a user-friendly interface for content evaluation.

![Version](https://img.shields.io/badge/version-1.0-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
[![Support via Patreon](https://img.shields.io/badge/Support%20me%20on-Patreon-orange.svg?logo=patreon)](https://www.patreon.com/hammadkhurshid)

## Table of Contents

- [Project Overview](#project-overview)
- [Problem Statement](#problem-statement)
- [Solution](#solution)
- [Web App Components](#web-app-components)
- [Tech Stack](#tech-stack)
- [How to Use](#how-to-use)
- [Group Members](#group-members)
- [Supervisor and Co-Supervisor](#supervisor-and-co-supervisor)
- [License](#license)

## Project Overview

This project is a web application designed to detect hate speech in text data using a fine-tuned RoBERTa model. The app allows users to input text, which is then analyzed by the model to determine if it falls under any of the predefined categories such as Abusive/Offensive, Normal, Religious Hate, Sexism, or Profane/Untargeted.

## Problem Statement

Hate speech has become a significant problem in online communities, leading to harassment, bullying, and other negative consequences. Identifying and moderating such content is crucial for maintaining a healthy and inclusive environment.

## Solution

To tackle this issue, we developed a web application that uses Natural Language Processing (NLP) techniques and a fine-tuned RoBERTa model to automatically detect and classify hate speech in text data. The model is trained on a dataset with fine-grained labels to accurately identify different types of hate speech.

## Web App Components

### 1. **Frontend**
   - **Input Form**: A text box where users can input the text they want to analyze.
   - **Analyze Button**: Triggers the analysis of the input text by sending it to the backend.
   - **Results Display**: Shows the classification result with a probability score, indicating the likelihood of the text being classified under each label.

### 2. **Backend**
   - **Flask Server**: Handles the incoming requests from the frontend, processes the input text, and returns the classification results.
   - **RoBERTa Model**: The fine-tuned RoBERTa model that performs the hate speech detection.

### 3. **Model**
   - The model is trained on a dataset with five labels: Abusive/Offensive, Normal, Religious Hate, Sexism, and Profane/Untargeted.
   - The model is fine-tuned to maximize accuracy and minimize false positives/negatives.

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript (React.js)
- **Backend**: Python, Flask
- **Model**: RoBERTa (fine-tuned using Hugging Face Transformers library)
- **Database**: Not used in this project, as it is a simple input-output web app.
- **Deployment**: GitHub, Local Machine

## How to Use

1. **Clone the Repository**: 
```bash
   git clone https://github.com/hammad13khurshid/HSDRUML.git
```
2.	Install Dependencies:
```bash
   pip install -r requirements.txt
```
4.	Run the Web App:
```bash 
   flask run OR python app.py
```

4.	Input Text: Enter the text you want to analyze in the input form on the web app.
5.	Analyze: Click on the “Analyze” button to get the classification result.
6.	View Results: The results, along with the probability scores, will be displayed on the same page.

## Group Members

    •	Member 1: Hafsa Kanwal      | FA20-BSE-011
    •	Member 2: Hammad Khurshid   | FA20-BSE-013
    •	Member 3: Shoaib Ali Chohan | FA20-BSE-065

	
## Supervisor and Co-Supervisor

	•	Supervisor:      Dr. Nouman Ali
	•	Co-Supervisor:   Engr. Maryum Hamdani

## License

This project is licensed under the MIT License. See the LICENSE file for details.
