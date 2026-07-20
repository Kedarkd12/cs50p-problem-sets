def main():
    hours,minutes=input("What time is it? ").strip().split(":")
    hours=int(hours)
    minutes=int(minutes)
    convert(hours,minutes)

def convert(x,z):
    if(x==7 and 00<z<60):
        print("Breakfast time")
    elif(x==12 and 00<z<60):
        print("Lunch Time")
    elif(x==18 and 00<z<60):
        print("Dinner Time")

if __name__ == "__main__":
    main()
     