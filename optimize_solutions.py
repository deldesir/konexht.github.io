import yaml
import os

# Paths
INPUT_FILE = "/root/konexht-portal/_data/solutions.yml"
OUTPUT_FILE = "/root/konexht-portal/_data/solutions.yml"

# The Big 4 Strategy Mapping
CATEGORY_MAP = {
    # 💰 Business & Economy
    "Business": "Business & Economy",
    "Finance": "Business & Economy",
    "Agriculture": "Business & Economy",
    "Logistics": "Business & Economy",
    "Supply Chain": "Business & Economy",
    "Retail": "Business & Economy",
    "Trade": "Business & Economy",
    "Essential Logistics": "Business & Economy",
    "Retail Management": "Business & Economy",
    "Market Intelligence": "Business & Economy",
    "Entrepreneurship": "Business & Economy",
    
    # 🛡️ Safety & Infrastructure
    "Crisis Management": "Safety & Infrastructure",
    "Trust & Security": "Safety & Infrastructure",
    "Utility Services": "Safety & Infrastructure",
    "Safety": "Safety & Infrastructure",
    "Justice": "Safety & Infrastructure",
    "Legal": "Safety & Infrastructure",
    
    # 🎓 Education & Jobs
    "Education": "Education & Jobs",
    "Health": "Education & Jobs",
    "Healthcare": "Education & Jobs",
    "Professional Services": "Education & Jobs",
    "Literacy": "Education & Jobs",
    "Job Market": "Education & Jobs",
    
    # 🎭 Community & Culture
    "Social": "Community & Culture",
    "Culture": "Community & Culture",
    "Entertainment": "Community & Culture",
    "Hospitality": "Community & Culture",
    "Tourism": "Community & Culture",
    "Adventure": "Community & Culture",
    "Faith": "Community & Culture",
    "Community": "Community & Culture",
    "Social Utility": "Community & Culture",
    "Social Connection": "Community & Culture",
    "Cultural Gaming": "Community & Culture",
    "Hotel Management": "Community & Culture",
    "Local Services": "Community & Culture",
    
    # Fallback
    "General": "Community & Culture"
}

# Elite Tier Rules (Based on Impact/Effort)
def determine_tier(solution):
    impact = solution.get("metrics", {}).get("impact", 3)
    tech = solution.get("metrics", {}).get("tech", [])
    
    # Tier 1: High Impact AND Complex Tech (AI/Payments/API)
    if impact >= 5:
        return "elite"
    
    # Tier 2: Standard
    return "standard"

def optimize():
    print("Reading solutions...")
    with open(INPUT_FILE, 'r') as f:
        solutions = yaml.safe_load(f)
        
    optimized_count = 0
    elite_count = 0
    
    for sol in solutions:
        original_cat = sol.get("category", "General").split(" / ")[0] # Handle split cats like "Health / Agri"
        
        # 1. Update Category
        new_cat = CATEGORY_MAP.get(original_cat, "Social Fabric")
        sol["original_category"] = sol["category"]
        sol["category"] = new_cat
        
        # 2. Assign Tier
        sol["tier"] = determine_tier(sol)
        if sol["tier"] == "elite":
            elite_count += 1
            
        optimized_count += 1
        
    print(f"Optimized {optimized_count} solutions.")
    print(f"Assigned {elite_count} Elite tiers.")
    
    print("Writing back to YAML...")
    with open(OUTPUT_FILE, 'w') as f:
        yaml.dump(solutions, f, sort_keys=False, allow_unicode=True)
        
    print("Done!")

if __name__ == "__main__":
    optimize()
