def remove_comments(line):
    if ';' in line:
        line = line.split(';')[0]
    return line.strip()


def parse_line(line):
    line = remove_comments(line)

    if line == "":
        return None

    label = ""
    instruction = ""
    operands = []

# Checking whether the line contains a label or not
    if ':' in line:
        parts = line.split(':', 1)
        label = parts[0].strip()
        line = parts[1].strip()

    if line == "":
        return {
            "label": label,
            "instruction": "",
            "operands": []
        }

# Replace multiple spaces and tabs with one space
    line = " ".join(line.split())

    parts = line.split(" ", 1)
    instruction = parts[0].upper()

    if len(parts) > 1:
        operand_text = parts[1]

# Remove unnecessary spaces around commas
        operand_text = operand_text.replace(" ", "")
        operands = operand_text.split(',')

    return {
        "label": label,
        "instruction": instruction,
        "operands": operands
    }


def main():
    file_name = "input.asm"

    try:
        file = open(file_name, "r")
    except FileNotFoundError:
        print("Source file not found.")
        return

    print("Parsed Assembly File")
    print("--------------------")

    line_number = 0

    for line in file:
        line_number += 1

        result = parse_line(line)

        if result is None:
            continue

        print("Line:", line_number)

        if result["label"]:
            print("Label      :", result["label"])

        if result["instruction"]:
            print("Instruction:", result["instruction"])

        if result["operands"]:
            print("Operands   :", ", ".join(result["operands"]))

        print()

    file.close()


main()
