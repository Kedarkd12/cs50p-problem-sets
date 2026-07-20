def convert(emote):
    print(f"{emote.replace(":)","🙂").replace(":(","🙁")}")

def main():
    emotion=input("Enter a sentence that includes emoticons:")
    convert(emotion)
main()
