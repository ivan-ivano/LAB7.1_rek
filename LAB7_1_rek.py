import random


def process_matrix(matrix, rows, cols, i=0, j=0, count=0, total_sum=0):
    if i >= rows:
        return matrix, count, total_sum

    if j >= cols:
        return process_matrix(matrix, rows, cols, i + 1, 0, count, total_sum)

    if j % 2 != 0 or i % 2 != 0 or matrix[i][j] % 7 == 0:
        count += 1
        total_sum += matrix[i][j]
        matrix[i][j] = 0

    return process_matrix(matrix, rows, cols, i, j + 1, count, total_sum)


def change(a, row1, row2, cols, j=0):
    if j >= cols:
        return

    tmp = a[row1][j]
    a[row1][j] = a[row2][j]
    a[row2][j] = tmp

    change(a, row1, row2, cols, j + 1)


def custom_sort(a, rows, cols, i0=0, i1=0):
    if i0 >= rows - 1:
        return a

    if i1 < rows - i0 - 1:
        if (a[i1][0] < a[i1 + 1][0] or
                (a[i1][0] == a[i1 + 1][0] and a[i1][1] > a[i1 + 1][1]) or
                (a[i1][0] == a[i1 + 1][0] and a[i1][1] == a[i1 + 1][1] and a[i1][2] < a[i1 + 1][2])):
            change(a, i1, i1 + 1, cols)

        return custom_sort(a, rows, cols, i0, i1 + 1)

    return custom_sort(a, rows, cols, i0 + 1, 0)


def print_matrix(matrix, index=0, row=0):
    if row >= len(matrix):
        return

    if index < len(matrix[row]):
        print(f"{matrix[row][index]:>5}{'  ' if index == len(matrix[row]) - 1 else ''}", end='')
        return print_matrix(matrix, index + 1, row)
    elif index == len(matrix[row]):
        print()
        return print_matrix(matrix, 0, row + 1)


def create_matrix(rows, cols, lower_limit, upper_limit, current_row=0, matrix=None):
    if matrix is None:
        matrix = []

    if current_row == rows:
        return matrix

    if len(matrix) <= current_row:
        matrix.append([])

    matrix[current_row].append(random.randint(lower_limit, upper_limit))

    if len(matrix[current_row]) == cols:
        return create_matrix(rows, cols, lower_limit, upper_limit, current_row + 1, matrix)

    return create_matrix(rows, cols, lower_limit, upper_limit, current_row, matrix)


def main():
    rows, cols = 8, 6
    lower_limit, upper_limit = 16, 97
    matrix = create_matrix(rows, cols, lower_limit, upper_limit)

    print("Матриця до обробки:")
    print_matrix(matrix)

    sorted_matrix = custom_sort(matrix, rows, cols)

    print("\nМатриця після сортування:")
    print_matrix(sorted_matrix)

    matrix, count, total_sum = process_matrix(sorted_matrix, rows, cols)

    print("\nМатриця після обробки:")
    print_matrix(matrix)

    print(f"Кількість підходящих елементів: {count}")
    print(f"Сума підходящих елементів: {total_sum}")


if __name__ == "__main__":
    main()
