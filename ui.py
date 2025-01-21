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

        # Shape selection
        self.shape_label = tk.Label(root, text="Select Shape:")
        self.shape_label.pack()

        self.shape_var = tk.StringVar()
        self.shape_dropdown = ttk.Combobox(root, textvariable=self.shape_var)
        self.shape_dropdown['values'] = ["rectangle", "square", "round", "pipe"]
        self.shape_dropdown.pack()
        self.shape_dropdown.bind("<<ComboboxSelected>>", self.update_ui)

        # Dimension inputs (initially hidden)
        self.dimension_labels = {}
        self.dimension_vars = {}
        self.dimension_entries = {}

        for dimension in ["Width (mm):", "Height (mm):", "Diameter (mm):", "Wall Thickness (mm):"]:
            self.dimension_labels[dimension] = tk.Label(root, text=dimension)
            self.dimension_vars[dimension] = tk.DoubleVar()
            self.dimension_entries[dimension] = tk.Entry(root, textvariable=self.dimension_vars[dimension])

        # Calculate button
        self.calculate_button = tk.Button(root, text="Calculate Weight", command=self.calculate_weight)
        self.calculate_button.pack()

        # Result display
        self.result_label = tk.Label(root, text="Weight: ")
        self.result_label.pack()

    def update_ui(self, event):
        selected_shape = self.shape_var.get()
        
        # Hide all dimension inputs
        for label in self.dimension_labels.values():
            label.pack_forget()
        for entry in self.dimension_entries.values():
            entry.pack_forget()

        # Show relevant dimension inputs based on selected shape
        if selected_shape == "rectangle":
            self.dimension_labels["Width (mm):"].pack()
            self.dimension_entries["Width (mm):"].pack()
            self.dimension_labels["Height (mm):"].pack()
            self.dimension_entries["Height (mm):"].pack()
        elif selected_shape == "square":
            self.dimension_labels["Width (mm):"].pack()
            self.dimension_entries["Width (mm):"].pack()
        elif selected_shape == "round":
            self.dimension_labels["Diameter (mm):"].pack()
            self.dimension_entries["Diameter (mm):"].pack()
        elif selected_shape == "pipe":
            self.dimension_labels["Diameter (mm):"].pack()
            self.dimension_entries["Diameter (mm):"].pack()
            self.dimension_labels["Wall Thickness (mm):"].pack()
            self.dimension_entries["Wall Thickness (mm):"].pack()

    def calculate_weight(self):
        try:
            length = float(self.length_entry.get())
            width = float(self.width_entry.get())
            height = float(self.height_entry.get())
            shape = self.shape_var.get()
            material = self.material_var.get()

            profile_dimensions = {'length': length, 'width': width, 'height': height}
            if shape == 'round':
                profile_dimensions['diameter'] = float(self.diameter_entry.get())
            elif shape == 'pipe':
                profile_dimensions['outer_diameter'] = float(self.outer_diameter_entry.get())
                profile_dimensions['inner_diameter'] = float(self.inner_diameter_entry.get())

            weight = calculate_weight(profile_dimensions, material, shape)
            self.result_label.config(text=f"Weight: {weight:.2f} kg")
        except Exception as e:
            self.result_label.config(text=f"Error: {str(e)}")

if __name__ == '__main__':
    root = tk.Tk()
    app = BalustradeCalculator(root)
    root.mainloop()