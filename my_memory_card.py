#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QGroupBox, QButtonGroup)
from random import shuffle
class Question():
    def __init__(self, question, right_answer, wrohg1, wrohg2, wrohg3):
        self.question = question
        self.right_answer = right_answer
        self.wrohg1 = wrohg1
        self.wrohg2 = wrohg2
        self.wrohg3 = wrohg3

question_list = []
question_1 =  Question('Сколько будет 70*12?', '840', '910', '740', '940')
question_list.append(question_1)

question_2 =  Question('Как переводится World?', 'Мир', 'Земля', 'Природа', 'Растение')
question_list.append(question_2)

question_3 =  Question('В каком году СССР?', '1922-1991гг.', '1932-1943гг.', '1932-1987гг.', '1934-1991гг.')
question_list.append(question_3)


app = QApplication([])
window = QWidget()



window.setWindowTitle('Memory Card')
window.move(0, 0)
window.resize(500, 400)
lb_Question = QLabel('Какой национальности не существует?')
RadioGroupBox=QGroupBox('Варианты ответов')

qrbutton1 = QRadioButton('Энцы')
qrbutton2 = QRadioButton('Смурфы')
qrbutton3 = QRadioButton('Чулымцы')
qrbutton4 = QRadioButton('Алеуты')

layout_ans1=QVBoxLayout()
layout_ans2=QVBoxLayout()
layout_ans3=QHBoxLayout()

layout_ans1.addWidget(qrbutton1) # два ответа в первый столбец
layout_ans1.addWidget(qrbutton2)
layout_ans2.addWidget(qrbutton3) # два ответа во второй столбец
layout_ans2.addWidget(qrbutton4)

layout_ans3.addLayout(layout_ans1)
layout_ans3.addLayout(layout_ans2)

RadioGroupBox.setLayout(layout_ans3)

AnGroupBox = QGroupBox('Результаты теста')
lb_result = QLabel('прав ты или нет?')
lb_correct = QLabel('ответ будет тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_result)
layout_res.addWidget(lb_correct)
RadioGroupBox.setLayout(layout_res)

button_ok = QPushButton('Ответить')

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_card = QVBoxLayout()

layout_line1.addWidget(lb_Question)
layout_line2.addWidget(RadioGroupBox)  
layout_line2.addWidget(AnGroupBox)  
AnGroupBox.hide()

layout_line3.addWidget(button_ok)
layout_card.addLayout(layout_line1)
layout_card.addLayout(layout_line2)
layout_card.addLayout(layout_line3)

window.setLayout(layout_card)

def show_result():
    AnGroupBox.hide()
    RadioGroupBox.show()
    button_ok.setText('Следующий вопрос')
    print('Процент правильных ответов', scores/vopros * 100)

def show_question():
    AnGroupBox.hide()
    RadioGroupBox.show()
    button_ok.setText('Ответить')
    button_group = QButtonGroup()
    button_group.addButton(qrbutton1)
    button_group.addButton(qrbutton2)
    button_group.addButton(qrbutton3)
    button_group.addButton(qrbutton4)

    button_group.setExclusive(False)
    qrbutton1.setChecked(False)
    qrbutton2.setChecked(False)
    qrbutton3.setChecked(False)
    qrbutton4.setChecked(False)
    button_group.setExclusive(True)

answers = [qrbutton1, qrbutton2, qrbutton3, qrbutton4]
shuffle(question_list)
def ask():
    global vopros
    vopros += 1

    shuffle(question_list)
    ask_question =  question_list[0]

    shuffle(answers)
    answers[0].setText(ask_question.right_answer)
    answers[1].setText(ask_question.wrohg1)
    answers[2].setText(ask_question.wrohg2)
    answers[3].setText(ask_question.wrohg3)

    lb_Question.setText(ask_question.question)
    lb_correct.setText(ask_question.right_answer)

    show_question()

def check_answer():
    if answers[0].isChecked():
        global scores
        scores+=1
        
        lb_result.setText('Правильно')
        show_result()

    if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        lb_result.setText('Неверно')
        show_result()

def click_ok():
    if button_ok.text() == 'Ответить':
        check_answer()

    else:
        ask()

scores = 0
vopros = 0

ask()
button_ok.clicked.connect(click_ok)
window.show()
app.exec()