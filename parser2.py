def clean_line(line):
    line = line.split("//")[0]
    return line.strip()


def parse_line(line):
    line = clean_line(line)

    if not line:
        return None

    if line.startswith("(") and line.endswith(")"):
        return {
            "type": "L",
            "symbol": line[1:-1].strip()
        }

    if line.startswith("@"):
        return {
            "type": "A",
            "value": line[1:].strip()
        }

    dest = ""
    comp_jump = line
    jump = ""

    if ";" in comp_jump:
        comp_jump, jump = comp_jump.split(";", 1)

    if "=" in comp_jump:
        dest, comp = comp_jump.split("=", 1)
    else:
        comp = comp_jump

    return {
        "type": "C",
        "dest": dest.strip(),
        "comp": comp.strip(),
        "jump": jump.strip()
    }


def main():
    with open("input.asm", "r") as file:
        line_number = 0

        for line in file:
            line_number += 1
            result = parse_line(line)

            if result is None:
                continue

            print("Line:", line_number)

            if result["type"] == "A":
                print("Type: A-instruction")
                print("Value:", result["value"])

            elif result["type"] == "L":
                print("Type: Label")
                print("Symbol:", result["symbol"])

            else:
                print("Type: C-instruction")
                print("Dest:", result["dest"])
                print("Comp:", result["comp"])
                print("Jump:", result["jump"])

            print()


main()