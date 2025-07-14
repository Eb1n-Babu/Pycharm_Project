import json

# Python dictionary
python_data = {
    "name": "Ebin",
    "skills": ["Python", "Multithreading", "File Handling"],
    "level": "Intermediate"
}

# Convert dictionary to JSON string
json_data = json.dumps(python_data, indent=4)

# Print JSON result
print(json_data)

# Save JSON data to a file
with open("data.json", "w") as json_file:
    json.dump(python_data, json_file, indent=4)

print("JSON file created successfully!")