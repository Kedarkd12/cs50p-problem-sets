import re


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    if matches := re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})",ip):
        return True
        if 0<=int(matches.group(1))<=255 :
            if 0<=int(matches.group(2))<=255 :
                if 0<=int(matches.group(3))<=255:
                    if 0<=int(matches.group(4))<=255:
                        return True
    else:
        return False

if __name__ == "__main__":
    main()