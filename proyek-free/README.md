# Output Program Free-Threaded

Pengujian dilakukan menggunakan Python **3.14 Free-Threaded** melalui `uv`.  
Hasil berikut merupakan waktu eksekusi pada dua pendekatan concurrency: AsyncIO dan Multiprocessing.

# 1. Output `async_fetch.py`
Program menjalankan HTTP fetch secara asynchronous menggunakan `httpx` dan event loop.

**Output:**
AsyncIO time: 0.7567708492279053

Pendekatan async di Python free-threaded bekerja optimal karena tidak terblokir oleh GIL, terutama untuk workload I/O-bound.

---

# 2. Output `multi_fetch.py`
Program melakukan fetch menggunakan multiprocessing untuk menjalankan beberapa proses paralel secara penuh.

**Output:**
Multiprocessing time: 0.8309884071350098

Performa multiprocessing sedikit lebih lambat dibanding AsyncIO dalam percobaan ini, kemungkinan karena overhead pembuatan proses baru.

