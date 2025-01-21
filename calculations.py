# calculations.py
def __init__(self, root):
    # Existing initialization code...
    
    # Shape selection
    self.shape_var.trace('w', self.update_shape_inputs)  # Add trace to call method on change

def update_shape_inputs(self, *args):
    """Update the UI based on the selected shape."""
    shape = self.shape_var.get()
    
    # Hide all dimension fields initially
    self.diameter_label.pack_forget()
    self.diameter_entry.pack_forget()
    self.outer_diameter_label.pack_forget()
    self.outer_diameter_entry.pack_forget()
    self.inner_diameter_label.pack_forget()
    self.inner_diameter_entry.pack_forget()
    self.wall_thickness_label.pack_forget()
    self.wall_thickness_entry.pack_forget()
    
    # Show relevant fields based on shape
    if shape == 'round':
        self.diameter_label.pack()
        self.diameter_entry.pack()
    elif shape == 'pipe':
        self.outer_diameter_label.pack()
        self.outer_diameter_entry.pack()
        self.inner_diameter_label.pack()
        self.inner_diameter_entry.pack()
        self.wall_thickness_label.pack()
        self.wall_thickness_entry.pack()
    else:
        self.length_label.pack()
        self.length_entry.pack()
        self.width_label.pack()
        self.width_entry.pack()
        self.height_label.pack()
        self.height_entry.pack()
        
        
def get_material_density(material: str) -> float:
    """Retrieve the density of the specified steel material."""
    densities = {
        "steel": 7850,  # Density in kg/m^3
        # Add more materials and their densities as needed
    }
    return densities.get(material.lower(), 0)

def calculate_weight(profile_dimensions: dict, shape: str) -> float:
    """Calculate the weight of the steel structure based on dimensions and shape."""
    density = 7850  # Density of steel in kg/m^3

    if shape == 'rectangle':
        volume = profile_dimensions['length'] * profile_dimensions['width'] * profile_dimensions['height']  # in m^3
    elif shape == 'square':
        volume = profile_dimensions['length'] ** 2 * profile_dimensions['height']  # in m^3
    elif shape == 'round':
        radius = profile_dimensions['diameter'] / 2
        volume = 3.14159 * (radius ** 2) * profile_dimensions['length']  # in m^3
    elif shape == 'pipe':
        outer_radius = profile_dimensions['outer_diameter'] / 2
        inner_radius = profile_dimensions['inner_diameter'] / 2
        volume = 3.14159 * (outer_radius ** 2 - inner_radius ** 2) * profile_dimensions['length']  # in m^3
    else:
        raise ValueError("Invalid shape selected.")

    weight = volume * density  # in kg
    return weight