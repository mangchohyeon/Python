import pandas as pd

# CSV 파일(Excel csv파일) 경로
file_path = input()

# CSV 파일 읽기
df = pd.read_csv(file_path)

#A열을 읽어와서 A열에 담긴 문자열을 eng라는 리스트에 추가
eng = df.iloc[:, 0].tolist()

#B열을 읽어와서 B열에 담긴 문자열을 kor라는 리스트에 추가
kor = df.iloc[:, 1].tolist()


