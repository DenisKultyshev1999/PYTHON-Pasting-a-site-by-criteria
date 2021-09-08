"""
Напишите приложение, которое будет отправлять поисковой запрос на api.stackexchange.com и отображать полученные данные в любом удобном вам виде.
Пример запроса: (https://api.stackexchange.com/docs/search#order=desc&sort=activity&intitle=beautiful&filter=default&site=stackoverflow&run=true)
Данные необходимо сохранять на жестком диске любым удобным для вас образом (файл, база данных, итд).

"""

from tkinter import *
import requests
from tkinter import ttk
import json

def Stack():

    page=page_number.get()     #page number for reference
    if len(page)!=0:
        str1='page='+page+'&'   
    else:
        str1=''

    order=field_order.get()    #order for reference
    if len(order)==4:
        str2='desc'
    else:
        str2='asc'
    
    tagged=input_tagged.get()    #tagged for reference
    if len(tagged)==0:
        str3=''
    else:
        str3='tagged='+tagged+'&'



    link='https://api.stackexchange.com/2.3/search?'+str1+'order='+str2+'&sort=activity&'+str3+'intitle=beautiful&site=stackoverflow'  #reference


    response = requests.get(link)
    todos = json.loads(response.text)
 


    with open('data.json', 'w') as f:
         json.dump(todos, f)

    l1 = Label(text=todos)  #text pane output
    l1.pack()

    l3 = Label(text=link)  #text pane output
    l3.pack()




root = Tk ()                      #window          
root.geometry("500x500")
root.title("Stack Overflow")


text_page = Label(text="Page(1-999)")  #page number
page_number = Entry()
text_page.pack()
page_number.pack()


text_order = Label(text="Order(default desc)")        #order
field_order = ttk.Combobox(root,values=["desc", "asc"])
text_order.pack()
field_order.pack()

text_tagged=Label(text="Tagged")    #tagged
input_tagged = Entry()
text_tagged.pack()
input_tagged.pack()


button_test = Button(text="Run", command=Stack)   #button
button_test.pack()

tx = Text(root, width=40, height=6, font='14')
scr = Scrollbar(root, command=tx.yview)
tx.configure(yscrollcommand=scr.set)
tx.grid(row=0, column=0)
scr.grid(row=0, column=1)

root.mainloop()