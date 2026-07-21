import sys
import csv

if len(sys.argv)>3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv)==1:
    sys.exit("Too few command-line arguments")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a python file")
elif not sys.argv[2].endswith(".csv"):
    sys.exit("Enter a valid file to create")

try:
    with open(sys.argv[1]) as file:
        reader=csv.DictReader(file)
        with open(sys.argv[2],"a",newline="") as file:
            writer=csv.DictWriter(file,fieldnames=["first","last","house"])
            writer.writeheader()
            for row in reader:
                name=row["name"]
                house=row["house"]
                last,first=name.split(",")
                writer.writerow({"first":first,"last":last,"house":house})
except FileNotFoundError:
    sys.exit("File doesnt exist")    


