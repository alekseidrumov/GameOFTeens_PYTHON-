from tkinter import *
import ctypes



user32 = ctypes.windll.user32
n_widht = int(user32.GetSystemMetrics(0) / 2 +100)
n_height = int(user32.GetSystemMetrics(1) / 2 + 100)
widht = str(n_height)
height = str(n_widht)
root = Tk()
class Main:
    def __init__(self, widht,height,root):
        self.root = root
        self.widht = widht
        self.height = height
        self.num_of_question = 0
        self.answers1 = [2,4,1,3,3,2,1,1,4,2]
        self.answers2 = [1,2,4,4,1,2,4,1,1,4]
        self.answers3 = [4,4,3,4,2,4,1,4,1,3]
        self.score = 0
        self.otvet = 0
    def menu(self):
        try:
            self.score = 0
            self.num_of_question = 0
            self.score_lbl.destroy()
            self.menu_but.destroy()
            self.result_proz_lbl.destroy() 
            self.result_lbl.destroy()
        except:
            pass
        self.frame = Frame(self.root)
        self.frame.pack()
        self.root.title('Menu')
        self.root.geometry(widht+"x"+height)
        menutext = Label(self.frame,text='Тесты',bd=10,font=('Comfortaa',20))
        menutext.pack()
        info_btn = Button(self.frame,text="Описание",command=self.info,width=15, height=3,font=('Comfortaa',20))
        info_btn.pack(pady=30)
        test1_btn = Button(self.frame,text="Украинский язык",command=self.test1,width=15, height=3,font=('Comfortaa',20))
        test1_btn.pack(pady=30)
        test2_btn = Button(self.frame,text="Математика",command=self.test2,width=15, height=3,font=('Comfortaa',20))
        test2_btn.pack(pady=30)
        test3_btn = Button(self.frame,text="История",command=self.test3,width=15, height=3,font=('Comfortaa',20))
        test3_btn.pack(pady=30)
        self.root.mainloop()


    def info(self):
        view = Tk()
        text = Label(view,text="TestX Программа сделанная, \nдля тестирования по трём предметам. \nЧтобы выбрать тест, нажмите на \nкнопку с соответствующим предметом. \nВ одном тесте, 10 вопросов на \nкаждый вопрос 4 ответа. \nВсе вопросы были взяты отсюда:https://zno.osvita.ua/",font=('Comfortaa',30))
        text.pack()

    def test2(self):
        if self.num_of_question == 0:
            self.frame.destroy()
            self.t = Test2("15+x-2x^2",'15+x+2x^2','15+6x-2x^2','15+11x-2x^2','Укажіть выраз, тотожно \nрівний виразу (2x+5)•(3-x).',self.root,self)
            self.t.pack()
        elif self.num_of_question == 1:
            self.t.destroy()
            self.t = Test2("10^1,5",'10^2','10^8','10^9','Обчисліть 2^6•5^6/10^4',self.root,self)
            self.t.pack()
        elif self.num_of_question == 2:
            self.t.destroy()
            self.t = Test2("8 см^2",'16 см^2','36√2 см^2','24 см^22','Знайдіть площу повної поверхні куба, \nдіагональ якого дорівнює 2√3 см.',self.root,self)
            self.t.pack()
        elif self.num_of_question == 3:
            self.t.destroy()
            self.t = Test2("(-20;-10)",'(-10;-5)','(-5;5)','(5;10)','Укажіть проміжок, у якому належить корінь \nрівняння √1-x=4',self.root,self)
            self.t.pack()
        elif self.num_of_question == 4:
            self.t.destroy()
            self.t = Test2("y=4x",'y=x','y=√x','y=|x|','Укажіть парну функцію',self.root,self)
            self.t.pack()
        elif self.num_of_question == 5:
            self.t.destroy()
            self.t = Test2("m=6n",'m=6/n','m=2n/3','m=3/2n','Визначте m із співвідношення \nm/2=3/n де n≠0',self.root,self)
            self.t.pack()
        elif self.num_of_question == 6:
            self.t.destroy()
            self.t = Test2("-2,5;2",'-2','2,5','-2;2,5',"""Розв'яжіть рівняння 2x(x+2)=5(x+2).""",self.root,self)
            self.t.pack()
        elif self.num_of_question == 7:
            self.t.destroy()
            self.t = Test2("(-∞;5)",'(-∞;-5)','(-5;+∞)','5;+∞',"""Розв'яжіть нерівність 1/x-5<0.""",self.root,self)
            self.t.pack()
        elif self.num_of_question == 8:
            self.t.destroy()
            self.t = Test2("9",'11','4','-9',"Якщо x+2z-6z=-1 і -y+3z=5, то x = ",self.root,self)
            self.t.pack()
        elif self.num_of_question == 9:
            self.t.destroy()
            self.t = Test2("lg5",'5','lg20','2',"lg25/lg5=",self.root,self)
            self.t.pack()
        else:
            self.t.destroy()
            self.score_lbl = Label(self.root,text='Счет: '+str(self.score),font=('Comfortaa',20))
            self.score_lbl.pack(side=BOTTOM)
            self.menu_but = Button(self.root,text='Вернусться в меню',font=('Comfortaa',20),command=self.menu)
            self.menu_but.pack(side=BOTTOM)
            if self.score == 10:
                self.result_lbl = Label(self.root,text="\nТи готовий до тесту.\n Тепер є час на підготовку \nдо наступного предмету",font=('Comfortaa',20),justify=CENTER)
                self.result_lbl.pack()
                self.result_proz_lbl = Label(self.root,text='100% правильних відповідей.',font=('Comfortaa',20))
                self.result_proz_lbl.pack(pady=100)
            elif self.score > 6 and self.score < 10:
                self.result_lbl = Label(self.root,text="Ти майже дійшов до мети!\n Але потрібно ще готуватись.",font=('Comfortaa',20),justify=CENTER)
                self.result_lbl.pack()
                self.result_proz_lbl = Label(self.root,text='більше 80% правильних відповідей.',font=('Comfortaa',20))
                self.result_proz_lbl.pack(pady=100)
            else:
                self.result_lbl = Label(self.root,text="Схоже сьогодні не твій день. \nПриділи більше уваги підготовці \nі повертайся до тесту через деякий час",font=('Comfortaa',20),justify=CENTER)
                self.result_lbl.pack()
                self.result_proz_lbl = Label(self.root,text='менше 80% правильних відповідей',font=('Comfortaa',20))
                self.result_proz_lbl.pack(pady=100)


    def test1(self):
        if self.num_of_question == 0:
            self.frame.destroy()
            self.t = Test1('олень','колесо','читання','випадок','Правильно підкреслено літеру на \nпозначення наголошеного звука в слові',self.root,self)
            self.t.pack()
        elif self.num_of_question == 1:
            self.t.destroy()
            self.t = Test1('не/зовсім зрозумілий','зошит не/підписано','не/всі з цим обізнані','не/забутня подорож','Частку не треба писати разом у варіанті',self.root,self)
            self.t.pack()
        elif self.num_of_question == 2:
            self.t.destroy()
            self.t = Test1('плащ','читач','ситець','насіння','Суфікс -ов- має прикметник, \nутворений від іменника',self.root,self)
            self.t.pack()
        elif self.num_of_question == 3:
            self.t.destroy()
            self.t = Test1("""розв'язувати задачу""",'уникнути небезпеки','заказати букет квітів','перекладати болгарською','Суфікс -ов- має прикметник, \nПомилково вжито слово в рядку',self.root,self)
            self.t.pack()
        elif self.num_of_question == 4:
            self.t.destroy()
            self.t = Test1("пане Костянтине",'для всіх дослідників','восьмидесяти років','візьмімо участь','Неправильно утворено форму \nслова у варіанті',self.root,self)
            self.t.pack()
        elif self.num_of_question == 5:
            self.t.destroy()
            self.t = Test1("Жінки втомились бути непрекрасними.",'За правду, браття, єднаймось щиро.','Весна прийшла, та якось несподівано!','Шматок землі, ти звешся Україною.','Спонукальним є речення',self.root,self)
            self.t.pack()
        elif self.num_of_question == 6:
            self.t.destroy()
            self.t = Test1("п'ятниць, їстоньки, яблунька",'якість, кукурудза, український','''гайок, об'єднування, сьогодення''','серйозний, щебечуть, джміль','Однакова кількість звуків і букв \nу кожному слові рядка',self.root,self)
            self.t.pack()
        elif self.num_of_question == 7:
            self.t.destroy()
            self.t = Test1("Словник являється \nнадійним джерелом інформації.",'Камера схову розташована на першому поверсі.','Ялту вважають одним з найкращих курортів.','Директор банку перебуває за кордоном.','Виділене слово вжито в невластивому \nйому значенні в реченні',self.root,self)
            self.t.pack()
        elif self.num_of_question == 8:
            self.t.destroy()
            self.t = Test1('бездога..ий, страше..ий, студе..ий','свяще..ий, довгожда..ий, безіме..ий','невблага..ий, орли..ий, ешело..ий.','незбагне..ий, моното..ий, безці..ий','Подвоєне нн треба писати на місці \nпропуску в усіх словах рядка',self.root,self)
            self.t.pack()
        elif self.num_of_question == 9:
            self.t.destroy()
            self.t = Test1("верб..я, кур..йозний, тьм..яний",'моркв..яний, розз..явити, цв..яшок','дзв..якнути, ін..єкція, різдв..яний','дво..ярусний, різьб..яр, Лук..янович','Без апострофа треба \nписати всі слова в рядку',self.root,self)
            self.t.pack()
        else:
            self.t.destroy()
            self.score_lbl = Label(self.root,text='Счет: '+str(self.score),font=('Comfortaa',20))
            self.score_lbl.pack(side=BOTTOM)
            self.menu_but = Button(self.root,text='Вернусться в меню',font=('Comfortaa',20),command=self.menu)
            self.menu_but.pack(side=BOTTOM)
            if self.score == 10:
                self.result_lbl = Label(self.root,text="\nТи готовий до тесту.\n Тепер є час на підготовку \nдо наступного предмету",font=('Comfortaa',20),justify=CENTER)
                self.result_lbl.pack()
                self.result_proz_lbl = Label(self.root,text='100% правильних відповідей.',font=('Comfortaa',20))
                self.result_proz_lbl.pack(pady=100)
            elif self.score > 6 and self.score < 10:
                self.result_lbl = Label(self.root,text="Ти майже дійшов до мети!\n Але потрібно ще готуватись.",font=('Comfortaa',20),justify=CENTER)
                self.result_lbl.pack()
                self.result_proz_lbl = Label(self.root,text='більше 80% правильних відповідей.',font=('Comfortaa',20))
                self.result_proz_lbl.pack(pady=100)
            else:
                self.result_lbl = Label(self.root,text="Схоже сьогодні не твій день. \nПриділи більше уваги підготовці \nі повертайся до тесту через деякий час",font=('Comfortaa',20),justify=CENTER)
                self.result_lbl.pack()
                self.result_proz_lbl = Label(self.root,text='менше 80% правильних відповідей',font=('Comfortaa',20))
                self.result_proz_lbl.pack(pady=100)
        
    def test3(self):
        if self.num_of_question == 0:
            self.frame.destroy()
            self.t = Test3("палеоліту.",'мезоліту.','енеоліту.','неоліту.','Поява першого керамічного посуду \n- це характерна риса епохи',self.root,self)
            self.t.pack()
        elif self.num_of_question == 1:
            self.t.destroy()
            self.t = Test3("монголам.",'угорцям.','полякам.','хрестоносцям.','У 1238 р. під Дорогичином військо князя \nДанила Галицького завдало поразки',self.root,self)
            self.t.pack()
        elif self.num_of_question == 2:
            self.t.destroy()
            self.t = Test3("міщани",'бояри','смерди','дружинники','Яка соціальна верства становила \nпереважну більшість населення \nКиївської Русі IX–XII ст.?',self.root,self)
            self.t.pack()
        elif self.num_of_question == 3:
            self.t.destroy()
            self.t = Test3("козаків.",'селян.','міщан.','шляхти.','Фільварок — це форма господарювання',self.root,self)
            self.t.pack()
        elif self.num_of_question == 4:
            self.t.destroy()
            self.t = Test3("упорядкування системи \nуправління Запорозькою Січчю.",'ліквідацію решток \nавтономного устрою Гетьманщини.','запровадження полкового \nустрою в Слобідській Україні.','повернення козаків \nЗадунайської Січі на Запоріжжя.','Діяльність Другої Малоросійської \nколегії було спрямовано на',self.root,self)
            self.t.pack()
        elif self.num_of_question == 5:
            self.t.destroy()
            self.t = Test3("масонською ложею «Любов до істини».",'Кирило-Мефодіївським братством.','польським Патріотичним товариством.',"Південним товариством декабристів.",'Повстання Чернігівського \nполку наприкінці 1825 — \nна початку 1826 рр. було підготовлено',self.root,self)
            self.t.pack()
        elif self.num_of_question == 6:
            self.t.destroy()
            self.t = Test3("завершенню промислового перевороту.",'скасуванню заборон \nщодо української мови.','відкриттю українських \nкафедр в університетах.','зрівнянню в правах \nусіх верств суспільства.',"""Реформи \n1860–1870-х рр. у \nРосійській імперії сприяли""",self.root,self)
            self.t.pack()
        elif self.num_of_question == 7:
            self.t.destroy()
            self.t = Test3("1919 р.",'1920 р.','1921 р.','1922 р.',"""У якому році Українська \nСРР стала складовою СРСР?""",self.root,self)
            self.t.pack()
        elif self.num_of_question == 8:
            self.t.destroy()
            self.t = Test3("справи «Спілки визволення України»",'«Шахтинської справи»','Голодомору','«Закону про п’ять колосків»',"Жертвою якої репресивної \nакції став С. Єфремов?",self.root,self)
            self.t.pack()
        elif self.num_of_question == 9:
            self.t.destroy()
            self.t = Test3("6 листопада 1943 р.",'17 лютого 1944 р.','28 жовтня 1944 р.','9 травня 1945 р.',"Визволення всієї території \nУкраїни від німецьких \nокупантів та їхніх союзників відбулося",self.root,self)
            self.t.pack()
        else:
            self.t.destroy()
            self.score_lbl = Label(self.root,text='Счет: '+str(self.score),font=('Comfortaa',20))
            self.score_lbl.pack(side=BOTTOM)
            self.menu_but = Button(self.root,text='Вернусться в меню',font=('Comfortaa',20),command=self.menu)
            self.menu_but.pack(side=BOTTOM)
            if self.score == 10:
                self.result_lbl = Label(self.root,text="\nТи готовий до тесту.\n Тепер є час на підготовку \nдо наступного предмету",font=('Comfortaa',20),justify=CENTER)
                self.result_lbl.pack()
                self.result_proz_lbl = Label(self.root,text='100% правильних відповідей.',font=('Comfortaa',20))
                self.result_proz_lbl.pack(pady=100)
            elif self.score > 6 and self.score < 10:
                self.result_lbl = Label(self.root,text="Ти майже дійшов до мети!\n Але потрібно ще готуватись.",font=('Comfortaa',20),justify=CENTER)
                self.result_lbl.pack()
                self.result_proz_lbl = Label(self.root,text='більше 80% правильних відповідей.',font=('Comfortaa',20))
                self.result_proz_lbl.pack(pady=100)
            else:
                self.result_lbl = Label(self.root,text="Схоже сьогодні не твій день. \nПриділи більше уваги підготовці \nі повертайся до тесту через деякий час",font=('Comfortaa',20),justify=CENTER)
                self.result_lbl.pack()
                self.result_proz_lbl = Label(self.root,text='менше 80% правильних відповідей',font=('Comfortaa',20))
                self.result_proz_lbl.pack(pady=100)
       
            
        
   
    def save1(self):
        self.otvet = 1
        self.num_of_question = self.num_of_question + 1
        if self.answers1[self.num_of_question -1] == self.otvet:
            self.score = self.score + 1
        self.test1()
        
    def save2(self):
        self.otvet = 2
        self.num_of_question = self.num_of_question + 1
        if self.answers1[self.num_of_question -1] == self.otvet:
            self.score = self.score + 1
        self.test1()
    def save3(self):
        self.num_of_question = self.num_of_question + 1
        self.otvet = 3
        if self.answers1[self.num_of_question -1] == self.otvet:
            self.score = self.score + 1
        self.test1()
    def save4(self):
        self.num_of_question = self.num_of_question + 1
        self.otvet = 4
        if self.answers1[self.num_of_question -1] == self.otvet:
            self.score = self.score + 1
        self.test1()

    def save1_2(self):
        self.otvet = 1
        self.num_of_question = self.num_of_question + 1
        if self.answers2[self.num_of_question -1] == self.otvet:
            self.score = self.score + 1
        self.test2()
    def save2_2(self):
        self.otvet = 2
        self.num_of_question = self.num_of_question + 1
        if self.answers2[self.num_of_question -1] == self.otvet:
            self.score = self.score + 1
        self.test2()
    def save3_2(self):
        self.num_of_question = self.num_of_question + 1
        self.otvet = 3
        if self.answers2[self.num_of_question -1] == self.otvet:
            self.score = self.score + 1
        self.test2()
    def save4_2(self):
        self.num_of_question = self.num_of_question + 1
        self.otvet = 4
        if self.answers2[self.num_of_question -1] == self.otvet:
            self.score = self.score + 1
        self.test2()

    
    def save1_3(self):
        self.otvet = 1
        self.num_of_question = self.num_of_question + 1
        if self.answers3[self.num_of_question -1] == self.otvet:
            self.score = self.score + 1
        self.test3()
    def save2_3(self):
        self.otvet = 2
        self.num_of_question = self.num_of_question + 1
        if self.answers3[self.num_of_question -1] == self.otvet:
            self.score = self.score + 1
        self.test3()
    def save3_3(self):
        self.num_of_question = self.num_of_question + 1
        self.otvet = 3
        if self.answers3[self.num_of_question -1] == self.otvet:
            self.score = self.score + 1
        self.test3()
    def save4_3(self):
        self.num_of_question = self.num_of_question + 1
        self.otvet = 4
        if self.answers3[self.num_of_question -1] == self.otvet:
            self.score = self.score + 1
        self.test3()
        

