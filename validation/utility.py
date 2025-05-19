import re

def validate_metadata(data: dict):
    required_fields = ['board', 'effective_stack', 'ev_oop', 'ev_ip', 'range0', 'range1']
    for key in required_fields:
        if key not in data or data[key] in [None, '', []]:
            raise ValueError(f"Missing or invalid field: {key}")
    return True

def safe_extract(pattern: str, text: str, cast_type=str, default=None, strip_value=True):
    match = re.search(pattern, text)
    if match:
        value = match.group(1)
        return cast_type(value.strip()) if strip_value else cast_type(value)
    return default

def safe_float(pattern: str, text: str, default=None):
    return safe_extract(pattern, text, cast_type=float, default=default)

def cast_bool(val):
    return val.strip().lower() in ['1', 'true', 'yes']
