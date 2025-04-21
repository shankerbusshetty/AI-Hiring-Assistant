import json
import streamlit as st
import requests
import random


def save_candidate_data(data):
    with open("candidates.json", "a") as f:
        f.write(json.dumps(data) + "\n")


# --------------------------
# QUESTION BANK
# --------------------------

TECH_QUESTIONS = {
    "Python": [
        "Explain the difference between lists and tuples in Python.",
        "What are Python decorators and how do you use them?",
        "How does Python handle memory management?",
        "Explain the Global Interpreter Lock (GIL) in Python.",
        "What are Python generators and why would you use them?",
        "How would you handle exceptions in Python?",
        "What is the difference between 'is' and '==' in Python?",
        "Explain how Python's garbage collection works.",
        "What are lambda functions in Python?",
        "How would you implement multithreading in Python?"
    ],
    "JavaScript": [
        "Explain the difference between let, const, and var.",
        "What are closures in JavaScript?",
        "How does the event loop work in JavaScript?",
        "Explain the concept of hoisting in JavaScript.",
        "What are promises and how do they work?",
        "Explain the difference between == and === in JavaScript.",
        "What is async/await and how does it work?",
        "How would you handle errors in JavaScript?",
        "Explain the concept of 'this' in JavaScript.",
        "What are arrow functions and how do they differ from regular functions?"
    ],
    "Django": [
        "Explain Django's MTV architecture.",
        "What are Django migrations and how do they work?",
        "How would you optimize a slow Django application?",
        "Explain Django's authentication system.",
        "What are Django signals and when would you use them?",
        "How does Django handle database transactions?",
        "Explain Django's middleware system.",
        "What are class-based views and when would you use them?",
        "How would you implement caching in Django?",
        "Explain Django's ORM and its advantages."
    ],
    "React": [
        "Explain the virtual DOM in React.",
        "What are React hooks and why are they important?",
        "Explain the component lifecycle in React.",
        "What is JSX and how does it work?",
        "How would you optimize a React application?",
        "Explain state and props in React.",
        "What is Redux and when would you use it?",
        "How would you handle forms in React?",
        "Explain React's context API.",
        "What are higher-order components in React?"
    ],
    "Node.js": [
        "Explain the event-driven architecture of Node.js.",
        "What is the difference between blocking and non-blocking I/O?",
        "How would you handle errors in Node.js applications?",
        "Explain the concept of streams in Node.js.",
        "What is the purpose of the package.json file?",
        "How does Node.js handle child processes?",
        "Explain middleware in Express.js.",
        "What are the security best practices for Node.js applications?",
        "How would you scale a Node.js application?",
        "Explain the cluster module in Node.js."
    ],
    "SQL": [
        "Explain the difference between INNER JOIN and LEFT JOIN.",
        "What are database indexes and why are they important?",
        "How would you optimize a slow SQL query?",
        "Explain database normalization.",
        "What are stored procedures and when would you use them?",
        "Explain ACID properties in databases.",
        "What is the difference between DELETE, TRUNCATE, and DROP?",
        "How would you handle database transactions?",
        "Explain the difference between NoSQL and SQL databases.",
        "What are database views and when would you use them?"
    ],
    "Java": [
        "Explain the difference between JDK, JRE, and JVM.",
        "What are the main features of Java 8?",
        "Explain the concept of multithreading in Java.",
        "What are Java generics and why are they useful?",
        "Explain the Java memory model.",
        "What are Java streams and how do they work?",
        "Explain exception handling in Java.",
        "What is the difference between == and .equals() in Java?",
        "Explain Java's garbage collection mechanism.",
        "What are Java annotations and how do you use them?"
    ],
    "HTML": [
        "Explain the difference between HTML4 and HTML5.",
        "What are semantic HTML elements and why are they important?",
        "Explain the HTML document structure.",
        "What are data attributes and how would you use them?",
        "Explain the difference between block and inline elements.",
        "How would you optimize a website for accessibility?",
        "What are meta tags and why are they important?",
        "Explain the difference between cookies, localStorage, and sessionStorage.",
        "How would you embed multimedia content in HTML?",
        "Explain the purpose of the DOCTYPE declaration."
    ],
    "CSS": [
        "Explain the CSS box model.",
        "What are CSS preprocessors and why would you use them?",
        "Explain the difference between display: none and visibility: hidden.",
        "What are CSS Grid and Flexbox and when would you use each?",
        "Explain CSS specificity and how it works.",
        "How would you implement responsive design in CSS?",
        "What are CSS variables and how do you use them?",
        "Explain the difference between margin and padding.",
        "What are CSS animations and how do you implement them?",
        "Explain the concept of BEM in CSS."
    ]
}