class Test3:
    def __init__(self, answer1, answer2, answer3,answer4,question,root,zvidk):
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4
        self.question = question
        self.root = root
        self.zvidk = zvidk

    def add(self):
        self.zvidk.num_of_question = self.zvidk.num_of_question + 1 
    def pack(self):
        self.question_l = Label(self.root,text=self.question,font=('Comfortaa',20),justify=CENTER)
        self.question_l.pack(side=TOP)
        self.answer1_b = Button(self.root,text=self.answer1,font=('Comfortaa',20),command=self.zvidk.save1_3)
        self.answer1_b.pack(pady=50)
        self.answer2_b = Button(self.root,text=self.answer2,font=('Comfortaa',20),command=self.zvidk.save2_3)
        self.answer2_b.pack(pady=50)
        self.answer3_b = Button(self.root,text=self.answer3,font=('Comfortaa',20),command=self.zvidk.save3_3)
        self.answer3_b.pack(pady=50)
        self.answer4_b = Button(self.root,text=self.answer4,font=('Comfortaa',20),command=self.zvidk.save4_3)
        self.answer4_b.pack(pady=50)
        self.num_of_question_l = Label(self.root,text=str(self.zvidk.num_of_question + 1)+'/10')
        self.num_of_question_l.pack(side=BOTTOM)
        
    def destroy(self):
        self.question_l.destroy()
        self.answer1_b.destroy()
        self.answer2_b.destroy()
        self.answer3_b.destroy()
        self.answer4_b.destroy()
        self.num_of_question_l.destroy()



