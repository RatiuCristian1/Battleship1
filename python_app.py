# a dictionary that stores questions and answer
# have a variable that tracks the score of the playes
# loop through the dictionary using the key values pairs
#display each question to the user and allow them to answer
# tell them if they are right or wrong
# show the final result when quiz is complited


quiz = {
    "question1": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "question2": {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
    "question3": {
        "question": "What is the capital of Italy?",
        "answer": "Rome"
    },
    "question4": {
        "question": "What is the capital of Spain?",
        "answer": "Madrid"
    },
    "question5": {
        "question": "What is the capital of Austria?",
        "answer": "Wien"
    },
    "question6": {
        "question": "What is the capital of England?",
        "answer": "London"
    },
    "question7": {
        "question": "What is the capital of Holland?",
        "answer": "Amsterdam"
    },
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")
    
    if answer.lower() == value['answer'].lower():
        print('Corect')
        score += 1
        print("Your scrore is: " + str(score))
    else:
        print("Wrong!")
        print("The answer is : " + value['answer']) 
        print("Your score is : " + str(score))   











