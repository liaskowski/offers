# calculations.py

def get_material_density(material: str) -> float:
    """Retrieve the density of the specified steel material."""
    densities = {
        "steel": 7850,  # Density in kg/m^3
        # Add more materials and their densities as needed
    }
    return densities.get(material.lower(), 0)

def calculate_weight(profile_dimensions: dict, material: str) -> float:
    """Calculate the weight of the steel structure based on dimensions and material."""
    density = get_material_density(material)
    if density == 0:
        raise ValueError("Material not found.")
    
    # Example calculation: weight = volume * density
    volume = profile_dimensions['length'] * profile_dimensions['width'] * profile_dimensions['height']  # in m^3
    weight = volume * density  # in kg
    return weight