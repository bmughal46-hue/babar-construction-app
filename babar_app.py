# Construction Material Calculator - Babar Real Estate
def get_material_estimates(size_label):
    # Base calculation for 1 Marla (approximate values)
    # Aap in ratios ko apni requirement ke mutabiq adjust kar sakte hain
    base_bricks = 4500
    base_cement = 90
    base_steel = 0.4 # Tons
    base_bajri = 90  # Cft

    # Mapping sizes to multipliers
    # Yahan hum check karte hain ke kitne Marla ya Kanal hain
    multipliers = {
        "3 Marla": 3,
        "4 Marla": 4,
        "4 Marla Building": 5.5,    # Building ke liye extra material
        "5 Marla": 5,
        "7 Marla": 7,
        "8 Marla": 8,
        "8 Marla Building": 10.5,   # Building ke liye extra
        "10 Marla": 10,
        "16 Marla Building": 20,    # Multi-story or large area
        "1 Kanal": 20,              # 1 Kanal = 20 Marla
        "2 Kanal": 40,
        "4 Kanal": 80,
        "4 Kanal Commercial": 100   # Commercial projects require more strength
    }

    m = multipliers.get(size_label, 0)

    results = {
        "Bricks": int(base_bricks * m),
        "Cement": int(base_cement * m),
        "Steel": round(base_steel * m, 2),
        "Bajri": int(base_bajri * m)
    }
    return results

# --- List for your Dropdown Menu ---
all_options = [
    "3 Marla", "4 Marla", "4 Marla Building", "5 Marla", 
    "7 Marla", "8 Marla", "8 Marla Building", "10 Marla", 
    "16 Marla Building", "1 Kanal", "2 Kanal", 
    "4 Kanal", "4 Kanal Commercial"
]

# Example Usage:
selected = "5 Marla" # User yahan se select karega
data = get_material_estimates(selected)
print(f"Results for {selected}: {data}")
