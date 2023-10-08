import tkinter as tk
import json
import random

#Global Variables
score = 0
question_number = 0
choice = None


def main():
    global question_label, answer_entry, score_label
    main = tk.Tk()
    main.geometry("700x350")
    main.maxsize(700, 350)
    main.minsize(700, 350)
    main.configure(bg="blue")
    main.title("Mattheww's Trivia Game")

    greeting = tk.Label(main, text="Hello, Welcome to Matthew's Trivia Game!", font=("Arial", 24), bg="blue",
                        fg="white")
    greeting.pack(pady=10, padx=20)

    selection = tk.Label(main, text="Choose Category", font=("Arial", 28), bg="blue", fg="white")
    selection.pack(pady=10, padx=20)

    gym_button = tk.Button(main, text="Gym", relief=tk.RIDGE, width=15, borderwidth=5, font=("Arial", 14),
                           command=gym_question)
    gym_button.pack(padx=15)

    space = tk.Label(text=" ", bg="blue")
    space.pack()

    volleyball_button = tk.Button(main, text="Volleyball", relief=tk.RIDGE, width=15, borderwidth=5,
                                  font=("Arial", 14), command=volleyball_question)
    volleyball_button.pack(padx=155)

    main.mainloop()


def gym_question():
    global question_label, question_number, answer_entry, score_label, root, submit_button, next_button, q, data_set
    question_number = 0
    #open each file in its specific function
    with open("gymquestions.txt") as f:
        data = f.read()  
    data_set= json.loads(data) 
    questions=list(data_set.keys())
    q=[]
    for x in range(10):
       d=random.choice(questions)
       questions.remove(d)
       q.append(d)
    print(q)
    root = tk.Tk()
    root.configure(bg="#ADD8E6")
    root.geometry("700x350")
    root.title("Gym Questions")

    question_label = tk.Label(root, bg="#ADD8E6")
    question_label.pack()

    answer_entry = tk.Entry(root)
    answer_entry.pack()

    submit_button = tk.Button(root, text="Submit", command=check_answer)
    submit_button.pack()

    next_button = tk.Button(root, text="Next Question", state=tk.DISABLED, command=next_question)
    next_button.pack(pady=10)

    score_label = tk.Label(root,bg="#ADD8E6")
    score_label.pack()

    menu_button = tk.Button(root, text="Back to Main Menu", command=root.destroy)
    menu_button.pack(pady=20)
    
    ask_question()

    root.mainloop()


def volleyball_question():
    global question_label, question_number, answer_entry, score_label, root, submit_button, next_button, q, data_set
    question_number = 0
    with open("volleyballquestions.txt") as f:
        data = f.read()  
    data_set= json.loads(data) 
    questions=list(data_set.keys())
    q=[]
    for x in range(10):
       d=random.choice(questions)
       questions.remove(d)
       q.append(d)
    print(q)
    root = tk.Tk()
    root.geometry("700x350")
    root.configure(bg="#ADD8E6")
    root.title("Volleyball Questions")

    question_label = tk.Label(root, bg="#ADD8E6")
    question_label.pack()

    answer_entry = tk.Entry(root)
    answer_entry.pack()

    submit_button = tk.Button(root, text="Submit", command=check_answer)
    submit_button.pack()

    next_button = tk.Button(root, text="Next Question", state=tk.DISABLED, command=next_question)
    next_button.pack(pady=10)

    score_label = tk.Label(root,bg="#ADD8E6")
    score_label.pack()
    
    menu_button = tk.Button(root, text="Back to Main Menu", command=root.destroy)
    menu_button.pack(pady=20)

    ask_question()
    root.mainloop()

def ask_question():
    global question_number, q, question_label, answer_entry, submit_button, score_label

    if question_number < len(q):
        question_label.configure(text=f"Question {question_number + 1}: {q[question_number]}")
        answer_entry.delete(0, tk.END)
        submit_button.config(state=tk.NORMAL) #once the user hits submit, they can move on to the next question
        next_button.configure(state=tk.DISABLED)
    else:
        question_label.configure(text="Quiz completed!")
        score_label.configure(text=f"You scored a {score}/10")
        submit_button.config(state=tk.DISABLED)
        next_button.configure(state=tk.DISABLED)

def check_answer():
    global score, question_number, q, data_set, submit_button, next_button
    user_answer = answer_entry.get()
    correct_answer = data_set[q[question_number]]
    if user_answer.lower() == correct_answer.lower():
        score += 1
        result_text = "Correct!"
    else:
        result_text = f"Wrong! The correct answer is {correct_answer}."

    result_label = tk.Label(root, text=result_text, bg="#ADD8E6")
    result_label.pack()

    submit_button.configure(state=tk.DISABLED)
    next_button.configure(state=tk.NORMAL)

    score_label.configure(text=f"Score: {score}")

def next_question():
    global question_number
    question_number += 1
    ask_question()

if __name__ == "__main__":
    main()