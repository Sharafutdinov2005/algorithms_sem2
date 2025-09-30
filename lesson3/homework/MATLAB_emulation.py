from abc import ABC, abstractmethod
from typing import List


class Vertex(ABC):
    """
    Abstract class that realizes interface for calculation graph.
    """

    @property
    def number_of_inputs(
        self,
    ) -> int:
        ...

    @property
    def number_of_outputs(
        self,
    ) -> int:
        ...

    @abstractmethod
    def set_input(
        self,
        input_index: int,
        value: float,
    ) -> None:
        ...

    @abstractmethod
    def get_output(
        self,
        output_index: int,
    ) -> float:
        ...

    @abstractmethod
    def calculate(
        self,
    ) -> None:
        ...


class Edge:
    out_vertex_id:      int
    out_port_id:        int
    inp_vertex_id:      int
    inp_port_id:        int

    def __init__(
        self,
        out_vertex_id,
        out_port_id,
        inp_vertex_id,
        inp_port_id,
    ) -> None:
        self.out_vertex_id = out_vertex_id
        self.out_port_id = out_port_id
        self.inp_vertex_id = inp_vertex_id
        self.inp_port_id = inp_port_id


class CalculationGraph(Vertex):
    _vertex:            List[Vertex]
    _adjacency_list:    List[List[Edge]]
    _inputs:            List[List[int]]
    _outputs:           List[List[int]]

    @property
    def number_of_inputs(
        self,
    ) -> int:
        return len(self._inputs)

    def set_input(
        self,
        num_input: int,
        value: float,
    ) -> None:
        vertex_to_set = self._inputs[num_input][0]
        vertex_input_to_set = self._inputs[num_input][1]

        self._vertex[vertex_to_set].set_input(vertex_input_to_set, value)

    @property
    def number_of_outputs(
        self,
    ) -> int:
        return len(self._outputs)

    def get_output(
        self,
        output_index
    ) -> float:
        i, output = (
            self._outputs[output_index][0], self._outputs[output_index][1]
        )
        return self._vertex[i].get_output(output)

    def calculate(
        self,
    ) -> None:
        for vertex in self._calc_order:
            print(vertex)
            for edge in self._adjacency_list[vertex]:
                out_value = self._vertex[edge.out_vertex_id].get_output(
                    edge.out_port_id
                )
                self._vertex[vertex].set_input(
                    edge.inp_port_id,
                    out_value
                )

            self._vertex[vertex].calculate()

    def set_data(
        self,
        vertex: List[Vertex],
        edges: List[Edge],
    ) -> None:
        self._vertex = vertex
        self._build_adjacency_list(vertex, edges)
        self._topological_sort()

    def _build_adjacency_list(
        self,
        vertex: List[Vertex],
        edges: List[Edge],
    ) -> None:
        self._adjacency_list = []
        self._inputs = []
        self._outputs = []

        for i in range(len(vertex)):
            self._adjacency_list.append([])
            for input in range(vertex[i].number_of_inputs):
                self._inputs.append([i, input])  # all possible inputs
            for output in range(vertex[i].number_of_outputs):
                self._outputs.append([i, output])  # all possible outputs

        for edge in edges:
            self._adjacency_list[edge.inp_vertex_id].append(edge)
            # removing taken i/o
            # It provides convenient interface for i/o processing
            self._inputs.remove([edge.out_vertex_id, edge.out_port_id])
            self._outputs.remove([edge.inp_vertex_id, edge.inp_port_id])

    def _topological_sort(
        self,
    ) -> None:
        visited = [False] * len(self._vertex)
        self._calc_order = []

        def DFS(v: int) -> None:
            visited[v] = True
            for u in self._adjacency_list[v]:
                if not visited[u.inp_vertex_id]:
                    DFS(u.inp_vertex_id)
            self._calc_order.append(v)

        for v in range(len(self._vertex)):
            if not visited[v]:
                DFS(v)

        self._calc_order = self._calc_order
        print(self._calc_order)


class BinarySummator(Vertex):
    _input = [None, None]
    _output = [None]

    @property
    def number_of_inputs(
        self,
    ) -> int:
        return 2

    @property
    def number_of_outputs(
        self,
    ) -> int:
        return 1

    def set_input(
        self,
        input_index: int,
        value: float,
    ) -> None:
        self._input[input_index] = value

    def get_output(
        self,
        output_index: int,
    ) -> float:
        return self._output[output_index]

    def calculate(
        self,
    ) -> None:
        self._output[0] = sum(self._input)


if __name__ == "__main__":
    plus1 = BinarySummator()
    plus2 = BinarySummator()

    vertex = [plus1, plus2]

    edges = [Edge(0, 0, 1, 0)]

    graph = CalculationGraph()

    graph.set_data(vertex, edges)

    print(graph.number_of_inputs, graph.number_of_outputs)

    graph.set_input(0, 1)
    graph.set_input(1, 1)
    graph.set_input(2, 1)

    graph.calculate()

    print(graph.get_output(0))
