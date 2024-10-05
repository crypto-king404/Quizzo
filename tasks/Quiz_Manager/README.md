# `quiz_manager.py`

## Overview

`quiz_manager.py` is a Python module that manages quiz navigation and question retrieval for quizzes generated using the `QuizGenerator` class. It provides functionality to navigate through the quiz questions and ensures a smooth quiz-taking experience by managing question indices and displaying questions in the desired order.

### Table of Contents
1. [Installation](#installation)
2. [Classes and Methods](#classes-and-methods)
    - [QuizManager](#quizmanager)
        - [`__init__`](#__init__)
        - [`get_question_at_index`](#get_question_at_index)
        - [`next_question_index`](#next_question_index)
3. [Usage](#usage)
4. [Example](#example)
5. [Dependencies](#dependencies)

## Installation

Before using the module, ensure that you have the following libraries installed:

```bash
pip install streamlit
```

Additionally, make sure that `DocumentProcessor`, `EmbeddingClient`, `ChromaCollectionCreator`, and `QuizGenerator` classes from the `tasks` module are correctly set up in your project directory.

## Classes and Methods

### `QuizManager`

The `QuizManager` class handles quiz navigation and question retrieval. It takes a list of quiz questions as input and provides methods to retrieve questions based on their index and navigate to the next or previous question.

#### `__init__(self, questions: list)`

**Parameters:**
- `questions`: A list of quiz questions. Each question should be a dictionary containing the question text, choices, answer, and explanation.

**Description:**
Initializes the `QuizManager` with a list of quiz questions. The constructor calculates and stores the total number of questions.

---

#### `get_question_at_index(self, index: int)`

**Parameters:**
- `index`: An integer representing the index of the question to retrieve.

**Description:**
Retrieves the quiz question at the specified index. If the index is out of bounds, the method wraps around and returns a question starting from the beginning. This ensures that the quiz can loop through questions seamlessly.

**Returns:**
- A dictionary representing the quiz question at the specified index.

---

#### `next_question_index(self, direction=1)`

**Parameters:**
- `direction`: An integer indicating the direction to move in the quiz. Use `1` to move to the next question and `-1` to move to the previous question.

**Description:**
Adjusts the current quiz question index based on the specified direction and updates the session state to reflect the new index. This method is useful for navigating through the quiz in Streamlit-based applications.

---

## Usage

```python
import streamlit as st
from tasks.Quiz_Generator.quiz_generator import QuizGenerator
from tasks.Quiz_Manager.quiz_manager import QuizManager

# Assuming you have a list of questions generated
questions = [
    {
        "question": "What is the capital of France?",
        "choices": [
            {"key": "A", "value": "Paris"},
            {"key": "B", "value": "London"},
            {"key": "C", "value": "Berlin"},
            {"key": "D", "value": "Madrid"}
        ],
        "answer": "A",
        "explanation": "Paris is the capital and most populous city of France."
    }
    # Add more questions as needed
]

# Initialize the QuizManager with a list of questions
quiz_manager = QuizManager(questions)

# Retrieve a question by its index
question = quiz_manager.get_question_at_index(0)
st.write(f"Question: {question['question']}")

# Navigate to the next question
quiz_manager.next_question_index(direction=1)
```

## Example

To use the `QuizManager` class, ensure that you have a list of quiz questions generated using the `QuizGenerator` class or manually created. Pass this list to `QuizManager` and use the `get_question_at_index()` and `next_question_index()` methods to display and navigate through questions in your application.

## Dependencies

- Python 3.x
- `streamlit`
