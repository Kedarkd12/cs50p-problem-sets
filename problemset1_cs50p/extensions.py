extent=input("Enter File name: ").strip()

if extent.endswith(".gif"):
    print("File Type : image/gif")
elif extent.endswith(".jpg"):
    print("File Type : image/jpg")
elif extent.endswith(".jpeg"):
    print("File Type : image/jpeg")
elif extent.endswith(".png"):
    print("File Type : image/png")
elif extent.endswith(".pdf"):
    print("File Type : image/pdf")
elif extent.endswith(".txt"):
    print("File Type : image/txt")
elif extent.endswith(".zip"):
    print("File Type : image/zip")
else:
    print("application/octet-stream")
