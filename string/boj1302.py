import sys
input = sys.stdin.readline

n = int(input())
lst = []

for _ in range(n):
  lst.append(input().strip())

set_list = list(set(lst))
book_cnt = []

for i in set_list:
  book_cnt.append(lst.count(i))

max_val = max(book_cnt)
new_lst = []

for i in range(len(book_cnt)):
  if book_cnt[i] == max_val:
    new_lst.append(set_list[i])

sorted_lst = sorted(new_lst)

print(sorted_lst[0])

