import customtkinter
from customtkinter import CTk, CTkFrame, CTkLabel, CTkEntry, CTkTextbox, CTkButton
import random
import time
import datetime






timer = None
time_running = False





customtkinter.set_default_color_theme("dark-blue")

def update_timer():
    if time_running:
            end_time = time.time()
            time_it_took = end_time - start_time
            delta = datetime.timedelta(seconds=time_it_took)
            minutes = delta.seconds // 60
            seconds = delta.seconds % 60
            elapsed_time_str = '{:02}:{:02}'.format(minutes, seconds)
            timer_label.configure(text=elapsed_time_str)
            timer_label.after(1000, update_timer)
def Start():

    with open('jeff.txt') as file:
        global start_time, time_running
        start_time = time.time()
        time_running = True

        lines = file.readlines()
        fake_phrase = []
        for _ in range(10):
            random_word = random.choice(lines).replace('\n', '')
            fake_phrase.append(random_word)

        global random_line
        random_line = ' '.join(fake_phrase).lower()

        label_text.configure(text=f'{random_line}')
        user_entry.delete('0.1', 'end')
        timer_label.configure(text='00:00', text_color='white')
        update_timer()



def EnterEvent(event):
    global time_running
    time_running = False
    end_time = time.time()
    time_it_took = end_time - start_time
    delta = datetime.timedelta(seconds=time_it_took)
    minutes = delta.seconds // 60
    seconds = delta.seconds % 60
    elapsed_time_str = '{:02}:{:02}'.format(minutes, seconds)
    timer_label.configure(text=f'{elapsed_time_str}')

    user_text = user_entry.get('1.0', 'end')
    print(user_text)
    user_entry.delete('1.0', 'end')

    phrase_as_list = [word for word in random_line.split()]
    user_text_as_list = [word for word in user_text.split()]
    wrong_words = []
    for index, word in enumerate(user_text_as_list, start=0):
        if word == phrase_as_list[index]:
            print(word)
            print(phrase_as_list[index])
            print('correct')
        elif word != phrase_as_list[index]:
            print(word)
            print(phrase_as_list[index])
            print('Wrong')
            wrong_words.append(word)

    if wrong_words:
        user_entry.insert('0.0',text=f'Words you got wrong{wrong_words}')
        timer_label.configure(text_color='red')
    else:
        timer_label.configure(text_color='green')






customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"



#setting teh app as the method for ctk
app = customtkinter.CTk()
# setting the size of the window
app.geometry('700x500')
#setting window title
app.title('Typing Test!')

app.bind('<Return>', EnterEvent)



frame = CTkFrame(master=app)
frame.pack(pady=20,  padx=10, fill="both", expand=True)


wrap_length = 600
label_text = CTkLabel(master=app, text=f'Press the fish to start!', wraplength=wrap_length, font=('Arial', 23, 'bold'))
label_text.place(relx=0.5, y=100, anchor="center")


user_entry = CTkTextbox(master=app, width=500, height=100, border_width=10, font=('Arial', 20, 'bold'))
user_entry.place(relx=0.5, y=280, anchor='center')


timer_label = CTkLabel(master=app, text=f'00:00', wraplength=wrap_length, font=('Arial', 23))
timer_label.place(relx=0.5, y=180, anchor="center")


button_start = CTkButton(master=app,text='<º))))><', command=Start, width=300, height=50, font=('Arial', 20, 'bold'))
button_start.place(relx=0.5, y=370, anchor='center')





app.mainloop()