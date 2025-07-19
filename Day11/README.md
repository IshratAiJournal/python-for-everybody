# Socket Request: ETag and Content-Length

This project uses raw sockets in Python to fetch binary data from a URL using HTTP and extract specific metadata from the headers.

### 🔍 Task Objective:
- Connect to a server using `socket`.
- Send a `GET` request to fetch a resource.
- Decode the response headers.
- Extract and print:
  - ✅ First word of the file
  - 📄 `ETag` header
  - 📄 `Content-Length` header

### 🌐 Resource URL:
- `http://data.pr4e.org/cover3.jpg`
- `http://data.pr4e.org/intro-short.txt`

### 🧠 Learning Outcome:
- Understanding low-level socket programming
- Parsing HTTP headers manually
- Handling binary vs. text content
