##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)

# Insert your code here to draw the house!

houseBody = drawpad.create_rectangle(300,300,500,500,fill = 'red')
houseRoof = drawpad.create_line(300,300,400,180,fill = 'black')
houseRoof2 = drawpad.create_line(500,300,400,180,fill = 'black')
houseDoor = drawpad.create_rectangle(375,415,425,500, fill = 'brown')
window1 = drawpad.create_rectangle(310,320,350,360, fill = 'white')
window2 = drawpad.create_rectangle(450,320,490,360, fill = 'white')
window3 = drawpad.create_rectangle(310,400,350,440, fill = 'white')
window4 = drawpad.create_rectangle(450,400,490,440, fill = 'white')
doorhandle = drawpad.create_oval(420,475,423,470, fill = 'gold')
grass = drawpad.create_rectangle(200,500,600,525, fill = 'green')
chim1 = drawpad.create_line(500,300,500,200)
chim2 = drawpad.create_line(500,200,450,200)
chim3 = drawpad.create_line(450,200,450,240)
root.mainloop()