import os
import psutil

class ResourceAllocator:
    def __init__(self, max_memory_percentage=50):
        # Initialize with the maximum memory percentage allowed for the application
        self.max_memory_percentage = max_memory_percentage

    def set_max_memory_percentage(self, percentage):
        # Set the maximum memory percentage
        if 0 < percentage <= 100:
            self.max_memory_percentage = percentage
        else:
            raise ValueError("Percentage must be between 1 and 100")

    def get_max_memory_bytes(self):
        # Calculate the maximum memory in bytes
        total_memory = psutil.virtual_memory().total
        max_memory_bytes = (self.max_memory_percentage / 100) * total_memory
        return max_memory_bytes

    def is_memory_usage_within_limit(self):
        # Check if the current memory usage is within the limit
        current_memory_usage = psutil.virtual_memory().used
        return current_memory_usage <= self.get_max_memory_bytes()

# Example usage:
if __name__ == '__main__':
    allocator = ResourceAllocator()
    
    print(f"Max memory allowed: {allocator.get_max_memory_bytes() / (1024 ** 3):.2f} GB")

    if allocator.is_memory_usage_within_limit():
        print("Memory usage is within the limit.")
    else:
        print("Memory usage exceeds the limit.")