class Test1:
    def __init__(self, answer1, answer2, answer3,answer4,question,root,zvidk):
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4
        self.question = question
        self.root = root
        self.zvidk = zvidk

    def add(self):
        self.zvidk.num_of_question = self.zvidk.num_of_question + 1 
    def pack(self):
        self.question_l = Label(self.root,text=self.question,font=('Comfortaa',20),justify=CENTER)
        self.question_l.pack(side=TOP)
        self.answer1_b = Button(self.root,text=self.answer1,font=('Comfortaa',20),command=self.zvidk.save1)
        self.answer1_b.pack(pady=50)
        self.answer2_b = Button(self.root,text=self.answer2,font=('Comfortaa',20),command=self.zvidk.save2)
        self.answer2_b.pack(pady=50)
        self.answer3_b = Button(self.root,text=self.answer3,font=('Comfortaa',20),command=self.zvidk.save3)
        self.answer3_b.pack(pady=50)
        self.answer4_b = Button(self.root,text=self.answer4,font=('Comfortaa',20),command=self.zvidk.save4)
        self.answer4_b.pack(pady=50)
        self.num_of_question_l = Label(self.root,text=str(self.zvidk.num_of_question + 1)+'/10')
        self.num_of_question_l.pack(side=BOTTOM)
        
    def destroy(self):
        self.question_l.destroy()
        self.answer1_b.destroy()
        self.answer2_b.destroy()
        self.answer3_b.destroy()
        self.answer4_b.destroy()
        self.num_of_question_l.destroy()
    
