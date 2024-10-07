import tkinter as tk
from tkinter import messagebox

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.root.geometry("400x400")

        # Lista de tareas
        self.tasks = []
        self.completed_tasks = []

        # Frame principal
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(pady=10)

        # Etiqueta del título
        self.title_label = tk.Label(self.main_frame, text="Task Manager", font=("Arial", 16))
        self.title_label.pack()

        # Cuadro de entrada para agregar tareas
        self.task_entry = tk.Entry(self.main_frame, width=25, font=("Arial", 12))
        self.task_entry.pack(pady=5)

        # Botón para agregar tarea
        self.add_task_button = tk.Button(self.main_frame, text="Add Task", command=self.add_task)
        self.add_task_button.pack()

        # Lista de tareas (Listbox)
        self.task_listbox = tk.Listbox(self.main_frame, width=30, height=10, font=("Arial", 12), selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=5)

        # Botón para marcar la tarea como completada
        self.complete_task_button = tk.Button(self.main_frame, text="Mark as Completed", command=self.mark_as_completed)
        self.complete_task_button.pack(pady=5)

        # Barra de progreso
        self.progress_label = tk.Label(self.main_frame, text="Progress: 0%", font=("Arial", 12))
        self.progress_label.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def mark_as_completed(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            selected_task = self.task_listbox.get(selected_task_index)

            if selected_task not in self.completed_tasks:
                self.completed_tasks.append(selected_task)
                self.task_listbox.itemconfig(selected_task_index, {'fg': 'gray'})
                self.update_progress()
            else:
                messagebox.showinfo("Info", "Task already completed.")
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task.")

    def update_progress(self):
        total_tasks = len(self.tasks)
        completed_tasks = len(self.completed_tasks)
        if total_tasks > 0:
            progress = int((completed_tasks / total_tasks) * 100)
        else:
            progress = 0

        self.progress_label.config(text=f"Progress: {progress}%")

# Configuración de la ventana principal
root = tk.Tk()
app = TaskManagerApp(root)
root.mainloop()
