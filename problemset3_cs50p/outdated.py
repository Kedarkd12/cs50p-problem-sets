months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    t=input("Date:")
    if "/" in t:
        t=t.split("/")
        month=int(t[0])
        days=int(t[1])
        year=int(t[2])
        if month>12 or month<1:
            continue
        if days>31 or days<1:
            continue
        else:
            print(f"Date:{year}-{month:02}-{days:02}")
            break

    else:
        t=t.replace(",","").split(" ")
        month=t[0]
        days=int(t[1])
        year=t[2]
        if month not in months:
            continue
        else:
            m=months.index(month)+1
        if m>12 or m<1:
            continue
        if days>31 or days<1:
            continue
        else:
            print(f"Date:{year}-{m:02}-{days:02}")
            break