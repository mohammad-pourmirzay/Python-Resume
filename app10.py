import termcolor

print(termcolor.colored("Hello, welcome to the question game", color = "green"))
print(termcolor.colored("Please specify the difficulty level of the questions", color ="green"))
difficulty_questions = int(input("Easy = 1, Medium = 2, Hard = 3 : "))
score = 0

class Question:
    def __init__(self, question_text, option_1, option_2, option_3, option_4, right_option):
        self.question_text = question_text
        self.option_1 = option_1
        self.option_2 = option_2
        self.option_3 = option_3
        self.option_4 = option_4
        self.right_option = right_option

    def option(self):
        print("Question:",self.question_text)
        print("Option_1:",self.option_1)
        print("Option_2:",self.option_2)
        print("Option_3:",self.option_3)
        print("Option_4:",self.option_4)



question_1_1 = Question("What color is the sky?", "blue = 1", "red = 2", "green = 3", "pink = 4", 1)
question_1_2 = Question("What color are the trees?", "blue = 1", "red = 2", "green = 3", "pink = 4", 3)
question_1_3 = Question("What color is the sea? ", "blue = 1", "red = 2", "green = 3", "pink = 4", 1)

if difficulty_questions == 1:
    question_1_1.option()
    user_input_1 = int(input("What is the right option?: "))
    if user_input_1 == question_1_1.right_option:
        print(termcolor.colored("your win!!!", color="green"))
        score += 1
    else:
        print(termcolor.colored("yiur lost!!!", color= "red"))
        score -= 1
elif difficulty_questions == 2:
    pass
elif difficulty_questions == 3:
    pass

print("socore your", score)