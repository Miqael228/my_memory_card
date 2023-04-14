#создай приложение для запоминания информации
from random import shuffle
from random import randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton,QGroupBox,QButtonGroup

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

app = QApplication([])
main_win = QWidget()
main_win.resize(600, 400)
button = QPushButton('Ответить')
main_win.setWindowTitle('Memory Card')
lable = QLabel('Вопрос')
main_win.yesquest = 0
main_win.tasks = 0
main_win.status = 0
#Первый GroupBox(Вопрос)
RadioGroupBox = QGroupBox('Варианты ответов')
ans1 = QRadioButton('неправильно')
ans2 = QRadioButton('правильно')
ans3 = QRadioButton('неправильно')
ans4 = QRadioButton('неправильно')
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

answer = [ans1, ans2, ans3, ans4]



RadioGroup = QButtonGroup()
RadioGroup.addButton(ans1)
RadioGroup.addButton(ans2)
RadioGroup.addButton(ans3)
RadioGroup.addButton(ans4)



layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()


layout_ans2.addWidget(ans1)
layout_ans2.addWidget(ans2)
layout_ans3.addWidget(ans3)
layout_ans3.addWidget(ans4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)



#Второй GroupBox(ответ на 1 вопр.)
AnsGroupBox = QGroupBox('Результат теста')
que1 = QLabel('Правильно/Неправильно')
que2 = QLabel('Правельный ответ')

AnsGroupBox.hide()

layout_que = QVBoxLayout()
layout_que.addWidget(que1, alignment=(Qt.AlignLeft  |  Qt.AlignTop))
layout_que.addWidget(que2, alignment=(Qt.AlignHCenter  |  Qt.AlignVCenter), stretch=2)

AnsGroupBox.setLayout(layout_que)


layout_main = QVBoxLayout()

layout_line1.addWidget(lable, alignment=(Qt.AlignHCenter  |  Qt.AlignVCenter))

layout_line3.addStretch(1)
layout_line3.addWidget(button, stretch=2)
layout_line3.addStretch(1)


layout_line2.addWidget(RadioGroupBox, stretch=5)



layout_line2.addWidget(AnsGroupBox, stretch=5)



layout_main.addLayout(layout_line1, stretch=1)
layout_main.addLayout(layout_line2, stretch=4)
layout_main.addLayout(layout_line3, stretch=3)
layout_main.setSpacing(5)



def show_question():
    button.setText('Ответить')
    AnsGroupBox.hide()
    RadioGroupBox.show()
    RadioGroup.setExclusive(False)
    ans1.setChecked(False)
    ans2.setChecked(False)
    ans3.setChecked(False)
    ans4.setChecked(False)
    RadioGroup.setExclusive(True)



quest_l = list()
quest_l.append(Question('Государственный язык Бразилии', 'Португальский', 'Итальянский', 'Испанский', 'Бразильский'))
quest_l.append(Question('Какой национальности не существует?','Смурфы' ,'Энцы', 'Чулымцы', 'Алеуты'))
quest_l.append(Question('Выберете неподходящее слово', 'Машина', 'Дом', 'Магазин', 'Площадка'))
quest_l.append(Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
quest_l.append(Question('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата'))



def ask(q: Question):
    shuffle(answer)
    lable.setText(q.question)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    que2.setText(q.right_answer)
    show_question()


def check_answer():
    if answer[0].isChecked():
        show_correct('Правильно')
        main_win.yesquest += 1
        main_win.status = main_win.yesquest / main_win.tasks * 100
        print('Статистика')
        print('-Всего вопросов:', main_win.tasks)
        print('-Правильных ответов:', main_win.yesquest)
        qwqwe = randint(0, len(quest_l) - 1)
        print('Рейтинг:', main_win.status)
    else:
        show_correct('Неправильно')
        main_win.status = main_win.yesquest / main_win.tasks * 100
        print('Статистика')
        print('-Всего вопросов:', main_win.tasks)
        print('-Правильных ответов:', main_win.yesquest)
        qwqwe = randint(0, len(quest_l) - 1)
        print('Рейтинг:', main_win.status)
        


def next_question():
    main_win.tasks += 1
    print('Статистика')
    print('-Всего вопросов:', main_win.tasks)
    print('-Правильных ответов:', main_win.yesquest)
    qwqwe = randint(0, len(quest_l) - 1)
    ask(quest_l[qwqwe])

def show_correct(qwq):
    que1.setText(qwq)
    show_result()


def show_result():
    button.setText('Следующий вопрос')
    RadioGroupBox.hide()
    AnsGroupBox.show()


def click_ok():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()

next_question()

button.clicked.connect(click_ok)

main_win.setLayout(layout_main)
main_win.show()
app.exec_()