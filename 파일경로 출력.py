import os

# 파일 이름 입력받기
file_name = input("파일 이름을 입력하세요: ")

# 파일 이름에서 확장자 제거
base_name = os.path.splitext(file_name)[0]

# 현재 디렉토리의 모든 파일 검색
flag = False
for root, dirs, files in os.walk('.'):
    for file in files:
        # 파일 이름에서 확장자를 제거한 이름과 입력된 이름이 같은지 확인
        if os.path.splitext(file)[0] == base_name:
            # 파일 경로 출력
            print("")
            print("Result")
            print(f"파일명 : {file}")
            print(f'파일 경로 : "{os.path.abspath(os.path.join(root, file))}"')
            print("")
            flag = True
            

if not flag:
    print("")
    print("Result")
    print("파일이 존재하지 않습니다.")

