#indoor
name=input("Enter your full name:").strip().lower()
print(f"{name}")

#playback speed
sent=input("Enter a sentence:").strip()
print(f"{sent.replace(" ","...")}")

#making faces
def convert(emote):
    print(f"{emote.replace(":)","🙂").replace(":(","🙁")}")

def main():
    emotion=input("Enter a sentence that includes emoticons:")
    convert(emotion)
main()

#einstein
mass=int(input("Enter the mass:"))
c=300000000
E=mass*pow(c,2)
print(f"{E}")

#tip calculator
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    return float(d.replace("$",""))

def percent_to_float(p):
    return float(p.replace("%",""))/100

main()