# --------------------------
# PROMPT ENGINEERING SECTION
# --------------------------

def greeting_prompt(name, tech_stack):
    return f"Hi {name}! Welcome to TalentScout. I'll be asking a few questions based on your tech stack: {', '.join(tech_stack)}."

def generate_random_questions(tech_stack, num_questions=5):
    questions = []
    for tech in tech_stack:
        if tech in TECH_QUESTIONS:
            questions.extend(TECH_QUESTIONS[tech])
    
    # Remove duplicates and shuffle
    unique_questions = list(set(questions))
    random.shuffle(unique_questions)
    
    # Return requested number of questions
    return unique_questions[:num_questions]

def fallback_prompt():
    return "I'm sorry, I didn't understand that. Could you rephrase?"

# --------------------------
# STREAMLIT APP START
# --------------------------

st.set_page_config(page_title="TalentScout AI Assistant")
st.title("TALENTSCOUT - HIRING ASSISTANT")

# Initialize session state variables
if 'current_stage' not in st.session_state:
    st.session_state.current_stage = "personal_details"
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'generated_questions' not in st.session_state:
    st.session_state.generated_questions = []
if 'current_question_index' not in st.session_state:
    st.session_state.current_question_index = 0

exit_keywords = ["exit", "quit", "end", "stop"]

# --------------------------
# Personal Details Stage
# --------------------------

# ✅ Personal Details Stage
if st.session_state.current_stage == "personal_details":
    st.write("Welcome to TalentScout! Thank you for joining us today."
            " This interview will help us better understand your skills, experience, and how you can contribute to our team."
            " We’ll ask you a series of questions related to your background and the tech stack you work with."
             " Please fill in your details to begin.")
    
    with st.form("personal_details_form"):
        st.session_state.full_name = st.text_input("Full Name")
        st.session_state.email = st.text_input("Email Address")
        st.session_state.phone = st.text_input("Phone Number")
        st.session_state.experience = st.number_input("Years of Experience", min_value=0, step=1)
        st.session_state.position = st.text_input("Desired Position(s)")
        st.session_state.location = st.text_input("Current Location")
        
        submit_details = st.form_submit_button("Submit Details")

    if submit_details:
        # Check if any of the required fields are empty
        missing_fields = []

        if not st.session_state.full_name:
            missing_fields.append("Full Name")
        if not st.session_state.email:
            missing_fields.append("Email Address")
        if not st.session_state.phone:
            missing_fields.append("Phone Number")
        if st.session_state.experience == 0:  # Checking if experience is 0, assuming 0 is not valid input
            missing_fields.append("Years of Experience")
        if not st.session_state.position:
            missing_fields.append("Desired Position(s)")
        if not st.session_state.location:
            missing_fields.append("Current Location")

        # If any field is missing, show an error message
        if missing_fields:
            if len(missing_fields) == 6:
                st.error("Please fill in all details.")
            else:
                st.error(f"Please fill in the following fields: {', '.join(missing_fields)}")
        else:
            # ✅ Collect form data
            candidate_data = {
                "full_name": st.session_state.full_name,
                "email": st.session_state.email,
                "phone": st.session_state.phone,
                "experience": st.session_state.experience,
                "position": st.session_state.position,
                "location": st.session_state.location
            }

            # ✅ Save to JSON
            save_candidate_data(candidate_data)

            st.success("Candidate data saved successfully!")

            # ✅ Go to next stage
            st.session_state.current_stage = "tech_stack"
            st.rerun()

