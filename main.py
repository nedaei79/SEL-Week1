def get_fibonacci(n: int) -> list:
  res = [1, 1]
  for i in range(n - 1):
    res.append(res[-1] + res[-2])
  return res[:n + 1]


def print_result(fibonacci_n: list):
  print(fibonacci_n)


n = int(input())

fibonacci_n = get_fibonacci(n)

print_result(fibonacci_n)
