from tkinter import Button,Label
import random
import settings
import sys
import ctypes

class Cell:
    all=[]
    cell_count_label_object=None
    def __init__(self,x,y,is_mine=False):
        self.is_mine=is_mine
        self.cell_button=None
        self.x=x
        self.y=y
        Cell.all.append(self)
    def create_button(self,location):
        button=Button(
            location,
            width=12,
            height=4,
            # text=f"{self.y},{self.x}"
            )
        button.bind('<Button-1>',self.left_click)#left_click
        button.bind('<Button-3>',self.right_click)#right_click
        self.cell_button=button
    # @staticmethod
    # def create_cell_count_label(location):
    #     lbl=Label( bg="black",
    #         fg="white"
    #         location,text=f"Cells Left:{settings.CELL_COUNT}")
    #     cell_count_label_object=lbl

    def left_click(self,event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mine_length==0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()
    def get_cell_by_axis(self,y,x):
        for cell in Cell.all:
            if cell.y==y and cell.x==x:
                return cell
    @property
    def surrounded_cells(self):
        # print(self.get_cell_by_axis(0,0))
        cells=[
              self.get_cell_by_axis(self.y-1,self.x-1),
              self.get_cell_by_axis(self.y-1,self.x),
              self.get_cell_by_axis(self.y-1,self.x+1),
              self.get_cell_by_axis(self.y,self.x-1),
              self.get_cell_by_axis(self.y+1,self.x-1),
              self.get_cell_by_axis(self.y+1,self.x),
              self.get_cell_by_axis(self.y+1,self.x+1),
              self.get_cell_by_axis(self.y,self.x+1),

        ]
        cells=[cell for cell in cells if cell is not None]
        return cells
    @property
    def surrounded_cells_mine_length(self):
        counter=0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter+=1
        return counter
    def show_cell(self):
        self.cell_button.configure(text=self.surrounded_cells_mine_length)
    def show_mine(self):
        self.cell_button.configure(bg="blue")
        ctypes.windll.user32.MessageBoxW(0,'You clicked on a mine','Game Over',0)
        sys.exit()
    def right_click(self,event):
        print("you have clicked the right button")
    def random_mines():
        picked_random_mines=random.sample(Cell.all,9)
        for picked_random_mines in picked_random_mines:
            picked_random_mines.is_mine=True
    def __repr__(self):
        return f"Cell{self.y},{self.x}"

