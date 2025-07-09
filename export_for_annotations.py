import os
import pandas as pd
from data_ingestion import extract_text_from_pdf, extract_dialogue_blocks

# Choose the script you want to annotate
script_file = os.path.join(
    "data", "Bollywood-Data-master", "scripts-data", "Queen.pdf"  
)

# Extract text and dialogue blocks
text = extract_text_from_pdf(script_file)
blocks = extract_dialogue_blocks(text)

# Take a sample (e.g., first 100)
sample = blocks[:100]

# Create DataFrame for annotation
df = pd.DataFrame(sample, columns=["character", "dialogue"])
df["dialogue_id"] = range(1, len(df)+1)
df["stereotype_present"] = "" 
df["stereotype_type"] = ""     
df["gender"] = ""              

# Save to CSV
output_path = os.path.join("outputs", "manual_annotations.csv")
df.to_csv(output_path, index=False)
print(f"Annotation template saved to {output_path}")
