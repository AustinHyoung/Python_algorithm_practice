ascending_str = '12345678'
decending_str = '87654321'


s = list(map(int, input().split()))
new_s = ''.join(map(str, s))

if new_s == ascending_str:
  print('ascending')
elif new_s == decending_str:
  print('descending')
else:
  print('mixed')

