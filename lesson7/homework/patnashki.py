from collections import deque
from math import inf
from queue import PriorityQueue
from typing import Deque, Dict, List, Set, Tuple


class GemPuzzle:
    """
    Gem Puzzle console game class.

    It implements console interface for the 15 puzzle game,
    reads start position and finds shortest sequense of steps to the final
    position:

    ``1   2   3   4``\n
    ``5   6   7   8``\n
    ``9   10  11  12``\n
    ``13  14  15  0``

    if it's possible.
    """
    _god_number: int = 80  # max number of steps

    _start_position: Tuple[int]
    _solution: Tuple[int] = (
        1,  2,  3,  4,
        5,  6,  7,  8,
        9,  10, 11, 12,
        13, 14, 15, 0,
    )

    _parents: Dict[Tuple[int], Tuple[int]] = dict()

    _clozed: Set = set()

    def __init__(
        self,
    ) -> None:
        print("Welcome to the GemPuzzle console game!\n")

    @staticmethod
    def _is_solvable(
        position: Tuple[int],
    ) -> bool:
        """
        Checks the criteria of solvability.

        Args:
            position (Tuple[int]): current position of field in format of
            single tuple.

        Returns:
            bool: is position solvable.
        """
        N = 0  # sum for criteria

        for i in range(16):
            if position[i] == 0:
                N += 1 + i // 4
                continue

            for j in range(i, 16):
                N += (position[j] < position[i]) - (position[j] == 0)

        return N % 2 == 0

    @staticmethod
    def _manhattan_distance(
        A: Tuple[int],
        B: Tuple[int],
    ) -> int:
        """
        Finds Manhattan distance between two points (A, B) of position.

        Args:
            A (Tuple[int]): (A row, A column)
            B (Tuple[int]): (B row, B column)

        Returns:
            int: Manhattan distance.
        """
        return abs(A[0] - B[0]) + abs(A[1] - B[1])

    def _h(
        self,
        position: Tuple[int],
    ) -> int:
        """
        Counts evristics of position.

        Args:
            position (Tuple[int]): current position of field in format of
            single tuple.

        Returns:
            int: common Manhattan distance to the
            goal position.
        """
        common_distance = 0

        for i in range(16):
            if position[i] == 0:
                continue
            common_distance += self._manhattan_distance(
                self._get_row_column(i),
                self._get_row_column(position[i] - 1)
            )

        return common_distance

    @staticmethod
    def _find_zero(
        position: Tuple[int],
    ) -> int:
        """
        Finds index of zero element.

        Args:
            position (Tuple[int]): current position of field in format of
            single tuple.

        Returns:
            int: index of zero element.
        """
        for i in range(16):
            if position[i] == 0:
                return i

    @staticmethod
    def _get_row_column(
        index: int
    ) -> Tuple[int]:
        """
        Converts indext of element in single tuple to the row and column
        in the 2d matrix.

        Args:
            index (int): index of element.

        Returns:
            Tuple[int]: row, column of element.
        """
        return index // 4, index % 4

    def _is_solution(
        self,
        position: Tuple[int],
    ) -> bool:
        """
        Checks if position is goal position.

        Args:
            position (Tuple[int]): current position of field in format of
            single tuple.

        Returns:
            bool: is position a goal position.
        """
        return position == self._solution

    def _get_neighbours(
        self,
        position: Tuple[int],
    ) -> List[Tuple[int]]:
        """
        Swaps zero tile to with neighbours.

        Args:
            position (Tuple[int]): current position of field in format of
            single tuple.

        Returns:
            List[Tuple[int]]: list of adjacent positions.
        """
        zero_index = self._find_zero(position)
        row, column = self._get_row_column(zero_index)
        adjacnet = []
        neighbors = [
            row * 4 + (column - 1) if column > 0 else None,
            row * 4 + (column + 1) if column < 3 else None,
            (row - 1) * 4 + column if row > 0 else None,
            (row + 1) * 4 + column if row < 3 else None
        ]

        for neighbor in neighbors:
            if neighbor is None:
                continue
            new_position = list(position)
            new_position[zero_index], new_position[neighbor] = (
                new_position[neighbor], new_position[zero_index]
            )
            new_position = tuple(new_position)
            if new_position not in self._clozed:
                adjacnet.append(tuple(new_position))

        return adjacnet

    def _initialize_start_position(
        self,
    ) -> None:
        """
        Reads start position of the game.

        Raises:
            ValueError: if start position is unsolvable.
        """
        print("Set start position:")
        start_position = []
        for _ in range(4):
            start_position += list(map(int, input().split()))

        self._start_position = tuple(start_position)

        if not self._is_solvable(self._start_position):
            raise ValueError("Start position is unsolvable.")

    def _find_shortest_sequence(
        self,
    ) -> None:
        """
        Function represents positions like points in the graph,
        and finds shirtest way between start and finish using A-star algorithm.
        """
        priority_q = PriorityQueue()
        priority_q.put((self._h(self._start_position), self._start_position))

        g = {self._start_position: 0}

        while not priority_q.empty():
            _, position = priority_q.get()

            print(self._h(position))

            if self._is_solution(position):
                return
            self._clozed.add(position)
            for neighbour in self._get_neighbours(position):
                g_new = g[position] + 1
                if g_new < g.get(neighbour, inf):
                    priority_q.put((g_new + self._h(neighbour), neighbour))
                    g[neighbour] = g_new
                    self._parents[neighbour] = position

    def _get_sequense_from_parents(
        self,
    ) -> Deque[Tuple[int]]:
        """
        Builds list of positions led to the goal position from begining.

        Returns:
            Deque[Tuple[int]]: list of positions.
        """
        sequence = deque(maxlen=self._god_number)
        current_position = self._solution

        while current_position != self._start_position:
            sequence.appendleft(current_position)
            current_position = self._parents[current_position]

        return sequence

    @staticmethod
    def _print_position(
        position: Tuple[int]
    ) -> None:
        """
        Prints position to the console.

        Args:
            position (Tuple[int]): _description_
        """
        for i in range(4):
            for j in range(4):
                print(position[i * 4 + j], end=" ")
            print()
        print()

    def _print_winning_sequence(
        self,
    ) -> None:
        """
        Prints to console sequence of positions, led to the winning position.
        """
        sequence = self._get_sequense_from_parents()
        print(
            f"\nIt took {len(sequence)} steps out of "
            f"{self._god_number} (maximum):\n"
        )
        for i in range(len(sequence)):
            print(f"Step {i + 1}:")
            self._print_position(sequence[i])

    def run(
        self,
    ) -> None:
        """
        Main function of Gem Puzzle Game.

        It initializes start position of the game, and
        finds sequence of position leading to the final position.
        """
        self._initialize_start_position()

        self._find_shortest_sequence()

        self._print_winning_sequence()


if __name__ == "__main__":
    GemPuzzle().run()
