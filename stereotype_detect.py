relationship_keywords = ["daughter", "wife", "sister", "beti", "patni", "biwi", "behen", "maa", "bahu"]
profession_keywords = ["works as", "job", "engineer", "singer", "actor", "kaam", "naukri", "doctor"]

def detect_stereotypes(blocks):
    results = []
    for character, dialogue in blocks:
        dialogue_lower = dialogue.lower()
        stereotypes = []
        if any(r in dialogue_lower for r in relationship_keywords):
            stereotypes.append("relationship-based")
        if any(p in dialogue_lower for p in profession_keywords):
            stereotypes.append("profession-based")
        if stereotypes:
            gender = "female" if any(f in dialogue_lower for f in ["beti", "bahu", "wife", "daughter", "girl", "she", "her"]) else "male"
            results.append({
                "character": character,
                "gender": gender,
                "dialogue": dialogue,
                "stereotypes": stereotypes
            })
    return results