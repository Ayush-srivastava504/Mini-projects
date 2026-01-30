#!/usr/bin/env python3

import os

def main():
    print("Text File Sentence Remover")
    print("=" * 50)
    
    filename = input("Enter filename (default: textfile.txt): ").strip()
    if not filename:
        filename = "textfile.txt"
    
    print("\nEnter text below. Type 'END' on a new line when finished:")
    lines = []
    while True:
        try:
            line = input()
            if line == "END":
                break
            lines.append(line)
        except EOFError:
            break
    
    text_content = '\n'.join(lines)
    
    with open(filename, 'w') as f:
        f.write(text_content)
    
    print(f"\nText saved to {filename}")
    print("\n" + "=" * 50)
    
    if not os.path.exists(filename):
        print("Error: File not created.")
        return
    
    with open(filename, 'r') as f:
        content = f.read()
    
    if not content.strip():
        print("File is empty. Nothing to remove.")
        return
    
    print("Current file content:")
    print("-" * 50)
    print(content)
    print("-" * 50)
    
    target = input("\nEnter exact sentence to remove: ").strip()
    
    if not target:
        print("No sentence provided. Exiting.")
        return
    
    if target in content:
        new_content = content.replace(target, "", 1)
        
        print("\nModified content:")
        print("-" * 50)
        print(new_content)
        print("-" * 50)
        
        save = input("\nSave changes? (y/n): ").strip().lower()
        if save == 'y':
            with open(filename, 'w') as f:
                f.write(new_content)
            print(f"Changes saved to {filename}")
        else:
            print("Changes discarded.")
    else:
        print(f"Sentence not found in {filename}")

if __name__ == "__main__":
    main()