import tkinter as tk
from tkinter import ttk
from calculations import calculate_weight, get_material_density

class BalustradeCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Balustrade Weight Calculator")

        # Material selection
        self.material_label = tk.Label(root, text="Select Material:")
        self.material_label.pack()

        self.material_var = tk.StringVar()
        self.material_dropdown = ttk.Combobox(root, textvariable=self.material_var)
        self.material_dropdown['values'] = ["steel"]  # Add more materials as needed
        self.material_dropdown.pack()

        # Dimension inputs
        self.length_label = tk.Label(root, text="Length (m):")
        self.length_label.pack()
        self.length_entry = tk.Entry(root)
        self.length_entry.pack()

        self.width_label = tk.Label(root, text="Width (m):")
        self.width_label.pack()
        self.width_entry = tk.Entry(root)
        self.width_entry.pack()

        self.height_label = tk.Label(root, text="Height (m):")
        self.height_label.pack()
        self.height_entry = tk.Entry(root)
        self.height_entry.pack()

        # Calculate button
        self.calculate_button = tk.Button(root, text="Calculate Weight", command=self.calculate_weight)
        self.calculate_button.pack()

        # Result display
        self.result_label = tk.Label(root, text="Weight: ")
        self.result_label.pack()

    def calculate_weight(self):
        try:
            length = float(self.length_entry.get())
            width = float(self.width_entry.get())
            height = float(self.height_entry.get())
            material = self.material_var.get()

            profile_dimensions = {'length': length, 'width': width, 'height': height}
            weight = calculate_weight(profile_dimensions, material)
            self.result_label.config(text=f"Weight: {weight:.2f} kg")
        except Exception as e:
            self.result_label.config(text=f"Error: {str(e)}")

if __name__ == '__main__':
    root = tk.Tk()
    app = BalustradeCalculator(root)
    root.mainloop()