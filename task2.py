def input_matrix():
    matrix = []
    for i in range(3):
        row = list(map(int, input(f"Введите 3 числа через пробле: ").split()))
        if len(row) != 3:
            print("Должно быть 3 числа")
            return None
        matrix.append(row)
    return matrix

def unique_elements(matrix):
    unique_set = set()
    for row in matrix:
        unique_set.update(row)
    return tuple(unique_set)

def print_matrix(matrix):
    print("Введенная матрица:")
    for row in matrix:
        print(" ".join(map(str, row)))

def main():
    matrix = input_matrix()
    if matrix is None:
        return main()
    print_matrix(matrix)
    unique_tuple = unique_elements(matrix)
    print("Результирующий кортеж из уникальных элементов:", unique_tuple)

if __name__ == "__main__":
    main()
