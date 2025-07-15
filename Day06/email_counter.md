# Day 06 – Most Prolific Email Sender

📅 **Date:** 13 July 2025  
📘 **Module:** Python Data Structures – Dictionaries  
💡 **Topic:** Parsing lines, building dictionary, counting, finding max

---

## 🥘 Problem Statement
Write a program to read through `mbox-short.txt` and find out who sent the most mail.  
Each relevant line starts with `'From '` and includes the sender’s email address.

---

## 🔧 Tasks Performed
- Opened file using `open()`
- Parsed lines that start with `'From '`
- Extracted the sender email (second word)
- Used `.get()` method with dictionary to count emails
- Used a **maximum loop** to find the most frequent sender

---

## 🧠 Concepts Used
- `startswith("From ")` to filter valid lines
- `split()` to break the line into words
- `dict.get(key, default)` for safe counting
- Looping through dictionary items
- Conditional logic to find maximum value

---

## 🧾 Final Code
```python
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

handle = open(name)
counts = dict()

for line in handle:
    if line.startswith("From "):
        words = line.split()
        email = words[1]
        counts[email] = counts.get(email, 0) + 1

max_count = None
max_email = None

for email, count in counts.items():
    if max_count is None or count > max_count:
        max_email = email
        max_count = count

print(max_email, max_count)


📤 Output (Desired)
cwen@iupui.edu 5

📝 Notes
startswith("From ") is critical — don’t confuse it with "From:"

.get() avoids key errors and simplifies if-else logic

Use a None pattern when finding max/min

✅ Saved as: prolific_sender.py
📄 File Used: mbox-short.txt
