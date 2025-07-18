# Module 2 - Video 11.1: Regular Expressions

## 📅 Date: 17 July 2025, Day 37 of coding
## 📍 Course: Using Python to Access Web Data (Coursera Plus)

### ✅ What I Learned:
- Regular expressions help in searching and extracting patterns from text.
- Useful for cleaning, parsing, and matching specific content in web scraping.

### 🧠 Key Concepts:
- `import re`
- `re.search()` and `re.findall()`
- Special characters:
  - `^` matches the beginning
  - `$` matches the end
  - `.` matches any character
  - `*`, `+`, `?` for quantifiers

### 🧪 Example Code:
```python
import re

text = "My email is name@example.com"
match = re.findall(r'\S+@\S+', text)
print(match)  # Output: ['name@example.com']
