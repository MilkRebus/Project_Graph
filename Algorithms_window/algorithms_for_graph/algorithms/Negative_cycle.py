from .algorithm_maket import algorithm


class Negative_cycle(algorithm):
    def __init__(self):
        super(Negative_cycle, self).__init__()
        self.priorityMark = {"Top": {"Start": "#ff2929"}}

    def calculate(self, info):
        super().calculate(info)
        if self.exception():
            self.bellman_algo(self.priorityMark["Top"]["Start"])

    def weight_edge(self, weight):
        if self.parameters["Weight graph"]:
            return weight if weight is not None else 0
        else:
            return 1
    def exception(self):
        super().exception()
        super().simple_negative_cycle()
        if len(self.answer) == 0:
            return True
        else:
            return False

    def bellman_algo(self, start_node):
        node = dict((i, float("INF")) for i in self.graph["Top"].keys())
        path = dict((i, -1) for i in self.graph["Top"].keys())
        node[start_node] = 0;
        x = -1
        for _ in range(len(node)):
            x = -1
            if self.parameters["Oriented graph"]:
                for cord in self.graph["Arrow"].keys():
                    if node[cord[0]] != float("INF"):
                        if node[cord[1]] > node[cord[0]] + self.weight_edge(self.graph["Arrow"][cord]["algo"]["weight"]):
                            node[cord[1]] = node[cord[0]] + self.weight_edge(self.graph["Arrow"][cord]["algo"]["weight"])
                            path[cord[1]] = cord[0]
                            x = cord[1]
            else:
                for cord in self.graph["Stick"].keys():
                    cord = list(cord)
                    if node[cord[0]] != float("INF"):
                        if node[cord[1]] > node[cord[0]] + self.weight_edge(self.graph["Stick"][cord]["algo"]["weight"]):
                            node[cord[1]] = node[cord[0]] + self.weight_edge(self.graph["Stick"][cord]["algo"]["weight"])
                            path[cord[1]] = cord[0]
                            x = cord[1]
                    if node[cord[1]] != float("INF"):
                        if node[cord[0]] > node[cord[1]] + self.weight_edge(self.graph["Stick"][cord]["algo"]["weight"]):
                            node[cord[0]] = node[cord[1]] + self.weight_edge(self.graph["Stick"][cord]["algo"]["weight"])
                            path[cord[0]] = cord[1]
                            x = cord[0]
        if x == -1:
            self.append_answer("Цикл отрицательного веса не обнаружен")
        else:
            self.set_answer()


    def set_answer(self):
        self.append_answer("Обнаружен цикл отрицательного веса!")
        self.path = None