import time
import numpy as np
import psutil
import os

def cpu_benchmark():
    start_time = time.time()
    n = 1000000
    a = np.random.rand(n)
    b = np.random.rand(n)
    c = a * b
    elapsed_time = time.time() - start_time
    print(f"CPU benchmark: {elapsed_time:.2f} seconds")

def memory_benchmark():
    start_time = time.time()
    n = 1000000
    a = np.random.rand(n)
    max_memory = np.max(a)
    min_memory = np.min(a)
    mean_memory = np.mean(a)
    elapsed_time = time.time() - start_time
    print(f"Memory benchmark: {elapsed_time:.2f} seconds")
    print(f"Memory usage: {psutil.virtual_memory().percent}%")

def disk_io_benchmark():
    start_time = time.time()
    filename = "test_file"
    data = os.urandom(100000000)  # 100MB
    with open(filename, 'wb') as f:
        f.write(data)
    elapsed_write_time = time.time() - start_time
    
    start_time = time.time()
    with open(filename, 'rb') as f:
        data = f.read()
    elapsed_read_time = time.time() - start_time
    
    os.remove(filename)
    
    print(f"Disk I/O benchmark (write): {elapsed_write_time:.2f} seconds")
    print(f"Disk I/O benchmark (read): {elapsed_read_time:.2f} seconds")

def main():
    print("Starting Raspberry Pi Benchmark...")
    print("-------------------------------")
    
    print("1. CPU Benchmark")
    cpu_benchmark()
    print("-------------------------------")
    
    print("2. Memory Benchmark")
    memory_benchmark()
    print("-------------------------------")
    
    print("3. Disk I/O Benchmark")
    disk_io_benchmark()
    print("-------------------------------")
    
    print("Benchmark completed.")

if __name__ == "__main__":
    main()
