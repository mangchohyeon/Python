import pandas as pd

# 엑셀 파일 입력받기 (파일명은 실제 파일명으로 변경)
print("변환하고 싶은 엑셀파일의 경로를 입력하세요 : ")
infile_path = str(input())
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
print("txt파일로 저장할 파일의 이름을 입력하세요 : ")
input(outfile_path)
outfile = open(outfile_path, 'w')
for line in Lines :
    outfile.write(line)

outfile.close()
print("파일이 성공적으로 저장되었습니다!")
print(f"파일 이름 : {outfile_path}")
print('')
print("파일 내용")

# 결과 출력
print("1~100번줄")
for i in range(0,101) :
    print(Lines[i])
