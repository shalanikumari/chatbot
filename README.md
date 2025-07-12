Breakdown of the Code
1. Importing Required Modules
import random
from datetime import datetime
random: Used to select random responses from predefined lists (e.g., greetings, farewells).

datetime: Used to fetch and format the current date and time.

2. Defining the chatbot() Function
def chatbot():
This function encapsulates the entire chatbot logic.

3. Greeting the User
print("Welcome to ChatBot! (Type 'bye' to exit)\n")
When the program starts, it displays a welcome message instructing users how to exit.

4. Predefined Response List
greetings = ["Hello!", "Hi there!", "Hey!", "Namaste!", "How can I help you!"]
farewell = ["Goodbye!", "See you later!", "Bye! Have a nice day!", "Take care!", "Nice to meet you!!"]
greetings: List of possible replies for greetings.

farewell: List of replies used when the user ends the conversation.

5. Main Chat Loop

while True:
    user_input = input("You: ").lower()
A while loop keeps the chatbot running until the user types an exit command.

input() gets the user's message.

.lower() ensures case-insensitive comparison by converting the input to lowercase.

6. Handling User Input with Conditionals
The chatbot checks for specific keywords in the user’s input using if/elif statements.

Examples:

Greeting Check:
if "hello" in user_input or "hi" in user_input:
    print(f"Bot: {random.choice(greetings)}")
Returns a random greeting.

Checking for time:
elif "what is the time now" in user_input:
    now = datetime.now().strftime("%H:%M:%S")
    print(f"Bot: The current time is {now}.")
Uses the datetime module to print the current time in HH:MM:SS format.

Checking for date or day:
elif "what is the date" in user_input or "what is the day" in user_input:
    today = datetime.now().strftime("%A, %d %B %Y")
    print(f"Bot: Today is {today}.")
Displays the day of the week and full date.

Exit Condition:
elif "bye" in user_input or "exit" in user_input:
    print(f"Bot: {random.choice(farewell)}")
    break
Ends the chat session with a random farewell message and exits the loop using break.

7. Default Response for Unknown Input
else:
    print("Bot: Hmm... I didn't understand that. Can you rephrase?")
Provides a fallback response when the input doesn’t match any predefined condition.

