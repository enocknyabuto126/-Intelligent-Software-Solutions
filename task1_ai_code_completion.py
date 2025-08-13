x# Task 1: AI-Powered Code Completion
# Comparing Manual vs AI-Suggested Code for Sorting Dictionaries

def manual_sort_dicts_by_key(data_list, key):
    """
    Manual implementation: Sort a list of dictionaries by a specific key
    This is the traditional approach without AI assistance
    """
    # Manual implementation using sorted() with lambda
    return sorted(data_list, key=lambda x: x[key])

def ai_suggested_sort_dicts_by_key(data_list, key):
    """
    AI-suggested implementation: Sort a list of dictionaries by a specific key
    This represents what GitHub Copilot or similar tools might suggest
    """
    # AI tools often suggest this more explicit approach
    def get_key_value(item):
        return item[key]
    
    return sorted(data_list, key=get_key_value)

def alternative_ai_approach(data_list, key):
    """
    Alternative AI-suggested approach using operator module
    This is another common AI suggestion for cleaner code
    """
    from operator import itemgetter
    return sorted(data_list, key=itemgetter(key))

# Test data
test_data = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "Chicago"},
    {"name": "Diana", "age": 28, "city": "Boston"}
]

# Testing all implementations
print("Original data:")
for item in test_data:
    print(f"  {item}")

print("\n1. Manual Implementation (by age):")
manual_result = manual_sort_dicts_by_key(test_data, "age")
for item in manual_result:
    print(f"  {item}")

print("\n2. AI-Suggested Implementation (by name):")
ai_result = ai_suggested_sort_dicts_by_key(test_data, "name")
for item in ai_result:
    print(f"  {item}")

print("\n3. Alternative AI Approach (by city):")
alt_result = alternative_ai_approach(test_data, "city")
for item in alt_result:
    print(f"  {item}")

# Performance comparison
import time
import random

# Generate larger dataset for performance testing
large_data = [
    {"id": i, "value": random.randint(1, 1000), "category": f"cat_{i % 10}"}
    for i in range(10000)
]

print(f"\nPerformance Test with {len(large_data)} items:")

# Test manual implementation
start_time = time.time()
manual_sort_dicts_by_key(large_data, "value")
manual_time = time.time() - start_time

# Test AI-suggested implementation
start_time = time.time()
ai_suggested_sort_dicts_by_key(large_data, "value")
ai_time = time.time() - start_time

# Test alternative AI approach
start_time = time.time()
alternative_ai_approach(large_data, "value")
alt_time = time.time() - start_time

print(f"Manual implementation: {manual_time:.6f} seconds")
print(f"AI-suggested implementation: {ai_time:.6f} seconds")
print(f"Alternative AI approach: {alt_time:.6f} seconds")

# Analysis
print("\n" + "="*60)
print("ANALYSIS: Manual vs AI-Suggested Code Comparison")
print("="*60)

print("\nManual Implementation:")
print("- Uses lambda function directly in sorted()")
print("- More concise, single line")
print("- Slightly less readable for complex sorting logic")
print("- Performance: Good")

print("\nAI-Suggested Implementation:")
print("- Extracts sorting logic into separate function")
print("- More readable and maintainable")
print("- Easier to debug and modify")
print("- Performance: Similar to manual")

print("\nAlternative AI Approach (operator.itemgetter):")
print("- Uses built-in operator module")
print("- Most Pythonic and efficient")
print("- Cleanest syntax")
print("- Performance: Best (optimized C implementation)")

print("\nCONCLUSION:")
print("The AI-suggested approaches (especially the operator.itemgetter method)")
print("provide better code quality, readability, and performance compared to")
print("the manual lambda approach. AI tools excel at suggesting more")
print("Pythonic and efficient solutions that developers might not immediately consider.")
