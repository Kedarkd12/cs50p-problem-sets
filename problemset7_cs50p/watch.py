import re


def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    if matches := re.search(r"^(https?)://(?:www\.)?youtube\.com/embed(/\w+)$",s):
        return f"{matches.group(1)}://youtu.be{matches.group(2)}"

if __name__ == "__main__":
    main()