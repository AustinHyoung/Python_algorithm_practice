# 세로읽기
import sys

words = []
length = []

for _ in range(5):
  word = sys.stdin.readline()
  words.append(word)
  length.append(len(word))

answer = ''

for i in range(max(length)):
  for j in range(5):
    if i < length[j]:
      answer += words[j][i]
print(answer, end=" ")
