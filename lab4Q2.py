memory_hog = []
try:
    while True:
        
        memory_hog.append(' ' * 10**6)  
except MemoryError:
    print("Memory exhausted!")
