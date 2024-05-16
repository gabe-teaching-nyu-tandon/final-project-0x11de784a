import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from src.v_eff_factory import VeffFactory
from src.v_eff import Veff

filename = "mock_yml.yml"

class GUI():

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("GUI")

        self.label = tk.Label(self.root, text="Your Message", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.entry = tk.Entry(self.root, font=('Arial', 16))
        self.entry.bind("<KeyPress>", self.shortcut)
        self.entry.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text="Show Messagebox", font=('Arial', 16), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Show Message", font=('Arial', 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.clrbutton = tk.Button(self.root, text="Clear", font=('Arial', 18), command=self.clear)
        self.clrbutton.pack(padx=10, pady=10)

        self.root.mainloop()
    
    def show_message(self):
        if self.check_state.get() == 0:
            print(self.entry.get())
        else:
            messagebox.showinfo(title="Message", message=self.entry.get())

    def shortcut(self, event):
        if event.state == 12 and event.keysym == "Return":
            self.show_message()

    def clear(self):
        self.entry.delete(0, 'end')


# GUI()


class Visualizer:
    def __init__(self, veff_data, E_value):
        self.root = tk.Tk()
        self.root.title("0x11de784a")

        # Create a frame to hold the plots
        self.plot_frame = tk.Frame(self.root)
        self.plot_frame.pack(fill=tk.BOTH, expand=1)

        # Create two plots side by side
        self.plot1 = VeffPlot(self.plot_frame, veff_data, E_value)
        self.plot1.canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        self.Veff_plot = VeffPlot(self.plot_frame, veff_data, E_value)
        self.Veff_plot.canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        # Input frame
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(padx=10, pady=10)

        # Orbital Category Input
        self.category_label = tk.Label(self.input_frame, text="Orbit Category:", font=('Arial', 12))
        self.category_label.pack(side=tk.LEFT, padx=5)

        self.C_entry = tk.Entry(self.input_frame, font=('Arial', 16))
        self.C_entry.bind("<KeyPress>", self.C_input_handler)
        self.C_entry.pack(side=tk.LEFT, padx=5)

        # Angular Momentum Input
        self.AngularMomentum_label = tk.Label(self.input_frame, text="L:", font=('Arial', 12))
        self.AngularMomentum_label.pack(side=tk.LEFT, padx=5)

        self.L_entry = tk.Entry(self.input_frame, font=('Arial', 16))
        self.L_entry.bind("<KeyPress>", self.L_input_handler)
        self.L_entry.pack(side=tk.LEFT, padx=5)

        # Energy Input
        self.Energy_label = tk.Label(self.input_frame, text="E:", font=('Arial', 12))
        self.Energy_label.pack(side=tk.LEFT, padx=5)

        self.E_entry = tk.Entry(self.input_frame, font=('Arial', 16))
        self.E_entry.bind("<KeyPress>", self.E_input_handler)
        self.E_entry.pack(side=tk.LEFT, padx=5)

        self.root.mainloop()

    def C_input_handler(self, event):
        valid_keys = ['1', '2', '3', '4', '\b', '\r']  # backspace and enter
        if event.char in valid_keys:
            if event.char == '\r':
                return
        else:
            return "break"  # ignore the key press
    
    def L_input_handler(self, event):
        valid_keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '\r', '\b']
        if event.char in valid_keys:
            if event.char == '\r':
                veff_new = VeffFactory().create(float(self.L_entry.get()))
                self.Veff_plot.update_plot(veff_new.Veff_values)
                print("updated Veff Plot")
        else:
            return "break"  # ignore the key press

    def E_input_handler(self, event):
        valid_keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '\r', '\b']
        if event.char in valid_keys:
            if event.char == '\r':
                E_value = float(float(self.E_entry.get()))
                self.Veff_plot.update_E_line(E_value)
                print("updated E line")
        else:
            return "break"  # ignore the key press

class VeffPlot:
    def __init__(self, master, data, E_value):
        self.master = master
        self.data = data
        self.E_value = E_value
        self.figure = Figure(figsize=(8, 6), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.plot_veff_values()
        self.canvas = FigureCanvasTkAgg(self.figure, master=master)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def plot_veff_values(self):
        self.ax.plot(self.data[250:, 0], self.data[250:, 1], label='Effective Potential')
        self.ax.set_title('Effective Potential')
        self.ax.set_xlabel('Radius (r)')
        self.ax.set_ylabel('Veff Value')
        self.ax.legend()
        self.ax.set_xscale('log')
        self.ax.grid(True)
        self.ax.axhline(y=0.5*(self.E_value**2), color='r', linestyle='--', label='E Value')  # draw E line

    def update_plot(self, new_data):
        self.ax.clear()
        self.data = new_data
        self.plot_veff_values()
        self.canvas.draw()

    def update_E_line(self, new_E_value):
        self.ax.clear()
        self.E_value = new_E_value
        self.plot_veff_values()
        self.canvas.draw()