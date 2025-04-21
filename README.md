# TalentScout Hiring Assistant Chatbot 

## Project Overview

The **TalentScout Hiring Assistant Chatbot** is an AI-powered tool designed to help streamline the hiring process by automating candidate assessment during initial interviews. Developed with **Python** and **Streamlit**, the chatbot interacts with candidates to collect their personal details, tech stack, and generate tailored technical questions. The goal is to provide a seamless and efficient interview experience for HR professionals.

Key features include:
- Collecting candidate details (name, email, tech stack, etc.)
- Generating **5 technical questions** based on the candidate's chosen tech stack
- Real-time interactive interface using **Streamlit**
- Hugging Face’s **Transformers** library to generate questions based on tech stack

---

## Installation Instructions

To run the **TalentScout Hiring Assistant Chatbot** locally, follow these steps:

1. **Clone the repository** to your local machine.
   - Download or clone the project repository from GitHub to your local environment.

2. **Set up a virtual environment** (optional but recommended):
   - Create a new virtual environment for isolating dependencies.

3. **Install dependencies**:
   - Install all required libraries specified in the **requirements.txt** file.

4. **Launch the Streamlit application**:
   - Run the application using the appropriate command in your terminal or command prompt to start the chatbot locally.

5. Open your browser and visit the URL provided by Streamlit (typically `http://localhost:8501`) to interact with the chatbot.

---

## Usage Guide

Once the application is running, the user will be prompted to enter basic information such as:
- **Full Name**
- **Email Address**
- **Years of Experience**
- **Preferred Tech Stack** (e.g., Python, JavaScript, etc.)

After collecting the information, the chatbot will generate **5 technical questions** based on the selected tech stack. The user can respond to each question in real-time, making the interview process interactive and dynamic.

---

## Technical Details

### Libraries Used:
- **Streamlit**: For creating the frontend interface and managing user interactions.
- **Transformers (Hugging Face)**: For generating technical questions tailored to the candidate’s tech stack.
- **Python**: Backend logic for handling user inputs and interactions.

### Model Details:
- The **Hugging Face Transformers** library is used to generate relevant technical questions based on the candidate's tech stack. The model is designed to understand and generate questions suitable for various tech stacks, such as Python, JavaScript, and more.

### Architectural Decisions:
- **In-memory storage**: The candidate data and responses are stored temporarily during the session. Future versions could include database integration for storing data permanently.
- **Static question bank**: A predefined set of questions mapped to specific tech stacks is used to generate relevant questions. This approach simplifies question management and updates.

---

## Prompt Design

The prompts used to gather information and generate technical questions were carefully crafted to ensure:
1. **Effective Information Gathering**: Each prompt is designed to collect the candidate's details in a straightforward manner (name, email, tech stack).
2. **Context-Specific Question Generation**: After gathering the tech stack, the chatbot generates questions that are tailored to the selected skills, providing a relevant challenge to the candidate.
3. **Smooth User Experience**: The conversation flow is designed to be user-friendly, with easy-to-understand instructions and responses, ensuring a seamless experience for both the candidate and the interviewer.

---

## Challenges & Solutions

###  **1.Challenge**: Generating relevant and specific questions based on the tech stack.
   - **Solution**: A static question bank was created, where each tech stack (e.g., Python, JavaScript) has a set of associated questions. This allows the chatbot to generate accurate and relevant technical questions.

### **2.Challenge**: Maintaining the conversation context and user inputs across multiple interactions.
   - **Solution**: **Streamlit's session state** is used to maintain context during the conversation, storing user responses and progress throughout the session.

### **3.Challenge**: Generating dynamic questions based on user input.
   - **Solution**: Hugging Face's **Transformers** library is leveraged to generate context-aware questions based on the provided tech stack. This helps tailor the questions to each candidate’s experience and skill set.


## Future Improvements

- Integrate a database for permanent storage of candidate data and responses.
- Add scoring and feedback mechanisms based on candidate responses.
- Develop an admin dashboard for interviewers to track candidate performance.
- Enable PDF exports for candidate reports.
- Expand language support to cater to a global audience.

---

## Author

Shanker Busshetty|https://github.com/shankerbusshetty| Email: shankerbussetty@gmail.com

---
