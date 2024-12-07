---
title: Prettify-Error
date: 2024-12-07
author: Your Name
cell_count: 21
score: 20
---

```python

```


```python
error_string = """
{
    "error": {
        "error_code": 1002,
        "error_message": "Unspecified Error",
        "details": "Unexpected error: ['Traceback (most recent call last):', '  File \"/home/rajaraman/rprojects/ml-api-work/ml-api-raja/services/mlapi/app/main.py\", line 228, in post_predict_classic_joblib_api', '    result_obj = await label_generator.match_with_multi(', '                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^', '  File \"/home/rajaraman/rprojects/ml-api-work/ml-api-raja/services/mlapi/app/label_generator.py\", line 770, in match_with_multi', '    feature_scores, overall_score = get_match_scores(', '                                    ^^^^^^^^^^^^^^^^^', '  File \"/home/rajaraman/rprojects/ml-api-work/ml-api-raja/services/mlapi/app/label_generator.py\", line 559, in get_match_scores', '    overall_score = get_average_feature_score(', '                    ^^^^^^^^^^^^^^^^^^^^^^^^^^', '  File \"/home/rajaraman/rprojects/ml-api-work/ml-api-raja/services/mlapi/app/label_generator.py\", line 332, in get_average_feature_score', '    weighted_scores = get_feature_name_score_pair(', '                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^', '  File \"/home/rajaraman/rprojects/ml-api-work/ml-api-raja/services/mlapi/app/label_generator.py\", line 292, in get_feature_name_score_pair', '    if feature_prefix in individual_algo_feature_score_map.keys():', '       ^^^^^^^^^^^^^^', \"UnboundLocalError: cannot access local variable 'feature_prefix' where it is not associated with a value\"]"
    }
}
"""
```


```python
error_string
```




    '\n{\n    "error": {\n        "error_code": 1002,\n        "error_message": "Unspecified Error",\n        "details": "Unexpected error: [\'Traceback (most recent call last):\', \'  File "/home/rajaraman/rprojects/ml-api-work/ml-api-raja/services/mlapi/app/main.py", line 228, in post_predict_classic_joblib_api\', \'    result_obj = await label_generator.match_with_multi(\', \'                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\', \'  File "/home/rajaraman/rprojects/ml-api-work/ml-api-raja/services/mlapi/app/label_generator.py", line 770, in match_with_multi\', \'    feature_scores, overall_score = get_match_scores(\', \'                                    ^^^^^^^^^^^^^^^^^\', \'  File "/home/rajaraman/rprojects/ml-api-work/ml-api-raja/services/mlapi/app/label_generator.py", line 559, in get_match_scores\', \'    overall_score = get_average_feature_score(\', \'                    ^^^^^^^^^^^^^^^^^^^^^^^^^^\', \'  File "/home/rajaraman/rprojects/ml-api-work/ml-api-raja/services/mlapi/app/label_generator.py", line 332, in get_average_feature_score\', \'    weighted_scores = get_feature_name_score_pair(\', \'                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^\', \'  File "/home/rajaraman/rprojects/ml-api-work/ml-api-raja/services/mlapi/app/label_generator.py", line 292, in get_feature_name_score_pair\', \'    if feature_prefix in individual_algo_feature_score_map.keys():\', \'       ^^^^^^^^^^^^^^\', "UnboundLocalError: cannot access local variable \'feature_prefix\' where it is not associated with a value"]"\n    }\n}\n'




```python
import json

def prettify_error(error):
    """
    Prettify the given error dictionary for better readability.
    """
    try:
        # Extract error details
        error_code = error.get("error", {}).get("error_code", "N/A")
        error_message = error.get("error", {}).get("error_message", "N/A")
        details = error.get("error", {}).get("details", "N/A")

        # Format traceback details (if present) into a structured list
        if isinstance(details, str):
            traceback_details = details.split("\n")
        else:
            traceback_details = details

        # Construct the prettified error message
        prettified_error = {
            "Error Code": error_code,
            "Error Message": error_message,
            "Traceback Details": traceback_details
        }

        # Return prettified JSON output
        return json.dumps(prettified_error, indent=4)
    except Exception as e:
        return f"An error occurred while prettifying: {str(e)}"
```


