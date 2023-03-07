score = 0
questions = {1: "What year was python made?\nA: 1994\nB: 1991\nC: 2001\nD: 1997\n",
             2: "What was the last name of the late Queen Elizabeth II?\nA: Lincoln\nB: Reynolds\nC: Barclay\nD: Windsor\n",
             3: "What does He stand for on the periodic table?\nA: Hydrogen\nB: Helium\nC: Hassium\nD: Hafnium",
             4: "How many sides does a heptadecagon have?\nA: 170\nB: 70\nC: 17\nD: 7",
             5: "Which UK city is Banksy from?\nA: Bristol\nB: London\nC: Brighton\nD: Birmingham"}

def que(q, c):
    while True:
        a = input(q).upper()
        if a == c:
            print("Correct!")
            return 1
        else:
            print("Incorrect!")
            return 0

print("Welcome to the quiz game!\n\n\n", end="")

while True:
    score += que(questions[1], "B")
    score += que(questions[2], "D")
    score += que(questions[3], "B")
    score += que(questions[4], "C")
    score += que(questions[5], "A")
    print("Quiz completed. You scored {}/5 ({:.3f}%).".format(score, score/5*100))
    play_again = input("Play again? (Yes/No):")
    if play_again.lower != "yes":
        print("Bye!")
        break
