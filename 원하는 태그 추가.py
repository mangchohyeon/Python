<<<<<<< HEAD
lines = []

print("""추가하고 싶은 시작 태그를 입력하세요
                      만약 원하시는 태그가 없으시면 X를 입력하시면 됩니다.
                      태그를 작성할 때에는 <>기호 없이 입력하세요""")

tag_start = str(input())

if tag_start == "X" :
    tag_start = ""
else :
    tag_start  = "<" + tag_start + ">"

print("""추가하고 싶은 끝 태그를 입력하세요
                      만약 원하시는 태그가 없으시면 X를 입력하시면 됩니다.
                      태그를 작성할 때에는 <>기호 없이 입력하세요""")
tag_end = str(input())

if tag_end == "X" :
    tag_end = ""
else :
    if tag_start == "" :
        tag_end  = "<" + tag_end + ">"
    else :
        tag_end  = "</" + tag_end + ">"

print("지금부터는 태그를 추가하고 싶은 문자열을 입력하세요")
while True :
    line = str(input())
    if line == "" :
        break
    
    temp = line.lstrip()
    lines.append(tag_start + temp + tag_end)

print("-------------------------------------------------------------------------------------------------------------------------------------")
for i in lines :
    print(i)

=======
lines = []

print("""추가하고 싶은 시작 태그를 입력하세요
                      만약 원하시는 태그가 없으시면 X를 입력하시면 됩니다.
                      태그를 작성할 때에는 <>기호 없이 입력하세요""")

tag_start = str(input())

if tag_start == "X" :
    tag_start = ""
else :
    tag_start  = "<" + tag_start + ">"

print("""추가하고 싶은 끝 태그를 입력하세요
                      만약 원하시는 태그가 없으시면 X를 입력하시면 됩니다.
                      태그를 작성할 때에는 <>기호 없이 입력하세요""")
tag_end = str(input())

if tag_end == "X" :
    tag_end = ""
else :
    if tag_start == "" :
        tag_end  = "<" + tag_end + ">"
    else :
        tag_end  = "</" + tag_end + ">"

print("지금부터는 태그를 추가하고 싶은 문자열을 입력하세요")
while True :
    line = str(input())
    if line == "" :
        break
    
    temp = line.lstrip()
    lines.append(tag_start + temp + tag_end)

print("-------------------------------------------------------------------------------------------------------------------------------------")
for i in lines :
    print(i)

>>>>>>> dd8e939951dba8cd1978e102b9a0df48e8b907be
