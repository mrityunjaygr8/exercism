def commands(binary_str):
    binary = list(binary_str)
    output = list()

    if binary[4] == "1":
        output.append("wink")

    if binary[3] == "1":
        output.append("double blink")

    if binary[2] == "1":
        output.append("close your eyes")

    if binary[1] == "1":
        output.append("jump")

    if binary[0] == "1":
        output = list(reversed(output))
    return output
