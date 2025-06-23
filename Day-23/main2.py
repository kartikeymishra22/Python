from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)
pdf.set_font("DejaVu", size=12)

content = """ The time module provides functions to work with time, delays, timestamps, and performance measurement in Python.

✅ How to Import
python
Copy
Edit
import time
📘 Categories of time Functions
1. 📆 Getting the Current Time
🔹 time.time()
Returns the current time in seconds since Epoch (Jan 1, 1970).

python
Copy
Edit
import time
print(time.time())  # 1719139987.08364
2. 🕰️ Sleep or Delay Code
🔹 time.sleep(seconds)
Pauses the program for given seconds.

python
Copy
Edit
print("Wait 2 seconds...")
time.sleep(2)
print("Done")
3. ⏱️ Measure Code Execution Time
🔹 time.perf_counter()
Most precise timer for benchmarking code (better than time.time()).

python
Copy
Edit
start = time.perf_counter()

# Your code
for _ in range(1000000):
    pass

end = time.perf_counter()
print("Execution time:", end - start)
4. 📆 Working with Struct Time
🔹 time.localtime()
Returns current time in a struct_time object (tuple-like).

python
Copy
Edit
t = time.localtime()
print(t.tm_year, t.tm_mon, t.tm_mday)  # e.g., 2025 6 23
🔹 time.gmtime()
Same as localtime() but in UTC (Greenwich time).

5. 📅 Convert Between Formats
🔹 time.strftime(format, struct_time)
Formats a time object to string.

python
Copy
Edit
print(time.strftime("%Y-%m-%d %H:%M:%S"))  # '2025-06-23 12:38:00'
🔹 Common Format Codes:
Code	Meaning
%Y	Year (e.g., 2025)
%m	Month (01–12)
%d	Day of month
%H	Hour (24-hour)
%M	Minute
%S	Second

🔹 time.strptime(string, format)
Parses a string into a struct_time.

python
Copy
Edit
s = "2025-06-23"
t = time.strptime(s, "%Y-%m-%d")
print(t.tm_year)  # 2025
6. ⌚ Epoch and Timestamp Conversion
🔹 time.mktime(struct_time)
Converts struct_time to seconds since epoch.

python
Copy
Edit"""

pdf.multi_cell(0, 10, content)
pdf_file_path = "time_module_overview.pdf"
pdf.output(pdf_file_path)
print(f"PDF saved as {pdf_file_path}")