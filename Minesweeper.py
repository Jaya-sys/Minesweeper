from tkinter import *
from cell import Cell
import settings
root=Tk()
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('Minesweeper')
root.configure(bg="black")
top_frame=Frame(root,bg="black", width=1440,height=180)
top_frame.place(x=0,y=0)
left_frame=Frame(root,bg="black",width=360,height=540)
left_frame.place(x=0,y=180)
center_frame=Frame(root,bg="black",width=1080,height=540)
center_frame.place(x=360,y=180)
for x in range(settings.GRID_SIZE):
	for y in range(settings.GRID_SIZE):
		c=Cell(y,x)
		c.create_button(center_frame)
		c.cell_button.grid(column=y,row=x)
# Cell.create_cell_count_label(left_frame)
#label
# Cell.create_cell_count_label.place(x=0,y=0 )
Cell.random_mines()
# print(Cell.all)
root.mainloop()
