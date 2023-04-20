# 116
# 125
# 134
# 143
# 152
# 161

# 215
# 224
# 233
# 242
# 251


# 314
# 323
# 332
# 341

# 413
# 422
# 431

# 512
# 521

# 611

word = input()
words = []

for i in range(1, len(word)+1):
  for j in range(1, (len(word)+1)-i):
    k = len(word) - (i+j)
    if k == 0:
      continue
    else:
      part1 = word[0:i]
      part2 = word[i:j+i]
      part3 = word[j+i:]
      reverse_part1 = part1[::-1]
      reverse_part2 = part2[::-1]
      reverse_part3 = part3[::-1]
      words.append(reverse_part1 + reverse_part2 + reverse_part3)

print(min(words))
