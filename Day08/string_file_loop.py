filename = "myfile.txt"

with open(filename, "r") as file:
    for line in file:
        line = line.strip()
        if line.startswith("Subject:"):
            print(line.upper())