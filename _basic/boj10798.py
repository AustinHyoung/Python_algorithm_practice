# 세로 읽기
# 15개의 문자열을 저장할 리스트 생성
lines = [''] * 15

# 입력받은 문자열을 한 글자씩 lines 리스트에 저장
for i in range(5):
    s = input().strip()
    for j in range(len(s)):
        lines[j] += s[j]

# lines 리스트에 저장된 문자열을 차례대로 출력
for line in lines:
    print(line, end='')