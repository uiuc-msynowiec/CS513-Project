import json

def remove_redundant_edits(filename):
    # Load data from the JSON file
    with open(filename, 'r') as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError("JSON must be a list of operations")

    cleaned_data = []
    prev_op = None
    prev_column = None

    for entry in data:
        current_op = entry.get("op")
        current_column = entry.get("columnName")

        if current_op == "core/mass-edit" and prev_op == "core/mass-edit" and current_column == prev_column:
            continue  # Skip this entry
        cleaned_data.append(entry)
        prev_op = current_op
        prev_column = current_column

    # Optionally overwrite the original file or save to a new one
    with open('filtered_' + filename, 'w') as f:
        json.dump(cleaned_data, f, indent=2)

    print(f"Filtered JSON saved as 'filtered_{filename}'")

# Example usage
remove_redundant_edits("Menu_cleaned.json")