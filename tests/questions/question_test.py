from qualitag.src.questions import Question, Answer

import pytest
from itertools import count

# Fixture to reset the Question class counter for every test (if needed)
@pytest.fixture(autouse=True)
def reset_question_counter():
    Question._Question__id_counter = count()

def test_question_initialization():
    question_text = "What is your favorite color?"
    question = Question(question_text)

    assert question.id == 0  # First question should have id 0
    assert question.question == question_text
    assert question.answers == []

def test_question_id_increment():
    q1 = Question("What is your favorite color?")
    q2 = Question("What is your favorite food?")
    
    assert q1.id == 0
    assert q2.id == 1  # Id should increment

def test_add_answer():
    question = Question("What is your favorite color?")
    answer = Answer("Blue")

    question.add_answer(answer)

    assert len(question.answers) == 1
    assert question.answers[0] == answer

def test_add_invalid_answer():
    question = Question("What is your favorite color?")

    with pytest.raises(AssertionError):
        question.add_answer("Not an answer object")  # Should raise an assertion error

def test_remove_answer():
    question = Question("What is your favorite color?")
    answer1 = Answer("Blue")
    answer2 = Answer("Red")

    question.add_answer(answer1)
    question.add_answer(answer2)

    question.remove_answer(answer1)

    assert len(question.answers) == 1
    assert question.answers[0] == answer2

def test_remove_invalid_answer():
    question = Question("What is your favorite color?")
    answer = Answer("Blue")

    with pytest.raises(AssertionError):
        question.remove_answer("Not an answer object")  # Should raise an assertion error

def test_remove_nonexistent_answer():
    question = Question("What is your favorite color?")
    answer1 = Answer("Blue")
    answer2 = Answer("Red")

    question.add_answer(answer1)

    with pytest.raises(ValueError):
        question.remove_answer(answer2)  # Should raise ValueError since answer2 is not in the list
