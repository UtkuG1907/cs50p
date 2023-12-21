name = input("File name: ")

extension = name.split(".")[-1].strip()


if extension == "jpg":
    extension = "jpeg"

match extension:
    case "png" | "jpeg" | "gif":
        print("image/"+extension)
    case "txt":
        print("text/plain")
    case "pdf":
        print("application/pdf")
    case "zip":
        print("application/zip")
    case "bin":
        print("application/octet-stream")
    case "PDF":
        print("application/pdf")
    case _:
        print("application/octet-stream")

