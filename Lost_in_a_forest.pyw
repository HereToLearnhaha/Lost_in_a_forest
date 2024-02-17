from tkinter import *

questions = [
    'You encounter a little girl in a cage.',
    'You stumble upon a clearing, a fancy manor can be seen.',
    'While exploring the manor, you encounter a an orge.',
    'You take the key from the orge\'s body. Mabye it can open the girl\'s cage.',
    'You see a menacing humanoid creature in a tuxeso. He\'s power walking towards you with killing intent',
    'All of a sudden- a man in full iron armor slays the creature from behind',
    'The man wants to join you to escape the forest. He introduces himself as Igor',
    'Igor knows the way to escape so you follow him. It\'s the way you originally came from',
    'There, you find the girl and you set her free upon Igor\'s request',
    'Igor turns out to be a child killer and he tries to swing the sword at the girl'
]

options = [
    ['Oh no!', 'damn..','LMAO'],
    ['Enter from a window','Enter through the backdoor','FRONT DOOR'],
    ['Kill it swiftly with a sword','Throw a rock at his head','BURN HIM'],
    ['I should free her','I should focus on escape first','NAHH'],
    ['I should run','Maybe he\'s friendly?','I CAN KILL HIM'],
    ['Thank you','Who are you?','I DONT NEED YOUR HELP'],
    ['Hi Igor','How can I trust you?','FUCK YOU IGOR'],
    ['I trust him I guess','I dont trust him','I\'ll remain cautious'],
    ['Yay!','Meh..','Nay!'],
    ['Sacrifice yourself for her','Stand and watch','Help the man kill her']
]

answers = [
    1,
    1,
    1,
    1,
    1,
    1,
    2,
    3,
    1,
    1
]

ending1 = 'You passed. Yay!!! Sooo go to haven, orrrrr.. (Ending-1)'
ending2 = 'Well, you were all over the place but you passed. Kind of an asshole buttt.. meh. (Ending-2)'
ending3 = 'I gotta say, you are quite the twisted individual. Take it as a compliment I guess. (Ending-3)'
Shittiest_ending = 'WHAATTT THE ACTUAL FUCK IS WRONG WITH YOU? *Sigh* you know what? hell. Straight to hell (Shittiest ending)'

karma = 0
karma1 = 0
karma2 = 0
karma3 = 0
karma4 = 0
karma5 = 0
karma6 = 0
karma7 = 0
karma8 = 0
karma9 = 0
karma10 =0

def again():
    label_Start.configure(text = 'You wake up again in the same place....' ,font = ('Comic Sans MS', 20,'bold'))
    quit.place_forget()
    reincarnation.place_forget()
    die.place_forget()
    start_button.configure(text = 'Start again?')
    start_button.place(relx = 0.5, rely = 0.5, anchor = CENTER)

def qn_1():
    global karma1
    start_button.place_forget()
    label_Start.configure(text = questions[0])
    
    Q1_1.place(relx=0.5,rely=0.3,anchor = CENTER)
    Q1_2.place(relx=0.5,rely=0.5,anchor = CENTER)
    Q1_3.place(relx=0.5,rely=0.7,anchor = CENTER)
    
def qn_2(ans1):
    global karma1
    label_Start.configure(text = questions[1])
    Q1_1.place_forget()
    Q1_2.place_forget()
    Q1_3.place_forget()
    
    Q2_1.place(relx=0.5,rely=0.3,anchor = CENTER)
    Q2_2.place(relx=0.5,rely=0.5,anchor = CENTER)
    Q2_3.place(relx=0.5,rely=0.7,anchor = CENTER)
    
    if ans1 == answers[0]:
        karma1 += 1
    elif ans1 != answers[0]:
        karma1 -= 0.2 

def qn_3(ans2):
    global karma2  
    label_Start.configure(text = questions[2])
    Q2_1.place_forget()
    Q2_2.place_forget()
    Q2_3.place_forget()
    
    Q3_1.place(relx=0.5,rely=0.3,anchor = CENTER)
    Q3_2.place(relx=0.5,rely=0.5,anchor = CENTER)
    Q3_3.place(relx=0.5,rely=0.7,anchor = CENTER)
    
    if ans2== answers[1]:
        karma2+= 1
    elif ans2!= answers[1]:
        karma2-= 0.4

