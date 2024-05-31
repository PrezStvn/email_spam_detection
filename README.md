# Email Classification Dashboard

## Overview
This repository contains the code and data for an Email Classification Dashboard that predicts whether emails are spam or ham. The project is structured into two main components: the backend, which handles data processing and model prediction, and the frontend, which presents an interactive dashboard for visualizing data distributions and submitting emails for classification.

## Repository Contents
- `combined_emails.csv` - The combined dataset used for training the model.
- `email_backend.py` - The backend script that processes email submissions and runs the machine learning model.
- `email_dash.py` - The frontend script that runs the Dash dashboard for interacting with the model.
- `requirements.txt` - A list of Python libraries required to run the project.
- `vectors/` - Directory containing the trained model and the TF-IDF vectors for subject and body.

## Prerequisites
Before you begin, ensure you have Python installed on your machine. It is recommended to use Python 3.6 or higher. You can download Python from [python.org](https://www.python.org/downloads/).

## Installation

1. **Clone the Repository:**
git clone https://github.com/PrezStvn/email_spam_detection.git

cd email_spam_detection


2. **Set Up a Virtual Environment (optional but recommended):**
- For Windows:
  ```
  python -m venv venv
  venv\Scripts\activate
  ```
- For MacOS/Linux:
  ```
  python3 -m venv venv
  source venv/bin/activate
  ```

3. **Install Required Libraries:**

pip install -r requirements.txt


## Running the Application

1. **Start the Backend:**

python email_backend.py

Ensure the backend server is running before starting the frontend.

2. **Launch the Dashboard:**

python email_dash.py

Once the dashboard is running, navigate to `http://localhost:8050` in your web browser to view it.

## Using the Dashboard
- **View Charts**: The dashboard displays various charts related to the data distribution and vector analyses of the emails.
- **Classify Emails**: Enter the text of an email in the provided text box and submit it to see whether it is classified as spam or ham.

  ## API Endpoint: `/predict`

### Description
The `/predict` endpoint is responsible for receiving email data and returning a classification result. It supports POST requests where the email subject and body are provided, and it responds with the email's classification as either spam or ham.

### HTTP Method
`POST`

### Request URL
```
/predict
```

### Request Body
The request must include a JSON object with the following properties:
- `subject`: A string representing the subject of the email.
- `body`: A string representing the body of the email.

#### Example Request Body
```json
{
  "subject": "Exclusive Offer Just for You!",
  "body": "Hello, I have a fantastic offer for you that you can't miss. Check out our website for amazing discounts on all products."
}
```

### Successful Response
A successful request returns a JSON object with the classification of the email.

#### Response Properties
- `classification`: (string) The classification result, either "spam" or "ham".

#### Example Successful Response
```json
{
  "classification": "spam"
}
```

### Error Response
In case of an error, such as a missing required field, the API will return an error message.

#### HTTP Status Code
- `400 Bad Request`: The request was unacceptable, often due to missing a required parameter.

#### Example Error Response
```json
{
  "error": "Missing required field: subject"
}
```

## Usage
To use this API, send a POST request to the `/predict` endpoint with a JSON payload containing the subject and body of the email you wish to classify. The API will process this data using a pre-trained machine learning model and return whether the email is likely to be spam or ham.

## Troubleshooting
- If you encounter any issues with library dependencies, ensure that all packages are correctly installed by re-running `pip install -r requirements.txt`.
- Make sure that no other processes are using the required ports (typically 8050 for Dash).

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your enhancements.
