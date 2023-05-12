def main():
    file_name = input("File name: ")
    file_name = file_name.lower().strip()
    parts = file_name.rpartition(".")
    if parts[2] == "gif":
        print("image/gif")
    elif parts[2] == "jpg" or parts[2] == "jpeg":
        print("image/jpeg")
    elif parts[2] == "png":
        print("image/png")
    elif parts[2] == "pdf":
        print("application/pdf")
    elif parts[2] == "txt":
        print("text/plain")
    elif parts[2] == "zip":
        print("application/zip")
    else:
        print("application/octet-stream")

main()
