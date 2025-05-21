import re

def parse_lab_results(raw_text):
    pattern = re.compile(r"(?P<test>[A-Za-z\s]+)\s+(?P<result>\d+\.?\d*)\s*(?P<unit>[a-zA-Z/%]+)?\s+(?P<range>\d+\.?\d*\s*-\s*\d+\.?\d*)")
    results = []
    for match in pattern.finditer(raw_text):
        result = match.groupdict()
        result["status"] = compare_with_range(result["result"], result["range"])
        results.append(result)
    return results

def compare_with_range(value, range_str):
    val = float(value)
    low, high = map(float, range_str.replace(" ", "").split('-'))
    if val < low:
        return "Low"
    elif val > high:
        return "High"
    return "Normal"

def generate_summary(data):
    summary = []
    for item in data:
        if item["status"] == "Normal":
            summary.append(f"{item['test']} is within normal range.")
        else:
            summary.append(f"{item['test']} is {item['status'].lower()}, check reference range.")
    return "\n".join(summary)
