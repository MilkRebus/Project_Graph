from .algorithm_maket import algorithm


class NumberPaths_Algorithm(algorithm):
    def __init__(self):
        super(NumberPaths_Algorithm, self).__init__()
        self.priorityMark = {"Top": {"From": "#ff2929", "Where": "#0c82c7"}}
        self.otherMark = {"Top": {"By": "#0cc779", "Without": "#7500eb"}}
        self.loop = False

    def calculate(self, info):
        super().calculate(info)
        if self.exception():
            self.main_algo(self.priorityMark["Top"]["From"], self.priorityMark["Top"]["Where"])

    def exception(self):
        if super().exception():
            if not self.parameters["Oriented graph"] and len(self.graph["Arrow"]) > 0:
                self.append_answer("Граф должен быть ориентированным")
        if len(self.answer) == 0:
            return True
        else:
            return False

    def main_algo(self, start_node, end_node):
        if self.loop or len(self.graph["Loop"]) > 0:
            self.append_answer("Был обнаружен цикл")
        else:
            if self.otherMark["Top"]["By"] is None:
                self.append_answer(f"Количество путей: {self.count_paths(start_node, end_node)}")
            else:
                after = self.count_paths(start_node, self.otherMark["Top"]["By"])
                end = self.count_paths(self.otherMark["Top"]["By"], end_node)
                if after * end > 0:
                    self.append_answer(f"Количество путей: {after * end}")
                else:
                    self.append_answer(f"Нет пути удовлетворяющего условиям")

    def count_paths(self, start_node, end_node):
        self.paths_number = dict(zip(self.graph["Top"].keys(), [int()] * len(self.graph["Top"])))
        self.top_visit = dict(zip(self.graph["Top"].keys(), [True] * len(self.graph["Top"])))
        self.paths_number[start_node] = 1
        self.start_node = start_node
        self.counting_paths(start_node, end_node)
        return self.paths_number[end_node]

    def counting_paths(self, g, v):
        if v == self.start_node:
            return self.paths_number[g]
        else:
            summ = 0
            for c in self.graph["Top"][v]["algo"]["Arrow"]["in"]:
                if c != self.otherMark["Top"]["Without"]:
                    summ += self.counting_paths(g, c)
            self.paths_number[v] += summ
            self.top_visit[v] = g
            return summ
