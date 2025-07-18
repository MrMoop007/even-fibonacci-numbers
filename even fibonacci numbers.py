def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

even_terms = []
current_term = fibonacci(0)
n = 0
while current_term <= 4000000:
    current_term = fibonacci(n)
    n += 1
    if current_term%2 == 0:
        even_terms.append(current_term)

print(sum(even_terms))
