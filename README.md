# 🔍 Reverse IP Lookup Tool (Multi-threaded)

A simple tool to perform **mass reverse IP lookups** quickly and efficiently. It uses threading to improve performance and automatically saves results to `result.txt`.

API used: [https://sexreverseipz.vercel.app](https://sexreverseipz.vercel.app)

---

## ⚙️ Features

- ✅ Input from file or direct terminal entry
- ✅ Multi-threaded with `ThreadPoolExecutor` (default: 20 threads)
- ✅ Automatically saves results to `result.txt`
- ✅ Supports mixed domains & IP addresses
- ✅ No extra dependencies (only `requests`)

---

## 🖥️ How to Use

### 1. Run the Script

```bash
python reverse_ip.py
```

### 2. Choose Input Method

- **From file**  
  Provide a file (e.g., `input.txt`) containing a list of IPs or domains (one per line).

- **Manual input**  
  You can input domains or IPs directly using:
  - Commas: `1.1.1.1, 8.8.8.8`
  - Spaces: `1.1.1.1 8.8.8.8`
  - Newlines

### 3. Output

Once the process completes, the domain results will be saved to:

```
result.txt
```

---

## 🧪 Example

### input.txt
```
1.1.1.1
8.8.8.8
example.com
```

### output (result.txt)
```
example.net
example.org
google.com
```

---

## ⚙️ Configuration

- `MAX_WORKERS = 20` → number of threads for parallel execution
- `OUTPUT_FILE = 'result.txt'` → output filename

---

## ⚠️ Notes

- This tool is for educational or authorized penetration testing purposes only.
- Not all IPs will return domain results.
- Make sure your internet connection is stable.

---

## 📄 License

MIT License. Free to use, modify, and share. Use responsibly.
