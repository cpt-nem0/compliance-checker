import json
import re


def extract_json(text: str) -> dict:
    try:
        result = json.loads(text)
    except:
        json_match = re.search(r"\{[\s\S]*\}", text)
        if json_match:
            result = json.loads(json_match.group(0))
        else:
            raise ValueError("Could not parse JSON from response")

    return result
