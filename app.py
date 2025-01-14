from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Questions for the quiz
questions = [
    {
        "question": "What is blockchain primarily used for?",
        "options": ["Data storage", "Decentralized transactions", "Cloud computing", "Artificial Intelligence"],
        "answer": "Decentralized transactions"
    },
    {
        "question": "Which of the following is a popular cryptocurrency?",
        "options": ["Bitcoin", "Etherium", "Litecoin", "All of the above"],
        "answer": "All of the above"
    },
    {
        "question": "What does DeFi stand for?",
        "options": ["Decentralized Finance", "Distributed File System", "Data Federation", "Dynamic Finance"],
        "answer": "Decentralized Finance"
    },
    {
        "question": "What is a smart contract?",
        "options": [
            "A physical contract stored in a blockchain",
            "A self-executing contract with the terms directly written into code",
            "A contract that requires government approval",
            "None of the above"
        ],
        "answer": "A self-executing contract with the terms directly written into code"
    },
    {
        "question": "What is the primary benefit of blockchain technology?",
        "options": ["Centralization", "Decentralization", "Lower costs", "Faster processing"],
        "answer": "Decentralization"
    },
    {
        "question": "Who is credited with the creation of Bitcoin?",
        "options": ["Vitalik Buterin", "Satoshi Nakamoto", "Elon Musk", "Craig Wright"],
        "answer": "Satoshi Nakamoto"
    },
    {
        "question": "Which consensus algorithm does Bitcoin use?",
        "options": ["Proof of Stake", "Proof of Work", "Delegated Proof of Stake", "Byzantine Fault Tolerance"],
        "answer": "Proof of Work"
    },
    {
        "question": "What is the maximum supply of Bitcoin?",
        "options": ["21 million", "18 million", "25 million", "Unlimited"],
        "answer": "21 million"
    },
    {
        "question": "What is Ethereum primarily known for?",
        "options": ["Cryptocurrencyy", "Smart Contractss", "Decentralized Apps", "All of the above"],
        "answer": "All of the above"
    }
]

@app.route('/')
def home():
    # Reset the session for a new quiz
    session.clear()
    return render_template('home.html')

@app.route('/quiz/<int:question_id>', methods=['GET', 'POST'])
def quiz(question_id):
    if question_id < 0 or question_id >= len(questions):
        return redirect(url_for('home'))

    if request.method == 'POST':
        # Store the user's answer in the session
        selected_option = request.form.get('answer')
        if not selected_option:
            return render_template('question.html', question=questions[question_id], question_id=question_id, timer=15, error="Please select an option.")

        # Save the answer
        if 'answers' not in session:
            session['answers'] = {}
        session['answers'][str(question_id)] = selected_option
        session.modified = True  # Force Flask to mark the session as changed

        # Redirect to the next question or results page
        if question_id + 1 < len(questions):
            return redirect(url_for('quiz', question_id=question_id + 1))
        else:
            return redirect(url_for('result'))

    return render_template('question.html', question=questions[question_id], question_id=question_id, timer=15, error=None)

@app.route('/result')
def result():
    # Retrieve answers from the session
    answers = session.get('answers', {})

    # Calculate the score
    score = 0
    for i, question in enumerate(questions):
        correct_answer = question['answer']
        user_answer = answers.get(str(i))

        if user_answer == correct_answer:
            score += 1

    return render_template('result.html', score=score, total=len(questions))

if __name__ == '__main__':
    app.run(debug=True)