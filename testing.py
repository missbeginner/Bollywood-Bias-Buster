import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score

# Load manual annotations
manual = pd.read_csv("outputs/manual_annotations.csv")

# Simple keyword-based stereotype detector (should match your model logic)
relationship_keywords = ["beti", "bahu", "shaadi", "pati", "wife", "daughter"]
profession_keywords = ["kaam", "job", "engineer", "doctor", "singer", "actor"]

def model_stereotype_detector(dialogue):
    text = str(dialogue).lower()
    if any(k in text for k in relationship_keywords + profession_keywords):
        return 1
    return 0

# Run model on the same dialogues
manual['model_stereotype_present'] = manual['dialogue'].apply(model_stereotype_detector)

# Save model predictions
model_pred = manual[['dialogue_id', 'model_stereotype_present']]
model_pred.rename(columns={'model_stereotype_present': 'stereotype_present'}, inplace=True)
model_pred.to_csv("outputs/model_predictions.csv", index=False)
print("Model predictions saved to outputs/model_predictions.csv")

# Prepare for evaluation
# Replace <null> with 0, then fillna and convert to int
manual['stereotype_present'] = manual['stereotype_present'].replace('<null>', 0).fillna(0).astype(int)
manual['model_stereotype_present'] = manual['model_stereotype_present'].fillna(0).astype(int)

# Calculate metrics
precision = precision_score(manual['stereotype_present'], manual['model_stereotype_present'])
recall = recall_score(manual['stereotype_present'], manual['model_stereotype_present'])
f1 = f1_score(manual['stereotype_present'], manual['model_stereotype_present'])

print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1 Score: {f1:.2f}")

