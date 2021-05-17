

class Row:
    def __init__(self):
        self.id = 0
        self.unfounds = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    def __str__(self):
        text = f"Row id:{self.id}"
        return text

    @staticmethod
    def create_rows():
        rows = list()
        for i in range(9):
            row = Row()
            row.id = i
            rows.append(row)
        return rows

    @property
    def founds(self):
        founds = set()
        for i in range(1,10):
            if i not in self.unfounds:
                founds.add(i)
        return founds

class Column:
    def __init__(self):
        self.id = 0
        self.unfounds = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    def __str__(self):
        text = f"Column id:{self.id}"
        return text

    @staticmethod
    def create_columns():
        columns = list()
        for i in range(9):
            col = Column()
            col.id = i
            columns.append(col)
        return columns

    @property
    def founds(self):
        founds = set()
        for i in range(1,10):
            if i not in self.unfounds:
                founds.add(i)
        return founds


class Region:
    def __init__(self):
        self.id = 0
        self.unfounds = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    def __str__(self):
        text = f"Region id:{self.id}"
        return text

    @staticmethod
    def create_regions():
        regions = list()
        for i in range(9):
            reg = Region()
            reg.id = i
            regions.append(reg)
        return regions

    @property
    def founds(self):
        founds = set()
        for i in range(1,10):
            if i not in self.unfounds:
                founds.add(i)
        return founds

    def find_region(row, column):
        if row<3 and column<3:
            return 0
        elif row<3 and column<6:
            return 1
        elif row<3 and column<9:
            return 2
        elif row<6 and column<3:
            return 3
        elif row<6 and column<6:
            return 4
        elif row<6 and column<9:
            return 5
        elif row<9 and column<3:
            return 6
        elif row<9 and column<6:
            return 7
        elif row<9 and column<9:
            return 8

class Cell:
    def __init__(self):
        self.id = 0
        self.row = 'foreignkey'
        self.column = 'foreignkey'
        self.region = 'foreignkey'
        self.non_possible = set()  #set olabilir
        self.value = 0
        self.given = False

    def __repr__(self):
        text = f"{self.value}"
        return text

    @staticmethod
    def create_cells():
        cells = list()
        rows = Row.create_rows()
        columns = Column.create_columns()
        regions = Region.create_regions()
        for r in range(9):
            for c in range(9):
                cell = Cell()
                cell.id = (9*r)+c
                cell.row = rows[r]
                cell.column = columns[c]
                cell.region = regions[Region.find_region(c,r)]
                cells.append(cell)
        return {
                "rows": rows,
                "columns": columns,
                "regions": regions,
                "cells": cells,
        }

    def set_value(self, value):
        '''
            el ile hücreye rakam girişi
        '''
        self.value = value
        self.row.unfounds.remove(value)
        self.column.unfounds.remove(value)
        self.region.unfounds.remove(value)
        if len(self.non_possible) < 8:
            for i in range(1,10):
                if i != value:
                    self.non_possible.add(i)

    def find_value(self):
        '''
            Döngüde çalışacak. Satır, sütun ve bölgeyi kontrol edip eğer seçilen hücrenin değeri kesinleşmişse aatama yapacak
        '''
        for i in self.row.founds:
            self.non_possible.add(i)
        for i in self.column.founds:
            self.non_possible.add(i)
        for i in self.region.founds:
            self.non_possible.add(i)
        if len(self.non_possible) == 8:
            for i in range(1,10):
                if i not in self.non_possible:
                    self.set_value(i)
