# Sudoku Puzzle

## Project Overview

This project is a web-based Sudoku game application where users can play Sudoku at different difficulty levels. The application is built using Python with Flask, SQLite for the database, and HTML/CSS/JavaScript for the frontend.

## Prerequisites

To run this application, you need to have the following installed:

- **Python:** The application is built with Python. You must have Python installed on your system. [Download Python](https://www.python.org/downloads/)

- **SQLite:** SQLite is used as the database for storing user data. SQLite usually comes pre-installed with Python. If not, [download SQLite](https://www.sqlite.org/download.html).

- **Flask:** Flask is a micro web framework written in Python. It is used to create and handle the backend of the application.

- **Flask-Session:** This extension for Flask provides session management. It uses the server-side for storing session data.

## Installation

1. **Clone the Repository**: First, clone the repository to your local machine using Git.

   ```bash
   git clone <[repository-url](https://github.com/Luudeus/Sudoku-Puzzle.git)>
   ```

2. **Navigate to the Project Directory**: Change your directory to the cloned project folder.

   ```bash
   cd sudoku-puzzle-web-app
   ```

3. **Install Required Python Libraries**: The required Python libraries can be installed using the `requirements.txt` file.

   - Run the following command to install these libraries:

     ```bash
     pip install -r requirements.txt
     ```

## Usage

After installing all the requirements, you can start the web application.

1. **Setting up the Environment**: Set the `FLASK_APP` environment variable to your main application file (for example, `app.py`).

   ```bash
   export FLASK_APP=app.py
   ```

2. **Running the Application**: Start the Flask application using the following command:

   ```bash
   flask run
   ```

3. **Accessing the Web Application**: Once the server starts, open a web browser and go to `http://127.0.0.1:5000/` or `http://localhost:5000/` to access the application.

4. **Navigating the Application**:
   - **Register/Login**: Users need to register and log in to play the game.
   - **Playing Sudoku**: Choose a difficulty level (easy, medium, hard, or expert) and start playing Sudoku.
   - **Leaderboard**: Check the leaderboard to see the top players.

5. **Closing the Application**: You can stop the server by pressing `CTRL+C` in the terminal where it's running.

## Additional Notes

- Ensure that your Python version is compatible with the libraries used in the project.
- The application uses SQLite, so make sure you have it properly set up on your system.
- The project structure and database setup should match the provided schema and backend code.

---
