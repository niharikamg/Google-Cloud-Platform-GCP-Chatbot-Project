from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Function to interact with Dialogflow API
def ask_dialogflow(query):
    url = "https://api.dialogflow.cloud.google.com/v2/projects/YOUR_PROJECT_ID/agent/sessions/123456:detectIntent"
    headers = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}
    data = {"queryInput": {"text": {"text": query, "languageCode": "en"}}}
    response = requests.post(url, json=data, headers=headers)
    return response.json()['queryResult']['fulfillmentText']

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    question = request.form['question']
    
    response = ask_dialogflow(question)
    
    return render_template('response.html', first_name=first_name, last_name=last_name, 
                           email=email, question=question, response=response)

if __name__ == '__main__':
    app.run(debug=True)
