from tkinter import *
import tkinter.font
import csv
import functools as fct


w=Tk()
w.title("자리배치")
w.geometry("1000x750+200+200")
w.resizable(True,True)

message_font = tkinter.font.Font(weight='bold') #글꼴설정



data_button = list() #버튼 담을 리스트 생성
data_tlabely = list() #자리 배치에서 y좌표를 위한 함수
data_tlabelx = list() #자리 배치에서 x좌표를 위한 함수
data_func = list(range(1,31)) 
st_name = []
message_start = """오른쪽 화면 커서에다 학생들의 이름이 적힌
Excel파일명을 입력하십시오.
O버튼은 자리배치에 포함되고
X버튼은 포함되지 않습니다.
"""

message_error = """해당 파일을 찾을 수 없습니다.
python과 같은 폴더에 있거나
파일이름이 틀리지 않았는지 확인해 주십시오."""

message_okay = """해당 파일을 찾았습니다!
시작 버튼을 누르면
자리바꾸기를 실행합니다."""


frame1=Frame(w, relief="solid", bd=3)
frame2=Frame(w, relief="solid", bd=3)

st_list=  []
for i in range(30) :
    st_list.append(int(1))

#버튼이 클릭 되었을때 버튼의 ox를 바꿔주는 함수
def ch_ox(k) :
    if  st_list[k] == 1 :
        st_list[k] = 0
        data_button[k]["text"] = 'X'
        
    else :
        st_list[k]= 1
        data_button[k]["text"] = 'O'


#파일이름이 입력되었을때 파일 여는 함수
def file_open(event) :
    global fn
    st_n = int(0)
    fn = ans.get()
    try :
        with open(fn+".csv", 'r',encoding='cp949') as f :
            data = csv.reader(f)
            for line in data :
                if line[0] == '' :
                    continue
                
                st_name.append(str(line[0]))
        message["text"] = message_okay
        
                
    except :
        message["text"] = message_error



#무작위 자리배치 해주는 함수      
def ch_stname() :
    import random as r
    import copy 

    pr_note = copy.copy(st_name)
    r.shuffle(pr_note)

    
    for i in range(0,30) :
        try : 
            if st_list[i] == 1 :
                st = r.choice(pr_note)
                data_button[i]["text"] = st
                pr_note.remove(st)
                
            elif st_list[i] == 0 :
                data_button[i]["text"] = ""
        except IndexError :
            t = data_button[i]["text"]
            if t == 'O' or 'X' :
                data_button[i]["text"] = ' '

    




t = int(0)
#버튼 30개를 리스트에다 담기
for i in range(6) :
    for j in range(5) :
        t += 1
        call_ch_ox = fct.partial(ch_ox,t-1)
        data_button.append(Button(frame1,text=str('O'),width = 5,height = 2,
                                  command = call_ch_ox, font = message_font))
        data_button[t-1].grid(row = i * 3, column = j*3)


#학생들 이름 적힌 파일명 입력받는 커서 만들기        
ans = Entry(frame2, width=35, font=message_font)
ans.focus()
ans.bind('<Return>', file_open)
ans.pack()

message = Label(frame2,text=message_start,width = 35, font=message_font)
message.pack()

start = Button(frame2, text = "시작",width=4,height=2,command = ch_stname, font = message_font)
start.pack()

frame1.pack(side="left",fill="both",expand=True,padx=3,pady=3)
frame2.pack(side="left",fill="both",expand=True,padx=3,pady=3)

w.mainloop()
