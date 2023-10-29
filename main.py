def get_fibonacci(n: int) -> list:
  return [1, 1, 2]


def print_result(fibonacci_n: list):
  for i in range(len(fibonacci_n) - 2):
    print(f"f[{i}]: {fibonacci_n[i]}  +  f[{i+1}]: {fibonacci_n[i+1]}  ->  f[{i+2}]: {fibonacci_n[i+2]}")


n = int(input())

fibonacci_n = get_fibonacci(n)

print_result(fibonacci_n)
