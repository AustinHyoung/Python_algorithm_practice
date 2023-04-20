n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(input())

result = []

for a in range(n-7):
    for i in range(m-7):
        # 만약 첫 번째 칸이 W라면 WBWBWBWB, BWBWBWBW로 시작하는 체스판을 만든다.
        cnt1, cnt2 = 0, 0
        for b in range(a, a+8):
            for j in range(i, i+8):
                if (b+j) % 2 == 0:
                    if board[b][j] != 'W': cnt1 += 1
                    if board[b][j] != 'B': cnt2 += 1
                else:
                    if board[b][j] != 'B': cnt1 += 1
                    if board[b][j] != 'W': cnt2 += 1
        result.append(cnt1)
        result.append(cnt2)

print(min(result))
