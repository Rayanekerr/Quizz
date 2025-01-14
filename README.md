# Quizz
Quizz for decentralization technologies
# Quizz
Quizz for decentralization technologies
# Documentation for Quiz Game

## Project Description
The Quiz Game is a simple Flask-based web application that allows users to answer a series of questions and see their final score. Each question is timed, and if the user does not answer within the allotted time, they are automatically moved to the next question.

## Features
- Multiple-choice questions.
- Automatic redirection to the next question when time runs out.
- Final score calculation.
- Simple and user-friendly interface.

## Installation and Setup

### Prerequisites
- Python 3.x installed on your machine.
- Flask library installed.

### Steps to Run the Application
1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```bash
   cd quiz_game
   ```
3. Install required dependencies:
   ```bash
   pip install flask
   ```
4. Run the application:
   ```bash
   python app.py
   ```
5. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## Folder Structure
```
quiz_game/
│
├── templates/         # HTML files for rendering pages
│   ├── home.html      # Home page
│   ├── question.html  # Quiz question page
│   ├── result.html    # Results page
│
├── app.py             # Main application logic
├── LICENSE            # License for the project
├── README.md          # Documentation file
```

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contributing
If you'd like to contribute, feel free to fork the repository and submit a pull request. Some suggested contributions:
- Add more questions to the quiz.
- Improve the UI/UX design.
- Add a leaderboard feature to display top scores.
