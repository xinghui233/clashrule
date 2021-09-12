import os
import re


def operation(filename):
    with open("./ACL4SSR/Clash" + filename, "r", encoding="utf-8") as f:
        f_list = f.readlines()
    content = "payload:\n"
    for i in f_list:
        if i == "\n":
            continue
        elif "#" not in i:
            i = "- " + i
        content = content + "  " + i
    with open("./rules/clash/" + re.search(r"(.*?).list", filename).group(1) + ".txt", "w", encoding="utf-8") as f:
        f.write(content)

def main():
    file_list = os.listdir("./ACL4SSR/Clash")
    for filename in file_list:
        if ".list" in filename:
            operation(filename)

if __name__ == "__main__":
    main()