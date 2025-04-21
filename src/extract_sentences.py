import os
import json
import nltk
from nltk.tokenize import sent_tokenize

# nltk.download('punkt')

def process_txt_files(base_dir, output_dir):
    print(f"\nSearching for .txt files in: {base_dir}")

    for root, dirs, files in os.walk(base_dir):
        for filename in files:
            if filename.endswith('.txt'):
                txt_path = os.path.join(root, filename)
                print(f"➤ Reading file: {txt_path}")
                
                try:
                    with open(txt_path, 'r', encoding='utf-8') as f:
                        text = f.read()

                    sentences = sent_tokenize(text, language='spanish')

                    json_filename = os.path.splitext(filename)[0] + '.json'
                    output_path = os.path.join(output_dir, json_filename)

                    with open(output_path, 'w', encoding='utf-8') as out:
                        json.dump(sentences, out, ensure_ascii=False, indent=2)

                    print(f"    ✔ Saved to: {output_path} ({len(sentences)} sentences)\n")

                except Exception as e:
                    print(f"    ✖ Error processing {txt_path}: {e}\n")


base_dir = "../granma-txts"
output_dir = "generated-jsons"
os.makedirs(output_dir, exist_ok=True)

for folder_name in os.listdir(base_dir):
    folder_path = os.path.join(base_dir, folder_name)
    if os.path.isdir(folder_path):
        print(f"\n📁 Processing folder: {folder_name}")
        process_txt_files(folder_path, output_dir)
