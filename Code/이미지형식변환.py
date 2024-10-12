from PIL import Image
import os

def convert_image():
    # 1. 사용자로부터 이미지 파일 이름을 입력받기
    filename = input("변환할 이미지 파일의 이름을 입력하세요 (확장자 제외): ")

    # 가능성이 있는 확장자 목록
    data_extension = ['.jpg', '.jpeg', '.png', '.gif', '.jfif']

    img = None
    for ext in data_extension:
        try:
            # 2. 이미지 파일의 형식을 확인하고 이미지 열기
            img = Image.open(filename + ext)
            print(f"{filename + ext} 파일을 성공적으로 열었습니다.")
            break  # 파일을 성공적으로 열었으면 반복문 종료
        except FileNotFoundError:
            continue  # 파일이 없으면 다음 확장자로 시도
        except IOError:
            continue  # 파일을 열 수 없으면 다음 확장자로 시도

    if img == None:
        print("파일을 찾을 수 없습니다. 경로와 파일 이름을 확인하세요.")
        return

    # 3. 사용자로부터 변환할 형식을 입력받기
    ext_res = input("변환할 형식을 입력하세요 (예: 'JPEG', 'PNG', 'GIF'): ").lower()

    # 4. 새로운 파일 이름 생성
    output_filename = f"{filename}.{ext_res}"  # 새로운 파일 이름 생성

    # 이미지 저장
    try:
        img.save(output_filename, format=ext_res)
        print(f"이미지를 성공적으로 변환하여 저장했습니다: {output_filename}")
    except Exception as e:
        print(f"이미지 저장 중 오류 발생: {e}")

# 함수 실행
convert_image()
