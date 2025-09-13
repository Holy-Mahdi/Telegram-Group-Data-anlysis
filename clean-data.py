import json
import csv
import re 


with open("result.json", "r", encoding="utf-8") as f :
    data = json.load(f)


messages = []
for msg in data.get("messages", []):
    if isinstance(msg.get("text"), str):
        messages.append(msg["text"])
    elif isinstance(msg.get("text_entities"), list):
        for ent in msg["text_entities"]:
            if "text" in ent and isinstance(ent["text"], str):
                messages.append(ent["text"])


def clean_text(s):
    return re.sub(r"[^\w\s\u0600-\u06FF]", "", s).strip() 


cleaned = [clean_text(m) for m in messages if m.strip()]


with open("cleaned_messages.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["message"])  # header
    for msg in cleaned:
        writer.writerow([msg])

print(f"Saved {len(cleaned)} messages to cleaned_messages.csv ✅")