from unstructured.partition.image import partition_image
elements = partition_image(filename="/content/nfl-howtounderstand-nutrients.png")
full_text = "\n".join([element.text for element in elements if element.text])

import re
import json

def ocr_text_to_json(text):
    result = {}
    lines = text.strip().split('\n')

    for line in lines:
        line = re.sub(r'\s+', ' ', line).strip()

        match = re.match(r'([A-Za-z\s]+)(.*)', line)
        if not match:
            continue
        key = match.group(1).strip()

        values_part = match.group(2).strip()

        value_matches = re.findall(r'(\d+\.?\d*\s*[a-zA-Z%]*)', values_part)

        if len(value_matches) == 2:
            amount = value_matches[0].strip()
            daily_value = value_matches[1].strip()
            result[key] = {"amount": amount, "daily_value": daily_value}
        elif len(value_matches) == 1:
            amount = value_matches[0].strip()
            result[key] = {"amount": amount}
        else:
            if values_part:
                result[key] = values_part
            else:
                result[key] = None

    return result


json_output = ocr_text_to_json(full_text)
print(json.dumps(json_output, indent=3))

