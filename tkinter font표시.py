import tkinter as tk
import tkinter.font as tkFont

def main():
    # Tkinter의 Root 창 생성
    root = tk.Tk()
    
    # 사용 가능한 글꼴 목록 가져오기
    fonts_list = tkFont.families()

    # 글꼴 목록을 출력합니다.
    for font in fonts_list:
        print(font)

    # Tkinter 창을 닫습니다.
    root.destroy()  # 프로그램 종료 전 root 창을 종료

if __name__ == "__main__":
    main()