```python
# Call the prettify function
prettified_output = prettify_error(error_string)
print(prettified_output)
```

    An error occurred while prettifying: 'str' object has no attribute 'get'



```python

```


```python

```


```python
import json

def prettify_error_from_string(error_string):
    """
    Prettify the error message from a JSON string.
    """
    try:
        # Parse the string into a dictionary
        error_dict = json.loads(error_string)
        
        # Extract error details
        error_code = error_dict.get("error", {}).get("error_code", "N/A")
        error_message = error_dict.get("error", {}).get("error_message", "N/A")
        details = error_dict.get("error", {}).get("details", "N/A")

        # Format traceback details (if present) into a structured list
        if isinstance(details, str):
            traceback_details = details.split("\n")
        else:
            traceback_details = details

        # Construct the prettified error message
        prettified_error = {
            "Error Code": error_code,
            "Error Message": error_message,
            "Traceback Details": traceback_details
        }

        # Return prettified JSON output
        return json.dumps(prettified_error, indent=4)
    except json.JSONDecodeError as e:
        return f"Error decoding JSON: {str(e)}"
    except Exception as e:
        return f"An error occurred: {str(e)}"
```


```python
# Call the prettify function with the error string
prettified_output = prettify_error_from_string(error_string)
print(prettified_output)
```

    Error decoding JSON: Expecting ',' delimiter: line 6 column 87 (char 178)



```python

```


```python

import json

def fix_and_prettify_error(error_string):
    """
    Fix the JSON string by escaping quotes and prettify the error message.
    """
    try:
        # Fix the error string by replacing unescaped quotes
        fixed_error_string = error_string.replace('"', '\\"').replace('\\"{', '{').replace('}\\"', '}')

        # Parse the fixed string into a Python dictionary
        error_dict = json.loads(fixed_error_string)

        # Extract error details
        error_code = error_dict.get("error", {}).get("error_code", "N/A")
        error_message = error_dict.get("error", {}).get("error_message", "N/A")
        details = error_dict.get("error", {}).get("details", "N/A")

        # Format traceback details (if present) into a structured list
        if isinstance(details, str):
            traceback_details = details.split("\n")
        else:
            traceback_details = details

        # Construct the prettified error message
        prettified_error = {
            "Error Code": error_code,
            "Error Message": error_message,
            "Traceback Details": traceback_details
        }

        # Return prettified JSON output
        return json.dumps(prettified_error, indent=4)
    except json.JSONDecodeError as e:
        return f"Error decoding JSON: {str(e)}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Fix and prettify the error string
prettified_output = fix_and_prettify_error(error_string)
print(prettified_output)

```

    Error decoding JSON: Expecting property name enclosed in double quotes: line 3 column 5 (char 7)



```python

```


```python

```


```python
import json

def prettify_error(error_string):
    try:
        # Parse the string into a dictionary
        error_dict = json.loads(error_string)

        # Extract error details
        error_code = error_dict.get("error", {}).get("error_code", "N/A")
        error_message = error_dict.get("error", {}).get("error_message", "N/A")
        details = error_dict.get("error", {}).get("details", "N/A")

        # Format traceback details (if present) into a structured list
        if isinstance(details, str):
            traceback_details = details.split("\n")
        else:
            traceback_details = details

        # Construct the prettified error message
        prettified_error = {
            "Error Code": error_code,
            "Error Message": error_message,
            "Traceback Details": traceback_details
        }

        # Return prettified JSON output
        return json.dumps(prettified_error, indent=4)
    except json.JSONDecodeError as e:
        return f"Error decoding JSON: {str(e)}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Call the prettify function
prettified_output = prettify_error(error_string)
print(prettified_output)

```

    Error decoding JSON: Expecting ',' delimiter: line 6 column 87 (char 178)



```python

```


```python

```


