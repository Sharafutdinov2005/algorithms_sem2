def graph_matrix_to_list(
    matrix: list[list[int]]
) -> list[list[int]]:
    adj_list = []

    for i in range(len(matrix)):
        adj_list.append([])
        for j in range(len(matrix)):
            if matrix[i][j]:
                adj_list[i].append(j)

    return adj_list


def graph_list_to_matrix(
    adj_list: list[list[int]]
) -> list[list[int]]:
    matrix = []
    for _ in range(len(adj_list)):
        matrix.append([0] * len(adj_list))

    for i in range(len(adj_list)):
        for a in adj_list[i]:
            matrix[i][a] = 1

    return matrix