def qn_4(ans3):
  global karma3
  label_Start.configure(text = questions[3])
  Q3_1.place_forget()
  Q3_2.place_forget()
  Q3_3.place_forget()
  
  Q4_1.place(relx=0.5,rely=0.3,anchor = CENTER)
  Q4_2.place(relx=0.5,rely=0.5,anchor = CENTER)
  Q4_3.place(relx=0.5,rely=0.7,anchor = CENTER)
  
  
  if ans3 == answers[2]:
        karma3 += 1
  elif ans3 != answers[2]:
        karma3 -= 0.4
          
def qn_5(ans4):
    global karma4
    label_Start.configure(text = questions[4])
    Q4_1.place_forget()
    Q4_2.place_forget()
    Q4_3.place_forget()
    
    Q5_1.place(relx=0.5,rely=0.3,anchor = CENTER)
    Q5_2.place(relx=0.5,rely=0.5,anchor = CENTER)
    Q5_3.place(relx=0.5,rely=0.7,anchor = CENTER)
    
    if ans4 == answers[3]:
        karma4 += 1
    elif ans4 != answers[3]:
        karma4 -= 0.4
        
def qn_6(ans5):
    global karma5
    label_Start.configure(text = questions[5])
    if ans5 == answers[4]:
        karma5 += 1
    elif ans5 != answers[4]:
        karma5 -= 0.4
        
    Q5_1.place_forget()
    Q5_2.place_forget()
    Q5_3.place_forget()
    
    Q6_1.place(relx=0.5,rely=0.3,anchor = CENTER)
    Q6_2.place(relx=0.5,rely=0.5,anchor = CENTER)
    Q6_3.place(relx=0.5,rely=0.7,anchor = CENTER)
        
def qn_7(ans6):
    global karma6
    label_Start.configure(text = questions[6])
    if ans6 == answers[5]:
        karma6 += 1
    elif ans6 != answers[5]:
        karma6 -= 0.4
        
    Q6_1.place_forget()
    Q6_2.place_forget()
    Q6_3.place_forget()
    
    Q7_1.place(relx=0.5,rely=0.3,anchor = CENTER)
    Q7_2.place(relx=0.5,rely=0.5,anchor = CENTER)
    Q7_3.place(relx=0.5,rely=0.7,anchor = CENTER)
           
def qn_8(ans7):
    global karma7
    label_Start.configure(text = questions[7])
    if ans7 == answers[6]:
        karma7 += 1
    elif ans7 != answers[6]:
        karma7 -= 0.4
        
    Q7_1.place_forget()
    Q7_2.place_forget()
    Q7_3.place_forget()
    
    Q8_1.place(relx=0.5,rely=0.3,anchor = CENTER)
    Q8_2.place(relx=0.5,rely=0.5,anchor = CENTER)
    Q8_3.place(relx=0.5,rely=0.7,anchor = CENTER)
        
def qn_9(ans8):
    global karma8
    label_Start.configure(text = questions[8])
    if ans8 == answers[7]:
        karma8 += 1
    elif ans8 != answers[7]:
        karma8 -= 0.4
        
    Q8_1.place_forget()
    Q8_2.place_forget()
    Q8_3.place_forget()
    
    Q9_1.place(relx=0.5,rely=0.3,anchor = CENTER)
    Q9_2.place(relx=0.5,rely=0.5,anchor = CENTER)
    Q9_3.place(relx=0.5,rely=0.7,anchor = CENTER)
    
def qn_10(ans9):
    global karma9
    label_Start.configure(text = questions[9])
    if ans9 == answers[8]:
        karma9 += 1
    elif ans9 != answers[8]:
        karma9 -= 0.4
        
    Q9_1.place_forget()
    Q9_2.place_forget()
    Q9_3.place_forget()
    
    Q10_1.place(relx=0.5,rely=0.3,anchor = CENTER)
    Q10_2.place(relx=0.5,rely=0.5,anchor = CENTER)
    Q10_3.place(relx=0.5,rely=0.7,anchor = CENTER)
    
