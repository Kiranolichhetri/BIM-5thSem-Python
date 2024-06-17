# Create a program capable of displaying questions to the user like KBC.
# Use List data type to store the questions and their correct answer
# Display the final amout the person is takig home after playing the game.

# Questions and answers
questions_list = [
    {
        "question": "How many continents are there?",
        "answer": "7"
    },
    {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "answer": "Jupiter"
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "answer": "Shakespeare"
    },
    {
        "question": "What is the boiling point of water?",
        "answer": "100"
    }
]

# Prize money for each question
prize_money = [1000, 2000, 5000, 10000, 20000]

# Function to play the game
def play_game():
    total_amount = 0
    
    for i, q in enumerate(questions_list):
        print(f"Question {i+1}: {q['question']}")
        user_answer = input("Your answer: ")
        
        if user_answer.strip().lower() == q['answer'].strip().lower():
            print("Correct!")
            total_amount += prize_money[i]
        else:
            print("Incorrect.")
            break
        
        print(f"Current amount: {total_amount}")
        print()
    
    print(f"Game over! You are taking home ${total_amount}")

# Start the game
play_game()
