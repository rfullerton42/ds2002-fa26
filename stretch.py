# stretch
def describe_number(n):
  if n % 2 == 0:
    parity = 'even'
  else:
    parity = 'odd'

  if n < 0:
    sign = 'negative'
  else: 
    sign = 'positive'

  return f"{n} is {parity} and {sign}"

numbers = [1, 5, 4, 3, 9]

for n in numbers:
  print(describe_number(n))
