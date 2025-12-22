from prometheus_client import start_http_server, Gauge, Counter, Summary
import psutil
import time
import random
import os

# 1-3. Metriks Sistem
cpu_usage = Gauge('system_cpu_usage', 'Persentase penggunaan CPU')
ram_usage = Gauge('system_ram_usage', 'Persentase penggunaan RAM')
disk_usage = Gauge('system_disk_usage', 'Persentase penggunaan Disk')

# 4-6. Metriks Traffic Model
http_requests_total = Counter('http_requests_total', 'Total request ke model')
model_latency = Summary('model_latency_seconds', 'Waktu respon model')
model_errors = Counter('model_errors_total', 'Total error pada model')

# 7-10. Metriks Tambahan (Syarat Advance)
network_io_sent = Gauge('network_sent_bytes', 'Byte terkirim')
network_io_recv = Gauge('network_recv_bytes', 'Byte diterima')
python_mem = Gauge('python_memory_usage_bytes', 'Memory script ini')
active_threads = Gauge('active_threads_count', 'Jumlah thread aktif')

def collect_metrics():
    while True:
        cpu_usage.set(psutil.cpu_percent())
        ram_usage.set(psutil.virtual_memory().percent)
        disk_usage.set(psutil.disk_usage('/').percent)
        
        net = psutil.net_io_counters()
        network_io_sent.set(net.bytes_sent)
        network_io_recv.set(net.bytes_recv)
        
        process = psutil.Process(os.getpid())
        python_mem.set(process.memory_info().rss)
        active_threads.set(psutil.active_count())
        
        time.sleep(5)

if __name__ == '__main__':
    start_http_server(8000)
    print("Exporter jalan di http://localhost:8000")
    collect_metrics()