def ending(ans10):
    global karma,karma1,karma2,karma3,karma4,karma5,karma6,karma7,karma8,karma9,karma10
    
    karma = karma1 +karma2 + karma3 + karma4 + karma5 + karma6 + karma7 + karma8 + karma9 + karma10
    
    if ans10 == answers[9]:
        karma10 += 1
    elif ans10 != answers[9]:
        karma10 -= 1
    
    Q10_1.place_forget()
    Q10_2.place_forget()
    Q10_3.place_forget()
    
    
    if karma >= 8:
        label_Start.configure(text ='Annnndddd Simulation overr! ' + ending1,font = ('Comic Sans MS', 12,'bold'))
    elif karma >=5 and karma < 8:
        label_Start.configure(text = 'Alriiighttt, Simulation over. ' + ending2)
    elif karma <5 and karma >=1 :
        label_Start.configure(text = 'Okayyyyy cut. '+ ending3,font = ('Comic Sans MS', 12,'bold'))
    elif karma < 1:
        label_Start.configure(text = 'CUT- I SAID CUT! '+ Shittiest_ending, font = ('Comic Sans MS', 12,'bold'))
        
        
    Q5_1.place_forget()
    Q5_2.place_forget()
    Q5_3.place_forget()
    
    quit.place(relx = 0.5, rely = 0.3, anchor= CENTER)
    reincarnation.place(relx=0.5,rely=0.5, anchor = CENTER)
    die.place(relx = 0.5, rely = 0.7, anchor = CENTER)
    
def exit_game():
    window.destroy()

window = Tk()
window.geometry('600x580')
window.title('THE ULTIMATE GAME')

Questions = Frame()
label_Start = Label(Questions, text = "You wake up in a dense forest. Before you lies a paved path.....", font = ('Comic Sans MS',18,'bold'))
start_button = Button(text = 'Start walking', bg = 'red', font = ('Comic Sans MS',20,'bold'), width = 15, command= qn_1)
quit = Button(text= 'Thank you', bg = 'red', font = ('Comic Sans MS', 20, 'bold'), command = exit_game)
reincarnation = Button(text= 'Reincarnate me!', bg = 'red', font = ('Comic Sans MS', 20, 'bold'), command = again)
die = Button(text= 'Ive had enough!', bg = 'red', font = ('Comic Sans MS', 20, 'bold'), command = exit_game)

Q1_1= Button(text = options[0][0], width = 25, font = ('Comic Sans MS', 20, 'bold'), bg = 'blue',command=lambda: qn_2(1))
Q1_2= Button(text = options[0][1], width = 25, font = ('Comic Sans MS', 20, 'bold'), bg = 'blue',command=lambda: qn_2(2))
Q1_3= Button(text = options[0][2], width = 25, font = ('Comic Sans MS', 20, 'bold'), bg = 'blue',command=lambda: qn_2(3))

Q2_1= Button(text = options[1][0], width = 25, font = ('Comic Sans MS', 20, 'bold'), bg = 'green',command=lambda: qn_3(1))
Q2_2= Button(text = options[1][1], width = 25, font = ('Comic Sans MS', 20, 'bold'), bg = 'green',command=lambda: qn_3(2))
Q2_3= Button(text = options[1][2], width = 25, font = ('Comic Sans MS', 20, 'bold'), bg = 'green',command=lambda: qn_3(3))

Q3_1= Button(text = options[2][0], width = 25, font = ('Comic Sans MS', 20, 'bold'), bg = 'yellow',command=lambda: qn_4(1))
Q3_2= Button(text = options[2][1], width = 25, font = ('Comic Sans MS', 20, 'bold'), bg = 'yellow',command=lambda: qn_4(2))
Q3_3= Button(text = options[2][2], width = 25, font = ('Comic Sans MS', 20, 'bold'), bg = 'yellow',command=lambda: qn_4(3))

Q4_1= Button(text = options[3][0], width = 25, font = ('Comic Sans MS', 20, 'bold'), bg = 'pink',command=lambda: qn_5(1))
Q4_2= Button(text = options[3][1], width = 25, font = ('Comic Sans MS', 20, 'bold'), bg = 'pink',command=lambda: qn_5(2))
Q4_3= Button(text = options[3][2], width = 25, font = ('Comic Sans MS', 20, 'bold'), bg = 'pink',command=lambda: qn_5(3))

