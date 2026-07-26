import os

path = r"C:\\Users\\ihita\\OneDrive - Lake Washington School District\\_2025-2026\\Other\\Research\\PDFs\\1.1.txt"

print("File exists:", os.path.exists(path))

with open(path, "r", encoding="utf-8") as f:
    text = f.read()

print("Number of characters:", len(text))
print("First 200 characters:")
print(repr(text[:200]))