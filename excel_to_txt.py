import pandas as pd
# 엑셀 파일 읽기 (파일명은 실제 파일명으로 변경)
infile_path = "wordmaster_2000.xlsx"  # 엑셀 파일 경로 지정
df = pd.read_excel(infile_path)  # 엑셀 파일 로드

# 빈 리스트 생성
Lines = []

# 반복문을 통해 각 행의 값을 가져오기
for index, row in df.iterrows():
    eng = str(row[1]) # 두 번째 열 (2열)
    kor = str(row[2])  # 세 번째 열 (3열)
    for j in range(0, len(kor)) :
        if(kor[j] == ']') :
            kor.replace(kor[j-1], '')
            break

    line = eng + "//" + kor + '\n'
    Lines.append(line)


#txt파일 작성
outfile_path = "워드마스터 수능2000.txt"
outfile = open(outfile_path, 'w')
for line in Lines :
    outfile.write(line)

outfile.close()
print("파일이 성공적으로 저장되었습니다!")
print("파일 이름 : '워드마스터 수능 2000.txt'")
print('')
print("파일 내용")

# 결과 출력
print("1~100번줄")
for i in range(0,101) :
    print(Lines[i])
