
import tkinter

def centerWidget(widget_root, root_width, root_height, hoizontal_shift, vertical_shift):
  screen_width = widget_root.winfo_screenwidth()
  screen_height = widget_root.winfo_screenheight()
  x = (screen_width // 2) - (root_width // 2) + hoizontal_shift
  y = (screen_height // 2) - (root_height // 2) + vertical_shift
  widget_root.geometry(f"{root_width}x{root_height}+{x}+{y}")


lst = (8, 'red'), (6, 'yellow'), (8, 'blue'), (2, 'yellow')

# Root Paraemeters
root_width = 300
root_height = 300
h_shift = 0
v_shift = -100

# Root Main
root = tkinter.Tk()
root.title('Player Card')
centerWidget(root, root_width, root_height, h_shift, v_shift)

for n in lst:
  
root.mainloop()
