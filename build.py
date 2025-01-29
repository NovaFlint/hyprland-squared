import os
from pathlib import Path
import subprocess


if not Path("result").is_dir():
    print("build script must be run from the project root, with access to the result directory")
    quit()


def main():
    os.system("rm -rf result/*")
    os.system('''
        find source/template/* -type d | \\
        rg "^source/template/(.+)$" -r \\$1 | \\
        xargs -I {} mkdir result/{}
        ''')
    files = clean_command_output_lines(read_command('''
        find source/template/* -type f | \\
        rg "^source/template/(.+)$" -r \\$1
        '''))

    for file in files:
        conf_in = read_file(Path("source/template/" + file))
        conf_out = transform_conf(conf_in)
        write_file(Path("result/" + file), conf_out)
        # idk if (Path) is helping at all

def read_command(command):
    # from (https://stackoverflow.com/a/4760517)
    return subprocess.run(command, shell=True, capture_output=True, text=True).stdout

def clean_command_output_lines(output):
    lines = output.split("\n")
    while lines[-1] == "":
        lines = lines[:-1]
    return lines

def read_file(path):
    with open(path, "r") as handle:
        return handle.read()
def write_file(path, data):
    with open(path, "w") as handle:
        handle.write(data)



multipliers = {
    "workspace": list(map(str, range(10))),
    "activity": list(map(str, range(10))),
    "direc:key": ["i", "j", "k", "l"],
    "direc:code": ["u", "l", "d", "r"],
    }

def transform_conf(code):
    lines_in = code.split("\n")
    lines_out = []
    for line in lines_in:
        if len(line) > 0 and line[0] != "#" and "@" in line:
            lines_out += multiply_conf_line(line)
        else:
            lines_out += [line]
    return "\n".join(lines_out)

def multiply_conf_line(line):
    bits = line.split("@")
    if len(bits) % 2 != 1:
        print("every line must have an even number of \"@\"")
        quit()

    outer_bits = []
    inner_multipliers = []

    outer_bits += [bits[0]]
    bits = bits[1:]
    while len(bits) > 0:
        if bits[0] in multipliers:
            inner_multipliers += [multipliers[bits[0]]]
            outer_bits += [bits[1]]
        elif bits[0] == "":
            outer_bits[-1] += "@" + bits[1]
        else:
            print(f"invalid multiplier \"{bits[0]}\"")
            quit()

        bits = bits[2:]
    
    if len(outer_bits) == 1:
        return [outer_bits[0]]

    out_lines = []
    for i in range(len(inner_multipliers[0])):
        out_lines += [""]
        for j in range(len(outer_bits) - 1):
            out_lines[-1] += outer_bits[j]
            out_lines[-1] += inner_multipliers[j][i]
        out_lines[-1] += outer_bits[-1]

    return out_lines



if __name__ == "__main__":
    main()
