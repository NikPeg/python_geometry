import settings


class Container:
    _figures_count = 0
    _figures = []

    def read(self):
        self._figures_count = int(settings.fin.readline())
        for i in range(self._figures_count):
            next_line = settings.fin.readline()
            figure_information = next_line.split()
            figure_type = figure_information[0]
            self._figures.append(eval(figure_type)(settings.fin, settings.fout))
            self._figures[-1].read()

    def print(self):
        for i in range(self._figures_count):
            self._figures[i].print()

    def sort(self):
        for i in range(self._figures_count):
            mx = -1
            mxj = 0
            for j in range(self._figures_count):
                if self._figures[j].perimeter > mx:
                    mx = self._figures[j].perimeter
                    mxj = j
            self._figures[i], self._figures[mxj] = self._figures[mxj], self._figures[i]
