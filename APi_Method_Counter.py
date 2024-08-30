import json

def count_http_methods(json_file_path):
    try:
        with open(json_file_path, 'r') as file:
            data = json.load(file)
            
            # Initialize counts for each HTTP method and a total count
            method_counts = {
                "GET": 0,
                "POST": 0,
                "PUT": 0,
                "DELETE": 0,
                "PATCH": 0,
                "OPTIONS": 0,
                "CONNECT": 0,
                "TOTAL": 0  # To keep track of the total number of requests
            }

            def count_requests(items):
                for item in items:
                    if 'request' in item and 'method' in item['request']:
                        method = item['request']['method'].upper()
                        if method in method_counts:
                            method_counts[method] += 1
                            method_counts["TOTAL"] += 1
                    # Recursively check nested items
                    if 'item' in item:
                        count_requests(item['item'])
            
            count_requests(data['item'])  # Start counting from the top-level items

            return method_counts

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Prompt the user to input the JSON file path
json_file_path = input("Please enter the path to your JSON file: ")

method_counts = count_http_methods(json_file_path)

if method_counts:
    print(f"The JSON file contains:")
    print(f"GET requests: {method_counts['GET']}")
    print(f"POST requests: {method_counts['POST']}")
    print(f"PUT requests: {method_counts['PUT']}")
    print(f"DELETE requests: {method_counts['DELETE']}")
    print(f"PATCH requests: {method_counts['PATCH']}")
    print(f"OPTIONS requests: {method_counts['OPTIONS']}")
    print(f"CONNECT requests: {method_counts['CONNECT']}")
    print(f"Total requests: {method_counts['TOTAL']}")
