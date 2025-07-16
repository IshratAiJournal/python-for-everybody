filename = "myfile.txt"

vowels = 'aeiouAEIOU'
subject_count = 0

with open(filename, "r") as file:
    for line in file:
        line = line.strip()
        if line.startswith("Subject:"):
            subject_count += 1

            vowel_count = 0
            word_count = len(line.split())

            for char in line:
                if char in vowels:
                    vowel_count += 1

            print(f"\nLine: {line}")
            print(f" vowels: {vowel_count} | Words: {word_count}")

print(f"\nTotal subject lines found: {subject_count}")