class Test2:
    def __init__(self, answer1, answer2, answer3,answer4,question,root,zvidk):
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4
        self.question = question
        self.root = root
        self.zvidk = zvidk

    def add(self):
        self.zvidk.num_of_question = self.zvidk.num_of_question + 1 
    def pack(self):
        self.question_l = Label(self.root,text=self.question,font=('Comfortaa',20),justify=CENTER)
        self.question_l.pack(side=TOP)
        self.answer1_b = Button(self.root,text=self.answer1,font=('Comfortaa',20),command=self.zvidk.save1_2)
        self.answer1_b.pack(pady=50)
        self.answer2_b = Button(self.root,text=self.answer2,font=('Comfortaa',20),command=self.zvidk.save2_2)
        self.answer2_b.pack(pady=50)
        self.answer3_b = Button(self.root,text=self.answer3,font=('Comfortaa',20),command=self.zvidk.save3_2)
        self.answer3_b.pack(pady=50)
        self.answer4_b = Button(self.root,text=self.answer4,font=('Comfortaa',20),command=self.zvidk.save4_2)
        self.answer4_b.pack(pady=50)
        self.num_of_question_l = Label(self.root,text=str(self.zvidk.num_of_question + 1)+'/10')
        self.num_of_question_l.pack(side=BOTTOM)
            
    def destroy(self):
        self.question_l.destroy()
        self.answer1_b.destroy()
        self.answer2_b.destroy()
        self.answer3_b.destroy()
        self.answer4_b.destroy()
        self.num_of_question_l.destroy()
        

m = Main(widht,height,root)
m.menu()