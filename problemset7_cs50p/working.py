import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    if matches := re.fullmatch(r"(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)",s):

        hour1=int(matches.group(1))
        minutes1=matches.group(2)
        period1=matches.group(3)
        hour2=int(matches.group(4))
        minutes2=matches.group(5)
        period2=matches.group(6)

        if minutes1==None:
            minutes1=0
        else:
            minutes1=int(minutes1)

        if minutes2==None:
            minutes2=0
        else:
            minutes2=int(minutes2)

        if not (0<hour1<=12 and
             00<=int(minutes1)<=59 and 
             0<hour2<=12 and 
             00<=int(minutes2)<=59):
                raise ValueError
        else:
            if period1=="AM":
                if hour1==12:
                    hour1=00
                else:
                    if hour1!=12:
                        hour1+=12
            else:
                if hour2==12:
                    hour2=00
                else:
                    if hour2!=12:
                        hour2+=12
            return f"{hour1:02}:{minutes1:02} to {hour2:02}:{minutes2:02}"
    else:
        raise ValueError
    
if __name__ == "__main__":
    main()