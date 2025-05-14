from flask import Flask, render_template, request
from google.oauth2 import service_account
import google.auth.transport.requests
import requests

app = Flask(__name__)

# Dialogflow project and session config
PROJECT_ID = "collegeinquirychatbot-bdok"
SESSION_ID = "123456"
CREDENTIALS_FILE = "dialogflow-access.json"  # Keep this file locally and out of GitHub

def ask_dialogflow(query):
    # Authenticate using service account
    credentials = service_account.Credentials.from_service_account_file(
        CREDENTIALS_FILE,
        scopes=["https://www.googleapis.com/auth/cloud-platform"]
    )
    request_auth = google.auth.transport.requests.Request()
    credentials.refresh(request_auth)
    token = credentials.token

    # Prepare Dialogflow API request
    url = f"https://dialogflow.googleapis.com/v2/projects/{PROJECT_ID}/agent/sessions/{SESSION_ID}:detectIntent"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data = {
        "queryInput": {
            "text": {
                "text": query,
                "languageCode": "en"
            }
        }
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()["queryResult"]["fulfillmentText"]

@app.route("/")
def home():
    return render_template("chat.html")

@app.route("/chat", methods=["POST"])
def chat():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["email"]
    question = request.form["question"]

    response = ask_dialogflow(question)

    return render_template(
        "response.html",
        first_name=first_name,
        last_name=last_name,
        email=email,
        question=question,
        response=response
    )

if __name__ == "__main__":
    app.run(debug=True)
