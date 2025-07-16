filename = "myfile.txt"

vowels = 'aeiouAEIOU'

with open(filename, "r") as file:
    for line in file:
        line = line.strip()
        if line.startswith("Subject:"):
            count = 0
            for char in line:
                if char in vowels:
                    count += 1
            print(f"Line: {line} Vowels: {count}")