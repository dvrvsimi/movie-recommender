# from tkinter import *
# import tkinter as tk
#
# root = tk.Tk()
# root.title('Dara\'s Netflix Recommendations')
# root.geometry("1000x1000")
# root.configure(background="black")
#
# canvas = tk.Canvas(root, height=600, width=1000)
# canvas.pack()
# photo = tk.PhotoImage(file="image.gif")
# canvas.create_image(20, 20, anchor="nw", image=photo)  #.grid(row=0, column=0, sticky=CENTER)
# root.mainloop()
from tkinter import *
from PIL import ImageTk, Image

# root definition
root = Tk()
root.title('Dara\'s Netflix Recommendations')
root.geometry("1336x1080")
root.configure(background="black")
# frame definition
frame = Frame(root, width=400, height=400)
frame.place(anchor='center', relx=0.5, rely=0.4)
# image definitions
image = ImageTk.PhotoImage(Image.open("img.jpg"))
image1 = PhotoImage(file= r"image1.png")
image2 = PhotoImage(file= r"image2.png")
image3 = PhotoImage(file= r"image3.png")


# label to display the image
label = Label(frame, image=image)
label.pack()

# label for inserting text
label1 = Label(root, text="what would you like to watch?", background="black", foreground="white", font="Poppins 18 bold")
label1.grid(row=0, column=0, padx=480, pady=410, sticky="")

# label.place(anchor="center", relx=0.5, rely=0.68)

# buttons
button = Button(root, text="action", width=20, height=10, command="click")
button.place(anchor="center", relx=0.1, rely=0.73)

button1 = Button(root, text="mystery", width=20, height=10, command="click")
button1.place(anchor="center", relx=0.3, rely=0.73)

button2 = Button(root, text="thriller", width=20, height=10, command="click")
button2.place(anchor="center", relx=0.5, rely=0.73)

button3 = Button(root, text="anime", width=20, height=10, command="click")
button3.place(anchor="center", relx=0.7, rely=0.73)

button4 = Button(root, text="psychological", width=20, height=10, command="click")
button4.place(anchor="center", relx=0.9, rely=0.73)

# label1 = Label(root, text="[1] action [2] psychological [3] thriller [4] comedy [5] romance [7] binge worthy series [8] anime [9] kdrama ", bg="black", fg="white", font="none 12 normal")
# label1.place(anchor="center", relx=0.5, rely=0.73)
# # label.grid(row=1, column=0, sticky=W)
#
# # text entry box
# hex_value = "#f5f5f5"
# feedback = Entry(root, bg=hex_value, width=7)
# feedback.place(anchor="center", relx=0.24, rely=0.8)
#
# # button
# Button(root, text="let\'s go!", width=12, command="click").place(anchor="center", relx=0.259, rely=0.85)




# new windows
root.mainloop()