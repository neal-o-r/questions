
arr = [
    [1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1],
]


class island_solver:
    def __init__(self, matrix):
        self.matrix = matrix
        self.nrows = len(matrix)
        self.ncols = len(matrix[0])
        self.visited = [[False for i in range(self.ncols)] for j in range(self.nrows)]

    def valid_index(self, i, j):
        return (
            i >= 0
            and j >= 0
            and i < self.nrows
            and j < self.ncols
            and not self.visited[i][j]
            and self.matrix[i][j]
        )

    def dfs(self, i, j):

        row_nbr = [-1, 0, 0, 1]
        col_nbr = [0, -1, 1, 0]
        self.visited[i][j] = True
        for nr, nc in zip(row_nbr, col_nbr):
            if self.valid_index(i + nr, j + nc):
                self.dfs(i + nr, j + nc)

    def count(self):

        c = 0
        for i in range(self.nrows):
            for j in range(self.ncols):
                if not self.visited[i][j] and self.matrix[i][j]:
                    self.dfs(i, j)
                    c += 1
        return c
