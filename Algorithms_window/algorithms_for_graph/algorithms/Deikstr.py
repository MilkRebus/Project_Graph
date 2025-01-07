from .algorithm_maket import algorithm


class Deikstr_Algorithm(algorithm):
    def __init__(self):
        super(Deikstr_Algorithm, self).__init__()
        self.priorityMark = {"Top": {"From": "#ff2929", "Where": "#1357bd"}}

    def calculate(self, info):
        super().calculate(info)
        if self.exception():
            self.deikstr_algo(self.priorityMark["Top"]["From"], self.priorityMark["Top"]["Where"])

    def weight_edge(self, weight):
        if self.parameters["Weight graph"]:
            return weight if weight is not None else 0
        else:
            return 1

    def exception(self):
        super().exception()
        if self.parameters["Weight graph"]: super().negative_edge()
        if self.priorityMark["Top"]["From"] == self.priorityMark["Top"]["Where"]:
            self.append_answer("Путь начинается и заканчивается в одной вершине")
        if len(self.answer) == 0:
            return True
        else:
            return False

    def deikstr_algo(self, start_node, end_node):
        unvisited_nodes = set(self.graph["Top"].keys())
        shortest_path = {node: float("inf") for node in self.graph["Top"].keys()}
        previous_nodes = {}
        shortest_path[start_node] = 0
        while unvisited_nodes:
            current_min_node = None
            for node in unvisited_nodes:
                if current_min_node is None:
                    current_min_node = node
                elif shortest_path[node] < shortest_path[current_min_node]:
                    current_min_node = node

            if self.parameters["Oriented graph"]:
                neighbors = self.graph["Top"][current_min_node]["algo"]["Arrow"]["out"]
            else:
                neighbors = self.graph["Top"][current_min_node]["algo"]["Stick"]

            for neighbor in neighbors:

                if self.parameters["Oriented graph"]:
                    if current_min_node != neighbor:
                        weight = self.weight_edge(self.graph["Arrow"][(current_min_node, neighbor)]["algo"]["weight"])
                else:
                    weight = self.weight_edge(
                        self.graph["Stick"][frozenset([current_min_node, neighbor])]["algo"]["weight"])

                tentative_value = shortest_path[current_min_node] + weight
                if tentative_value < shortest_path[neighbor]:
                    shortest_path[neighbor] = tentative_value
                    previous_nodes[neighbor] = current_min_node
            unvisited_nodes.remove(current_min_node)

        if end_node in previous_nodes:
            self.set_answer(previous_nodes, shortest_path, start_node, end_node)
        else:
            self.answer.append("Вершины не связыват не один путь")

    def set_answer(self, previous_nodes, shortest_path, start_node, end_node):
        self.append_answer("Вес кратчайшего пути: " + str(shortest_path[end_node]))
        if self.parameters["Light path"]:
            path = []
            node = end_node
            while node != start_node:
                path.append(node)
                node = previous_nodes[node]
            path.append(start_node)
            self.path = [path, "Arrow" if self.parameters["Oriented graph"] else "Stick"]
        else:
            self.path = None