# --------------------------
# Tech Stack Stage
# --------------------------

elif st.session_state.current_stage == "tech_stack":
    st.success("Personal details submitted successfully!")
    st.write("Email:", st.session_state.email)
    st.write("Phone:", st.session_state.phone)
    st.write("Experience:", st.session_state.experience, "years")
    st.write("Desired Role:", st.session_state.position)
    st.write("Location:", st.session_state.location)
    
    st.write("Please select your tech stack and click 'Start Interview':")
    
    with st.form("tech_stack_form"):
        st.session_state.tech_stack = st.multiselect(
            "Tech Stack (Select all you know)",
            ["Python", "JavaScript", "Django", "React", "Node.js", "SQL", "Java", "HTML", "CSS"]
        )
        
        submit_tech = st.form_submit_button("Start Interview")
        
        if submit_tech:
            if not st.session_state.tech_stack:
                st.error("Please select at least one technology")
            else:
                # Generate 5 random questions from the selected tech stacks
                st.session_state.generated_questions = generate_random_questions(st.session_state.tech_stack)
                
                # Start the interview
                st.session_state.current_stage = "interview"
                st.session_state.current_question_index = 0
                st.rerun()

# --------------------------
# Interview Stage
# --------------------------

# --------------------------
# Interview Stage
# --------------------------

elif st.session_state.current_stage == "interview":
    # Display greeting at the start of the interview
    if st.session_state.current_question_index == 0 and not any("Welcome to TalentScout" in msg[1] for msg in st.session_state.chat_history):
        greet = greeting_prompt(st.session_state.full_name, st.session_state.tech_stack)
        st.session_state.chat_history.append(("AI", greet))
    
    # Check if we have more questions
    if st.session_state.current_question_index < len(st.session_state.generated_questions):
        current_question = st.session_state.generated_questions[st.session_state.current_question_index]
        
        # Display the current question if not already in chat history
        if not any(msg[1] == current_question for msg in st.session_state.chat_history if msg[0] == "AI"):
            st.session_state.chat_history.append(("AI", current_question))
        
        # Display chat history
        st.subheader("Interview in Progress")
        for sender, message in st.session_state.chat_history:
            if sender == "User":
                st.markdown(f"**You:** {message}")
            else:
                st.markdown(f"**AI:** {message}")
        
        # Get user response
        user_input = st.text_input(
            f"Your answer to Q{st.session_state.current_question_index + 1}/{len(st.session_state.generated_questions)} (type 'exit' to end):", 
            key=f"q{st.session_state.current_question_index}"
        )
        
        if user_input:
            user_input = user_input.strip().lower()
            st.session_state.chat_history.append(("User", user_input))
            
            if user_input in exit_keywords:
                st.session_state.chat_history.append(("AI", "Thank you for chatting. Goodbye and good luck! 👋"))
                st.session_state.current_stage = "interview_complete"
                st.rerun()
            else:
                st.session_state.current_question_index += 1
                st.rerun()
    else:
        # Interview complete
        if not any("Thank you for completing the interview!" in msg[1] for msg in st.session_state.chat_history):
            st.session_state.chat_history.append(("AI", " **Thank you for completing the interview!** We appreciate the time and effort you put into your interview today. "
        "Our team will review your responses and qualifications, and we will notify you about the next steps in the hiring process soon. "
        "Thank you again, and we look forward to potentially working with you!"))
        st.session_state.current_stage = "interview_complete"
        st.rerun()

# --------------------------
# Interview Complete Stage
# --------------------------

elif st.session_state.current_stage == "interview_complete":
    st.success("Interview Completed!")
    st.subheader("Full Conversation")
    
    for sender, message in st.session_state.chat_history:
        if sender == "User":
            st.markdown(f"**You:** {message}")
        else:
            st.markdown(f"**AI:** {message}")
    
    if st.button("Start New Interview"):
        # Reset session state
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()