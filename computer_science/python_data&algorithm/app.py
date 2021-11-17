from student import Student
from question import Question
student1 = Student('Mg Mg', 'Business', 3.1, False)
student2 = Student('Mg Hla', 'Art', 3.2, True)

print(student2.is_on_probation)
print()
print("_____________________________")

question_prompts = [
    "What color are apples?\n (a) Red/Green \n (b) Purple \n (c) Orange \n\n ",
    "What color are Bananas?\n (a) Teal \n (b) Magenta \n (c) Yellow\n\n",
    "What color are strawberries?\n (a) Yello \n (b) Red \n (c) Blue\n\n"

]


questions = [
    Question(question_prompts[0], 'a'),
    Question(question_prompts[1], 'c'),
    Question(question_prompts[2], 'b')

]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + '/' + str(len(questions)) + "correct")

run_test(questions)
