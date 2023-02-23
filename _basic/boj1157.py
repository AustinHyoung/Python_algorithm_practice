# 단어 공부

s = input().upper()
list_set = list(set(s))

cnt_list = []
for i in list_set:
    cnt = s.count(i)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1:
    print("?")
else:
    max = cnt_list.index(max(cnt_list))
    print(list_set[max])
