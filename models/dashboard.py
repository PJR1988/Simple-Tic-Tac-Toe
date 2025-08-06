class Dashboard():
    def __init__(self):
        self._cells = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self._valid_cells = ["11", "12", "13", "21", "22", "23", "31", "32", "33"]
        self._dashboard_state = ""

        self.update_dashboard()

    def update_dashboard(self):
        self.dashboard_state = "   1   2   3 \n" \
                               "     |   |   \n" \
                               "1  {} | {} | {} \n" \
                               "  ___|___|___\n" \
                               "     |   |   \n" \
                               "2  {} | {} | {} \n" \
                               "  ___|___|___\n" \
                               "     |   |   \n" \
                               "3  {} | {} | {} \n" \
                               "     |   |   ".format(*self.get_all_cells())
        print(self.dashboard_state)

    def update_cell(self, cell: str = None, mark: str = None):
        if cell in self.valid_cells and mark in ['x', 'o']:
            self.cells[int(cell[0]) - 1][int(cell[1]) - 1] = mark
            self.update_dashboard()
            return True
        else:
            if mark not in ['x', 'o']:
                print(f"select 'x' or 'o', not {x11}")
            else:
                print(f"Already selected, {self.x11}")

    def reset_dashboard(self):
        self.cells = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]

        self.update_dashboard()

    def get_all_lines(self):
        return [
                self.line1,
                self.line2,
                self.line3,
                self.colum1,
                self.colum2,
                self.colum3,
                self.diagonal1,
                self.diagonal2
               ]

    def win(self, sel):
        if [sel, sel, sel] in self.get_all_lines():
            return True

    def get_all_cells(self):
        list_of_cells = []
        list_of_cells.extend(self.line1)
        list_of_cells.extend(self.line2)
        list_of_cells.extend(self.line3)
        return list_of_cells

    def update_valid_cells(self, cell: str = None):
        self.valid_cells.remove(cell)

    @property
    def line1(self):
        return self.cells[0]

    @property
    def line2(self):
        return self.cells[1]

    @property
    def line3(self):
        return self.cells[2]

    @property
    def colum1(self):
        return [self.cells[0][0], self.cells[1][0], self.cells[2][0]]

    @property
    def colum2(self):
        return [self.cells[0][1], self.cells[1][1], self.cells[2][1]]

    @property
    def colum3(self):
        return [self.cells[0][2], self.cells[1][2], self.cells[2][2]]

    @property
    def diagonal1(self):
        return [self.cells[0][0], self.cells[1][1], self.cells[2][2]]

    @property
    def diagonal2(self):
        return [self.cells[2][0], self.cells[1][1], self.cells[0][2]]

    @property
    def full(self):
        if " " not in self.get_all_cells():
            return True

    @property
    def cells(self):
        return self._cells

    @property
    def dashboard_state(self):
        return self._dashboard_state

    @property
    def valid_cells(self):
        return self._valid_cells

    @cells.setter
    def x11(self, cells: list[list]):
        self._cells = cells

    @valid_cells.setter
    def valid_cells(self, valid_cells):
        self.valid_cells = valid_cells

    @dashboard_state.setter
    def dashboard_state(self, dashboard_state):
        self._dashboard_state = dashboard_state