```python
import json
import re

def sanitize_and_prettify_error(error_string):
    """
    Sanitize the input JSON string and prettify the error message.
    """
    try:
        # Use regex to replace single quotes inside the 'details' field with double quotes
        sanitized_string = re.sub(
            r"(')(?:(?=(\\?))\2.)*?\1",  # Match strings wrapped in single quotes
            lambda match: f'"{match.group(0)[1:-1]}"',  # Replace single quotes with double quotes
            error_string
        )

        # Parse the sanitized string into a Python dictionary
        error_dict = json.loads(sanitized_string)

        # Extract error details
        error_code = error_dict["error"].get("error_code", "N/A")
        error_message = error_dict["error"].get("error_message", "N/A")
        details = error_dict["error"].get("details", "N/A")

        # Split traceback details if it's a string
        if isinstance(details, str):
            traceback_details = details.split(", ")
        else:
            traceback_details = details

        # Construct prettified output
        prettified_error = {
            "Error Code": error_code,
            "Error Message": error_message,
            "Traceback Details": traceback_details
        }

        # Return the prettified JSON
        return json.dumps(prettified_error, indent=4)
    except json.JSONDecodeError as e:
        return f"Error decoding JSON: {str(e)}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Call the function with the given error_string
prettified_output = sanitize_and_prettify_error(error_string)
print(prettified_output)

```

    Error decoding JSON: Expecting ',' delimiter: line 6 column 41 (char 132)



```python

```


```python

```


```python
import json
import re

def sanitize_and_prettify_error(error_string):
    """
    Sanitize and parse a malformed JSON string, then prettify the output.
    """
    try:
        # Fix the single quotes in JSON-like fields with regex
        sanitized_string = re.sub(
            r"(?<!\\)'",  # Match single quotes not preceded by a backslash
            '"',  # Replace with double quotes
            error_string
        )

        # Parse the fixed string into a Python dictionary
        error_dict = json.loads(sanitized_string)

        # Extract error details
        error_code = error_dict.get("error", {}).get("error_code", "N/A")
        error_message = error_dict.get("error", {}).get("error_message", "N/A")
        details = error_dict.get("error", {}).get("details", "N/A")

        # Split traceback details if it's a string
        if isinstance(details, str):
            traceback_details = details.split(", ")
        else:
            traceback_details = details

        # Construct a prettified dictionary
        prettified_error = {
            "Error Code": error_code,
            "Error Message": error_message,
            "Traceback Details": traceback_details
        }

        # Return prettified JSON
        return json.dumps(prettified_error, indent=4)
    except json.JSONDecodeError as e:
        return f"Error decoding JSON: {str(e)}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Input string
error_string = """
{
    "error": {
        "error_code": 1002,
        "error_message": "Unspecified Error",
        "details": "Unexpected error: ['Traceback (most recent call last):', '  File \"/home/rajaraman/rprojects/ml-api-work/ml-api-raja/services/mlapi/app/main.py\", line 228, in post_predict_classic_joblib_api', '    result_obj = await label_generator.match_with_multi(', '                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^', '  File \"/home/rajaraman/rprojects/ml-api-work/ml-api-raja/services/mlapi/app/label_generator.py\", line 770, in match_with_multi', '    feature_scores, overall_score = get_match_scores(', '                                    ^^^^^^^^^^^^^^^^^', '  File \"/home/rajaraman/rprojects/ml-api-work/ml-api-raja/services/mlapi/app/label_generator.py\", line 559, in get_match_scores', '    overall_score = get_average_feature_score(', '                    ^^^^^^^^^^^^^^^^^^^^^^^^^^', '  File \"/home/rajaraman/rprojects/ml-api-work/ml-api-raja/services/mlapi/app/label_generator.py\", line 332, in get_average_feature_score', '    weighted_scores = get_feature_name_score_pair(', '                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^', '  File \"/home/rajaraman/rprojects/ml-api-work/ml-api-raja/services/mlapi/app/label_generator.py\", line 292, in get_feature_name_score_pair', '    if feature_prefix in individual_algo_feature_score_map.keys():', '       ^^^^^^^^^^^^^^', \"UnboundLocalError: cannot access local variable 'feature_prefix' where it is not associated with a value\"]"
    }
}
"""

# Prettify and sanitize the error string
prettified_output = sanitize_and_prettify_error(error_string)
print(prettified_output)
```

    Error decoding JSON: Expecting ',' delimiter: line 6 column 41 (char 132)



```python

```


---
**Score: 20**