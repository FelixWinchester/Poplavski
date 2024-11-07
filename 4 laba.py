import numpy as np

eps = 1e-6


def gauss(sole):
    n = len(sole)
    m = len(sole[0])
    x_coords = list(range(n))

    print("Расширенная матрица СЛАУ:")
    for row in sole:
        print("\t".join(f"{x:.10f}" for x in row))
    print("Номера неизвестных:")
    print("\t".join(map(str, x_coords)), "\n")

    for j in range(m - 1):
        mx = j
        for i in range(j, n):
            if abs(sole[i][j]) > abs(sole[mx][j]):
                mx = i
        if abs(sole[mx][j]) < eps:
            sole[j], sole[mx] = sole[mx], sole[j]
        else:
            mx = j
            for i in range(j, n):
                if abs(sole[j][i]) > abs(sole[j][mx]):
                    mx = i
            x_coords[j], x_coords[mx] = x_coords[mx], x_coords[j]
            for i in range(n):
                sole[i][mx], sole[i][j] = sole[i][j], sole[i][mx]

        if abs(sole[j][mx]) < eps:
            raise ValueError("Division by zero!")

        for i in range(j + 1, n):
            d = sole[i][j] / sole[j][j]
            for k in range(m):
                sole[i][k] -= sole[j][k] * d

    print("Прямой ход метода Гаусса:")
    for row in sole:
        print("\t".join(f"{x:.10f}" for x in row))
    print("Номера неизвестных:")
    print("\t".join(map(str, x_coords)), "\n")

    for j in range(n - 1, -1, -1):
        for i in range(j - 1, -1, -1):
            d = sole[i][j] / sole[j][j]
            sole[i][j] -= sole[j][j] * d
            sole[i][m - 1] -= sole[j][m - 1] * d

    print("Обратный ход метода Гаусса:")
    for row in sole:
        print("\t".join(f"{x:.10f}" for x in row))
    print()

    s = np.zeros(n)
    for i in range(n):
        s[x_coords[i]] = sole[i][m - 1] / sole[i][i]
    return s


def gauss_solution(A, B):
    for i in range(len(A)):
        A[i].append(B[i])
    return gauss(A)


def solve():
    n = 5
    v = 16.0
    A = [[(v + i) / 100 if i != j else v + i for j in range(n)] for i in range(n)]
    V = [v + i for i in range(n)]

    B = [sum(A[i][j] * V[j] for j in range(n)) for i in range(n)]
    solution = gauss_solution(A, B)

    print("Решение СЛАУ:")
    print("\t".join(f"{x:.10f}" for x in solution))


if __name__ == "__main__":
    solve()
