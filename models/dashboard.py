class Dashboard():
    def __init__(self):
        self._x11 = ' '
        self._x12 = ' '
        self._x13 = ' '
        self._x21 = ' '
        self._x22 = ' '
        self._x23 = ' '
        self._x31 = ' '
        self._x32 = ' '
        self._x33 = ' '
        self._valid_cells = ["11", "12", "13", "21", "22", "23", "31", "32", "33"]

        self._dashboard_state="   |   |   \n   |   |   \n___|___|___\n   |   |   \n   |   |   \n___|___|___\n   |   |   \n   |   |   \n   |   |   "
        print(self.dashboard_state)

    def update_dashboard(self):
        self.dashboard_state = f"   |   |   \n {self.x11} | {self.x12} | {self.x13} \n___|___|___\n   |   |   \n {self.x21} | {self.x22} | {self.x23} \n___|___|___\n   |   |   \n {self.x31} | {self.x32} | {self.x33} \n   |   |   "
        print(self.dashboard_state)

    def reset_dashboard(self):
        self.x11 = ' '
        self.x12 = ' '
        self.x13 = ' '
        self.x21 = ' '
        self.x22 = ' '
        self.x23 = ' '
        self.x31 = ' '
        self.x32 = ' '
        self.x33 = ' '
        selfdashboard_state = self.update_dashboard()

    def get_all_lines(self):
        return [self.line1, self.line2, self.line3, self.colum1, self.colum2, self.colum3, self.diagonal1, self.diagonal2]

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
        return [self.x11, self.x12, self.x13]

    @property
    def line2(self):
        return [self.x21, self.x22, self.x23]

    @property
    def line3(self):
        return [self.x31, self.x32, self.x33]

    @property
    def colum1(self):
        return [self.x11, self.x21, self.x31]

    @property
    def colum2(self):
        return [self.x12, self.x22, self.x32]

    @property
    def colum3(self):
        return [self.x13, self.x23, self.x33]

    @property
    def diagonal1(self):
        return [self.x11, self.x22, self.x33]

    @property
    def diagonal2(self):
        return [self.x31, self.x22, self.x13]

    @property
    def full(self):
        if " " not in self.get_all_cells():
            return True

    @property
    def x11(self):
        return self._x11

    @property
    def x12(self):
        return self._x12

    @property
    def x13(self):
        return self._x13

    @property
    def x21(self):
        return self._x21

    @property
    def x22(self):
        return self._x22

    @property
    def x23(self):
        return self._x23

    @property
    def x31(self):
        return self._x31

    @property
    def x32(self):
        return self._x32

    @property
    def x33(self):
        return self._x33

    @property
    def dashboard_state(self):
        return self._dashboard_state

    @property
    def valid_cells(self):
        return self._valid_cells

    @x11.setter
    def x11(self, x11):
        if self._x11 == ' ':
            if x11 == 'x' or x11 == 'o':
                self._x11 = x11
                self.update_dashboard()
                return True
            else:
                print(f"select 'x' or 'o', not {x11}")
        else:
            print(f"Already selected, {self.x11}")

        return False

    @x12.setter
    def x12(self, x12):
        if self._x12 == ' ':
            if x12 == 'x' or x12 == 'o':
                self._x12 = x12
                self.update_dashboard()
                return True
            else:
                print(f"select 'x' or 'o', not {x12}")
        else:
            print(f"Already selected, {self.x12}")

        return False

    @x13.setter
    def x13(self, x13):
        if self._x13 == ' ':
            if x13 == 'x' or x13 == 'o':
                self._x13 = x13
                self.update_dashboard()
                return True
            else:
                print(f"select 'x' or 'o', not {x13}")
        else:
            print(f"Already selected, {self.x13}")

        return False

    @x21.setter
    def x21(self, x21):
        if self._x21 == ' ':
            if x21 == 'x' or x21 == 'o':
                self._x21 = x21
                self.update_dashboard()
                return True
            else:
                print(f"select 'x' or 'o', not {x21}")
        else:
            print(f"Already selected, {self.x21}")

        return False

    @x22.setter
    def x22(self, x22):
        if self._x22 == ' ':
            if x22 == 'x' or x22 == 'o':
                self._x22 = x22
                self.update_dashboard()
                return True
            else:
                print(f"select 'x' or 'o', not {x22}")
        else:
            print(f"Already selected, {self.x22}")

        return False

    @x23.setter
    def x23(self, x23):
        if self._x23 == ' ':
            if x23 == 'x' or x23 == 'o':
                self._x23 = x23
                self.update_dashboard()
                return True
            else:
                print(f"select 'x' or 'o', not {x23}")
        else:
            print(f"Already selected, {self.x23}")

        return False

    @x31.setter
    def x31(self, x31):
        if self._x31 == ' ':
            if x31 == 'x' or x31 == 'o':
                self._x31 = x31
                self.update_dashboard()
                return True
            else:
                print(f"select 'x' or 'o', not {x31}")
        else:
            print(f"Already selected, {self.x31}")

        return False

    @x32.setter
    def x32(self, x32):
        if self._x32 == ' ':
            if x32 == 'x' or x32 == 'o':
                self._x32 = x32
                self.update_dashboard()
                return True
            else:
                print(f"select 'x' or 'o', not {x32}")
        else:
            print(f"Already selected, {self.x32}")

        return False

    @x33.setter
    def x33(self, x33):
        if self._x33 == ' ':
            if x33 == 'x' or x33 == 'o':
                self._x33 = x33
                self.update_dashboard()
                return True
            else:
                print(f"select 'x' or 'o', not {x33}")
        else:
            print(f"Already selected, {self.x33}")

        return False

    @valid_cells.setter
    def valid_cells(self, valid_cells):
        self.valid_cells = valid_cells

    @dashboard_state.setter
    def dashboard_state(self, dashboard_state):
        self._dashboard_state = dashboard_state
