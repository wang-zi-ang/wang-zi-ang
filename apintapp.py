import tkinter as tk

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Paint Tool")
        self.canvas = tk.Canvas(root, bg="white", width=800, height=600)
        self.canvas.pack()
        self.last_x, self.last_y = None, None
        self.canvas.bind('<Button-1>', self.on_button_press)
        self.canvas.bind('<B1-Motion>', self.on_move)

    def on_button_press(self, event):
        self.last_x, self.last_y = event.x, event.y

    def on_move(self, event):
        if self.last_x is not None and self.last_y is not None:
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y, fill="black", width=2)
        self.last_x, self.last_y = event.x, event.y

if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()