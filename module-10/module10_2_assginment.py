# Name: Devin G. Hyden
# Date: 13 August 2026
# Assignment: Module 10.2 Assignment

import tkinter as tk


class Todo(tk.Tk):
    def __init__(self, tasks=None):
        super().__init__()

        # Initialize the tasks list to keep track of added task widgets
        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks

        # Set window title using last name
        self.title("Hyden-ToDo")
        self.geometry("300x400")

        # Create a menu Bar with File -> Exit
        self.menu_bar = tk.Menu(self)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)

        # Command self.destroy closes and exits the application cleanly
        self.file_menu.add_command(label="Exit", command=self.destroy)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.config(menu=self.menu_bar)

        # Create Canvas and Frame widgets to enable vertical scrolling for tasks
        self.tasks_canvas = tk.Canvas(self)
        self.tasks_frame = tk.Frame(self.tasks_canvas)
        self.text_frame = tk.Frame(self)

        # Create vertical scrollbar and link it to the canvas
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.tasks_canvas.yview)
        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)

        # Text input widget for typing new task items
        self.task_create = tk.Text(self.text_frame, height=3, bg="white", fg="black")

        # Pack main components into the application layout
        self.tasks_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas_frame = self.tasks_canvas.create_window((0, 0), window=self.tasks_frame, anchor="nw")

        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()

        # Instruction label explaining how to delete tasks
        self.todo1 = tk.Label(
            self.tasks_frame,
            text="--- Items Added --- ** Right Click Item to Delete**",
            bg="#8A2BE2",
            fg="white"
        )
        self.todo1.pack(side=tk.TOP, fill=tk.X)

        # Flag variable to alternate row colors for styling
        self.color_toggle = True

        # Event bindings for pressing Enter and window resizing
        self.bind("<Return>", self.add_task)
        self.bind("<Configure>", self.on_frame_configure)
        self.tasks_canvas.bind("<Configure>", self.task_width)

        # Add initial tasks if passed during initialization
        for task in self.tasks:
            self.add_task(None, task)

    def add_task(self, event=None, task_text=None):
        """Reads user input from the text box and adds a formatted task to the list."""
        if not task_text:
            task_text = self.task_create.get("1.0", tk.END).strip()

        if len(task_text) > 0:
            # Alternate colors
            if self.color_toggle:
                bg_color = "#E6B800"  # Gold accent
                fg_color = "black"
            else:
                bg_color = "#8A2BE2"  # Purple accent
                fg_color = "white"

            # Toggle boolean for the next added task
            self.color_toggle = not self.color_toggle

            # Create new task widget using styled Label
            new_task = tk.Label(self.tasks_frame, text=task_text, bg=bg_color, fg=fg_color, pady=5)

            # Change delete action to Right Mouse Click
            new_task.bind("<Button-3>", self.remove_task)
            new_task.bind("<Button-2>", self.remove_task)

            new_task.pack(side=tk.TOP, fill=tk.X)
            self.tasks.append(new_task)

        # Clear input field after task is created
        self.task_create.delete("1.0", tk.END)

    def remove_task(self, event):
        """Removes the right-clicked task label widget from the frame and list."""
        task = event.widget
        if task in self.tasks:
            self.tasks.remove(task)
            task.destroy()

    def on_frame_configure(self, event):
        """Updates the scrollable area when task list content dimensions change."""
        self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))

    def task_width(self, event):
        """Dynamically resizes task labels to match window width changes."""
        canvas_width = event.width
        self.tasks_canvas.itemconfig(self.canvas_frame, width=canvas_width)


if __name__ == "__main__":
    # Initialize and start the GUI application loop
    todo = Todo()
    todo.mainloop()