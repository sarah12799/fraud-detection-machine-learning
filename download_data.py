import gdown
import os

# Create local data folder if not exists
os.makedirs("data", exist_ok=True)

# Google Drive file IDs
FILES = {
    "tabular_data.csv": "1KpmWHkOaTeK5Jyp7I5lr3igetChtl2Qh", 
    "graph_data.csv": "1DTzhybsNBzFswm4gvmM8-Kbtayxq6xw2"     
}

# Download each file
for filename, file_id in FILES.items():
    url = f"https://drive.google.com/uc?id={file_id}"
    output_path = os.path.join("data", filename)
    print(f"⬇️  Downloading {filename} ...")
    gdown.download(url, output_path, quiet=False)

print("\n✅ All data files downloaded successfully into ./data/")