Q5_1= Button(text = options[4][0], width = 25, font = ('Comic Sans MS', 20, 'bold'), bg = 'orange',command= lambda: qn_6(1))
Q5_2= Button(text = options[4][1], width = 25, font = ('Comic Sans MS', 20, 'bold'), bg = 'orange',command= lambda: qn_6(2))
Q5_3= Button(text = options[4][2], width = 25, font = ('Comic Sans MS', 20, 'bold'), bg = 'orange',command= lambda: qn_6(3))

Q6_1= Button(text = options[5][0], width = 25, font = ('Comic Sans MS', 20, 'bold'), bg = 'blue',command= lambda: qn_7(1))
Q6_2= Button(text = options[5][1], width = 25, font = ('Comic Sans MS', 20, 'bold'), bg = 'blue',command= lambda: qn_7(2))
Q6_3= Button(text = options[5][2], width = 25, font = ('Comic Sans MS', 20, 'bold'), bg = 'blue',command= lambda: qn_7(3))

Q7_1= Button(text = options[6][0], width = 25, font = ('Comic Sans MS', 20, 'bold'), bg = 'green',command= lambda: qn_8(1))
Q7_2= Button(text = options[6][1], width = 25, font = ('Comic Sans MS', 20, 'bold'), bg = 'green',command= lambda: qn_8(2))
Q7_3= Button(text = options[6][2], width = 25, font = ('Comic Sans MS', 20, 'bold'), bg = 'green',command= lambda: qn_8(3))

Q8_1= Button(text = options[7][0], width = 25, font = ('Comic Sans MS', 20, 'bold'), bg = 'yellow',command= lambda: qn_9(1))
Q8_2= Button(text = options[7][1], width = 25, font = ('Comic Sans MS', 20, 'bold'), bg = 'yellow',command= lambda: qn_9(2))
Q8_3= Button(text = options[7][2], width = 25, font = ('Comic Sans MS', 20, 'bold'), bg = 'yellow',command= lambda: qn_9(3))

Q9_1= Button(text = options[8][0], width = 25, font = ('Comic Sans MS', 20, 'bold'), bg = 'orange',command= lambda: qn_10(1))
Q9_2= Button(text = options[8][1], width = 25, font = ('Comic Sans MS', 20, 'bold'), bg = 'orange',command= lambda: qn_10(2))
Q9_3= Button(text = options[8][2], width = 25, font = ('Comic Sans MS', 20, 'bold'), bg = 'orange',command= lambda: qn_10(3))

Q10_1= Button(text = options[9][0], width = 25, font = ('Comic Sans MS', 20, 'bold'), bg = 'blue',command=lambda: ending(1))
Q10_2= Button(text = options[9][1], width = 25, font = ('Comic Sans MS', 20, 'bold'), bg = 'blue',command=lambda:ending(2))
Q10_3= Button(text = options[9][2], width = 25, font = ('Comic Sans MS', 20, 'bold'), bg = 'blue',command=lambda:ending(3))

Q1_1.place_forget()
Q1_2.place_forget()
Q1_3.place_forget()

Q2_1.place_forget()
Q2_2.place_forget()
Q2_3.place_forget()

Q3_1.place_forget()
Q3_2.place_forget()
Q3_3.place_forget()

Q4_1.place_forget()
Q4_2.place_forget()
Q4_3.place_forget()

Q5_1.place_forget()
Q5_2.place_forget()
Q5_3.place_forget()

Q6_1.place_forget()
Q6_2.place_forget()
Q6_3.place_forget()

Q7_1.place_forget()
Q7_2.place_forget()
Q7_3.place_forget()

Q8_1.place_forget()
Q8_2.place_forget()
Q8_3.place_forget()

Q9_1.place_forget()
Q9_2.place_forget()
Q9_3.place_forget()

Q10_1.place_forget()
Q10_2.place_forget()
Q10_3.place_forget()
    
Questions.pack()
label_Start.pack()
start_button.place(relx = 0.5,rely=0.5, anchor = CENTER)
quit.place_forget()
reincarnation.place_forget()
die.place_forget()
window.mainloop()