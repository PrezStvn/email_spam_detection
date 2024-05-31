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

## Troubleshooting
- If you encounter any issues with library dependencies, ensure that all packages are correctly installed by re-running `pip install -r requirements.txt`.
- Make sure that no other processes are using the required ports (typically 8050 for Dash).

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your enhancements.
