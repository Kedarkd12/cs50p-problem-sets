from pyfiglet import Figlet
import sys
import random

f=Figlet()
fonts=f.getFonts()
if len(sys.argv)>1:
    if sys.argv[1]!="-f" and sys.argv[1]!="--font":
        sys.exit
    else:
        if sys.argv[2] not in fonts:
            sys.exit
        else:
            f.setFont(font=sys.argv[2])
            b=input("Input:")
            print(f.renderText(b))
else:
    a=input("Input:")
    r=random.choice(f.getFonts())
    f.setFont(font=r)
    print(f.renderText(a))
