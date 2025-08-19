def multiplication_table(x):
    results = []
    for i in range(11):
        results.append(x * i)
    return results

print(multiplication_table(2))