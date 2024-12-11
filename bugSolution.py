def function_with_uncommon_error(data):
    try:
        # Assume data is a list of dictionaries, each with a 'value' key
        result = [item['value'] for item in data if isinstance(item, dict) and 'value' in item]
        return result
    except (KeyError, TypeError) as e:
        # Handle KeyError if 'value' key is missing in some dictionaries
        # Handle TypeError if data is not a list of dictionaries
        print(f"Error: {e}")
        return []

# Example usage that may cause the TypeError
data1 = [{'value': 1}, {'value': 2}, {'value': 3}]
data2 = [{'another_key': 1}, {'value': 2}, {'value': 3}]  # KeyError
data3 = 123 #TypeError

print(function_with_uncommon_error(data1))
print(function_with_uncommon_error(data2))
print(function_with_uncommon_error(data3))