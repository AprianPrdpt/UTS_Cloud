# Output Program

Berikut hasil eksekusi dari kedua file uji performa (`async_fetch.py` dan `multi_fetch.py`) menggunakan Python 3.14 pada environment `uv`.

# 1. Hasil Output `async_fetch.py`
Program ini menjalankan pengambilan data menggunakan AsyncIO dengan library `httpx`.

**Output:**
AsyncIO time: 1.8975837230682373

Waktu tersebut menunjukkan total durasi eksekusi concurrent fetch menggunakan pendekatan asynchronous.


### 🔹 2. Hasil Output `multi_fetch.py`
Program ini menguji pengambilan data menggunakan **multiprocessing** untuk menjalankan beberapa proses secara paralel.

**Output:**
Multiprocessing time: 1.7358670234680176

Hasil ini menunjukkan berapa lama eksekusi paralel dengan proses terpisah selesai dijalankan.
