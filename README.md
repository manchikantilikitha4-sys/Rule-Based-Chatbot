# Rule-Based-Chatbot
1. Objective

The objective of this task is to create a simple rule-based chatbot using Python. The chatbot interacts with the user and responds based on predefined conditions using if-else statements.

2. Tools Required
	•	Python
	•	Any code editor (Notepad / VS Code / IDLE)
	•	Terminal or Command Prompt

3. Python Script (chatbot.py)

Copy and paste this code into a file named chatbot.py

 Rule-Based Chatbot using if-else:

print("Chatbot: Hello! I am a simple chatbot.")
print("Type 'bye' to exit the chat.\n")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello":
        print("Chatbot: Hi! How can I help you?")
    
    elif user_input == "how are you":
        print("Chatbot: I am fine. Thank you!")
    
    elif user_input == "what is your name":
        print("Chatbot: I am a rule-based chatbot.")
    
    elif user_input == "what can you do":
        print("Chatbot: I can answer simple questions.")
    
    elif user_input == "bye":
        print("Chatbot: Goodbye! Have a nice day.")
        break
    
    else:
        print("Chatbot: Sorry, I don't understand that.")

4. How to Run the Program (Step-by-Step)
	1.	Open Notepad
	2.	Paste the code
	3.	Click File → Save As
	4.	Save name as: chatbot.py
	5.	Open Command Prompt
	6.	Go to file location using cd command
Example:
cd Desktop
7.	Run the program:
python chatbot.py

5. Example Output

Chatbot: Hello! I am a simple chatbot.
Type 'bye' to exit the chat.

You: hello
Chatbot: Hi! How can I help you?

You: how are you
Chatbot: I am fine. Thank you!

You: bye
Chatbot: Goodbye! Have a nice day.

6. Deliverables
	•	Python file: chatbot.py
	•	GitHub repository with code
	•	README.md file

7. README.md Content (Formal)

You can copy and paste this in README.md:

Task 8: Rule-Based Chatbot using Python

Description:
This project implements a simple rule-based chatbot using Python. The chatbot interacts with users and provides responses based on predefined conditions using if-else statements. It can respond to greetings, basic questions, and exit commands. This project demonstrates basic Python concepts such as conditional statements, loops, and user input handling.

Features:
	•	Responds to user greetings
	•	Answers simple questions
	•	Continuous conversation using loop
	•	Exit option to stop chatbot

Tools Used:
	•	Python

Outcome:
This project helps in understanding decision-making using if-else and building basic conversational programs.

