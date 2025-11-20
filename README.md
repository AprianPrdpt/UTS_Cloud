# UTS Cloud

# Soal 1 — Keterkaitan SaaS, PaaS, dan IaaS

SaaS (Software as a Service), PaaS (Platform as a Service), dan IaaS (Infrastructure as a Service) merupakan tiga model utama layanan cloud computing yang berjalan secara bertingkat dan saling berhubungan satu sama lain. Dasarnya, IaaS menyediakan infrastruktur virtual seperti server, storage, dan jaringan yang dapat diatur pengguna sesuai kebutuhan. Di atas IaaS, PaaS menyediakan platform pengembangan yang memudahkan developer untuk membangun, menguji, dan menyebarkan aplikasi tanpa mengelola infrastruktur secara langsung. SaaS menempati posisi paling atas dengan menyediakan aplikasi siap pakai kepada pengguna akhir, di mana seluruh aspek pengelolaan aplikasi, hardware, sampai update dikelola oleh penyedia jasa cloud.


# Soal 2 - Diagram keterkaitan Cloud-Native App, Container, PaaS, dan SaaS

```
flowchart TB
    IaaS["IaaS (Infrastruktur Virtualisasi)<br/><br/>- Komputasi, Penyimpanan, Jaringan"]
      --> PaaS["PaaS (Platform Pengembangan)<br/><br/>- Mendukung deployment container<br/>- Contoh: Heroku, Google App Engine"]
    PaaS --> CNA["Cloud Native App / Teknologi Container<br/><br/>- Docker, Kubernetes, Microservice Architectures"]
    CNA --> SaaS["SaaS (Aplikasi Siap Pakai)<br/><br/>- Contoh: Google Docs, Office 365"]
    PaaS --> SaaS
```


