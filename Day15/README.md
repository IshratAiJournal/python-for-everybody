

#### ✅ Description

This Python script takes a location input from the user, retrieves its latitude and longitude using an online geocoding API, and then converts it into a [Plus Code](https://plus.codes/) using the `openlocationcode` module. It showcases practical usage of Python with web APIs and external modules.


#### 🔧 Technologies & Tools Used

* Python 3.13
* `urllib`, `json` (built-in modules)
* `openlocationcode` (external module for Plus Code generation)
* OpenStreetMap API (via `http://py4e-data.dr-chuck.net/opengeo`)

#### 🧠 What We Learned

* Parsing JSON data from a web API
* Handling user input and HTTP requests
* Installing and using external Python modules with `pip`
* Understanding how location encoding (Plus Codes) works

#### 🚧 Challenges Faced

We spent **2 full days** solving this assignment! Some of the major challenges included:

1. Handling **multiple variations of location outputs** (coordinates were changing slightly).
2. The **Plus Code validation kept failing**, even when the format looked right.
3. Installing `openlocationcode` was smooth, but using `encode()` threw errors due to incorrect module usage at first.
4. Had to **understand API responses deeply**, and test repeatedly to match the required Coursera result.
5. Finally got the **correct Plus Code: `849VVPFW+M6`** after dozens of iterations!

💪 This task taught us not just code, but also **patience, debugging skills, and perseverance.**

#### 📄 Files

* `location_to_pluscode.py` — The main script (uploaded separately)
* `README.md` — This file


#### 🎓 About the Course

**Course Name**: *Using Python to Access Web Data*
**Platform**: [Coursera](https://www.coursera.org/learn/python-network-data)
**Instructor**: Dr. Charles Severance (Dr. Chuck)
**Progress**: ✅ Week 6 Assignment Completed

