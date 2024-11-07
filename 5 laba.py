def tridiagonal_algorithm(a, b, c, d):
    n = len(a)
    p = [0] * (n + 1)
    q = [0] * (n + 1)

    # Прямая прогонка
    for i in range(n):
        denom = b[i] - a[i] * p[i]
        p[i + 1] = c[i] / denom
        q[i + 1] = (a[i] * q[i] - d[i]) / denom

    print("Прямая прогонка:")
    for i in range(1, n):
        print(f"( {p[i]:.4f}, {q[i]:.4f} )")
    print(f"( {q[n]:.4f}, )\n")

    # Обратная прогонка
    res = [0] * n
    res[n - 1] = q[n]
    for i in range(n - 2, -1, -1):
        res[i] = p[i + 1] * res[i + 1] + q[i + 1]

    return res


def solve():
    n = 5
    v = 16
    A = [[0] * n for _ in range(n)]

    # Создание трехдиагональной матрицы A
    for i in range(n):
        for j in range(max(0, i - 1), min(i + 2, n)):
            A[i][j] = (v + i) / 100
        A[i][i] = v + i

    V = [(v + i) for i in range(n)]
    B = [sum(A[i][j] * V[j] for j in range(max(0, i - 1), min(i + 2, n))) for i in range(n)]

    print("Расширенная матрица A|B:")
    for i in range(n):
        print("\t".join(f"{A[i][j]:.4f}" for j in range(n)), "|", f"{B[i]:.4f}")
    print()

    a = [A[i][i - 1] if i > 0 else 0 for i in range(n)]
    b = [-A[i][i] for i in range(n)]
    c = [A[i][i + 1] if i < n - 1 else 0 for i in range(n)]
    d = B

    # Решение системы
    X = tridiagonal_algorithm(a, b, c, d)
    print("Решение СЛАУ:")
    print("\t".join(f"{x:.4f}" for x in X))


if __name__ == "__main__":
    solve()
