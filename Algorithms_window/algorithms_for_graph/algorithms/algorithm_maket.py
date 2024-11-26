class algorithm:
    def __init__(self):
        self._info = {"priority": {}, "other": {}}
        self._other_mark = {}
        self._color_mark = {}
        self._path = []
        self._answer = []
        self._parameters = []
        self._graph = {}
        self._priority_mark = {}

    def append_answer(self, text):
        self._answer.append(text)

    @property
    def priorityMark(self):
        return self._priority_mark

    @priorityMark.setter
    def priorityMark(self, dict):
        self._info["priority"] = dict

    @property
    def otherMark(self):
        return self._other_mark

    @otherMark.setter
    def otherMark(self, dict):
        self._info["other"] = dict

    @property
    def answer(self):
        return self._answer

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, info):
        self._path = info

    @property
    def graph(self):
        return self._graph

    @graph.setter
    def graph(self, graph_dict):
        self._graph = graph_dict

    def calculate(self, info):
        self._answer = []
        self._path = None
        self.graph = info["graph"]
        self.parameters = info["parameter"]
        self._priority_mark = info["dop_info"]["priority"]
        self._other_mark = info["dop_info"]["other"]

    @property
    def parameters(self):
        return self._parameters

    @parameters.setter
    def parameters(self, parameter):
        self._parameters = parameter

    @property
    def info(self):
        return self._info

    def exception(self):
        if len(self.graph) != 0:
            if not (len(self.priorityMark["Top"]) == len(self.priorityMark["Top"]) and None not in set(
                    self.priorityMark["Top"].values())):
                self.append_answer("Не указаны дополнительные вершины")

            if len(self.graph["Arrow"]) == 0 and len(self.graph["Stick"]) == 0:
                self.append_answer("В графе отсутствуют ребра")

            if len(self.answer) == 0:
                return True
            else:
                return False
        else:
            return False

    def negative_cycle(self):
        return False

    def simple_negative_cycle(self):
        if len(self.graph) != 0:
            if self.parameters["Oriented graph"]:
                for i in self.graph["Loop"]:
                    if self.graph["Loop"][i]["algo"]["weight"] and self.graph["Loop"][i]["algo"]["weight"] < 0:
                        self.append_answer("Цикл отрицательного веса!")
                        break
            else:
                for i in self.graph["Stick"]:
                    if self.graph["Stick"][i]["algo"]["weight"] and self.graph["Stick"][i]["algo"]["weight"] < 0:
                        self.append_answer("Не ориентированное ребро отрицательного веса - отрицательный цикл!")
                        break
            if len(self.answer) == 0:
                return True
            else:
                return False
        else:
            return False

    def negative_edge(self):
        if len(self.graph) != 0:
            if self.parameters["Oriented graph"]:
                for i in self.graph["Arrow"]:
                    if self.graph["Arrow"][i]["algo"]["weight"] and self.graph["Arrow"][i]["algo"]["weight"] < 0:
                        self.append_answer("В графе есть ребра отрицательного веса")
                        break
                for i in self.graph["Loop"]:
                    if self.graph["Loop"][i]["algo"]["weight"] and self.graph["Loop"][i]["algo"]["weight"] < 0:
                        self.append_answer("В графе есть ребра отрицательного веса")
                        break
            else:
                for i in self.graph["Stick"]:
                    if self.graph["Stick"][i]["algo"]["weight"] and self.graph["Stick"][i]["algo"]["weight"] < 0:
                        self.append_answer("В графе есть ребра отрицательного веса")
                        break
            if len(self.answer) == 0:
                return True
            else:
                return False
        else:
            return False