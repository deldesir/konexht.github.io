import os
import re
import yaml

# Path to the booklets
BOOKLET_DIR = "/root/.gemini/antigravity/brain/bbab2d6b-93fb-4fde-b60b-733771a6cec8"
OUTPUT_FILE = "/root/konexht-portal/_data/solutions.yml"

def parse_booklet(filepath):
    solutions = []
    current_solution = None
    
    with open(filepath, 'r') as f:
        content = f.read()
        
    # Split by ### headers
    sections = re.split(r'### \d+\.', content)
    
    for section in sections[1:]: # Skip the intro
        lines = section.strip().split('\n')
        if not lines:
            continue
            
        name = lines[0].strip()
        pitch_match = re.search(r'> \*\*Pitch\*\*: (.*)', section)
        pitch = pitch_match.group(1) if pitch_match else ""
        
        # Extract table data
        table_rows = re.findall(r'\| \*\*([^*|]+)\*\* \| ([^|]+) \|', section)
        metadata = {k.strip(): v.strip() for k, v in table_rows}
        
        # Extract Value Proposition
        vp_match = re.search(r'\*\*Value Proposition\*\*: (.*)', section)
        val_prop = vp_match.group(1) if vp_match else ""
        
        # Generate a clean ID
        service_id_raw = metadata.get("Service ID", name).replace("`", "").strip()
        clean_id = re.sub(r'[^A-Z0-9]', '-', service_id_raw.upper())
        
        # Map to our YAML schema
        solution = {
            "id": clean_id,
            "name": name,
            "category": metadata.get("Category", "General"),
            "pitch": pitch,
            "tier": "standard",
            "status": "Concept",
            "metrics": {
                "impact": 4 if "Premium" in name else 3,
                "hustle": 2 if "Low" in metadata.get("Effort Level", "") else 4,
                "roi": "Medium",
                "effort": metadata.get("Effort Level", "Medium")
            },
            "tech": ["RapidPro", "WhatsApp"],
            "logic": val_prop[:100] + "..." if len(val_prop) > 100 else val_prop,
            "whatsapp_message": metadata.get("Ex. Message", "").replace('"', "").strip(),
            "strategy_analysis": {
                "strengths": val_prop,
                "limitations": "Standard deployment constraints.",
                "growth_path": "Scale via regional WhatsApp hubs.",
                "market_risk": "User adoption speed."
            }
        }
        
        # Special handling for premium tags
        if "Premium" in section or "🟦 🟦 🟦" in section:
            solution["tier"] = "premium"
            solution["metrics"]["impact"] = 5
            
        solutions.append(solution)
        
    return solutions

def main():
    all_solutions = []
    booklets = [f for f in os.listdir(BOOKLET_DIR) if f.startswith("booklet_") and f.endswith(".md") and f != "booklet_index.md" and f != "booklet_security.md"]
    
    for booklet in booklets:
        print(f"Parsing {booklet}...")
        path = os.path.join(BOOKLET_DIR, booklet)
        all_solutions.extend(parse_booklet(path))
        
    print(f"Total solutions extracted: {len(all_solutions)}")
    
    with open(OUTPUT_FILE, 'w') as f:
        yaml.dump(all_solutions, f, sort_keys=False, allow_unicode=True)
        
    print(f"Successfully wrote to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
