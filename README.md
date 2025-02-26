# College Inquiry Chatbot using Google Cloud Platform

## Overview
This project involves developing an **interactive college inquiry chatbot** using **Google Cloud Platform (GCP)** services such as **Google Compute Engine, Google App Engine, and Google Dialogflow**. The chatbot provides responses to student queries regarding college details, courses, fees, and more.

## Technologies Used
- **Google Compute Engine (IaaS)** - Hosting the chatbot backend
- **Google App Engine (PaaS)** - Deploying the chatbot as a web service
- **Google Dialogflow (SaaS)** - Processing natural language queries
- **Flask** (Python Web Framework) - For chatbot UI

---

## Setup Instructions
### 1. Set Up GCP Environment
1. **Create a GCP Account**
   - Sign up at [Google Cloud Console](https://console.cloud.google.com/).
   - Enable **Google App Engine** and **Google Dialogflow API**.
2. **Install Google Cloud SDK**:
   ```sh
   curl https://sdk.cloud.google.com | bash
   gcloud auth login
   ```

### 2. Deploy Flask Chatbot on Google App Engine
1. **Clone or Upload the Project Files**:
   ```sh
   git clone https://github.com/your-repo/gcp-chatbot.git
   cd gcp-chatbot
   ```
2. **Deploy the Flask App**:
   ```sh
   gcloud app deploy
   gcloud app browse
   ```

### 3. Configure Google Dialogflow
1. **Create a Dialogflow Agent** at [Dialogflow Console](https://cloud.google.com/dialogflow).
2. **Train the Agent with Example Queries**:
   - "Does the college have a football team?"
   - "Does it offer a Computer Science major?"
   - "What is the in-state tuition?"
   - "Does it provide on-campus housing?"
3. **Generate an API Key** for Dialogflow and update `flask_chatbot.py`:
   ```python
   url = "https://api.dialogflow.cloud.google.com/v2/projects/YOUR_PROJECT_ID/agent/sessions/123456:detectIntent"
   headers = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}
   ```

### 4. Test the Chatbot
- Open the chatbot URL and enter a query.
- The chatbot should return responses from **Google Dialogflow**.

---

## Expected Output
- **User enters a college-related question**.
- **Chatbot fetches response from Dialogflow**.
- **User details and chatbot creator details are displayed**.

Example Output:
```
User: John Doe | Email: john.doe@example.com
Question: Does the college have a football team?
Chatbot Answer: Yes, our college has a Division I football team.
Chatbot Creator: Your Name | Email: your.email@college.edu
 (universiy of cincinnati project)
---

## Submission
Submit **one file**:
- **GCP Chatbot URL** (where the chatbot is deployed)

---

## Conclusion
By following this guide, you will successfully **deploy an interactive chatbot on Google Cloud Platform**, leveraging **Flask and Dialogflow** to provide automated college inquiry responses.

🚀 Happy Building!

