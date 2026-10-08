# Prompt for the file name, strip spaces, and make it lowercase so ".GIF" and ".gif" work the same
filename = input("File name: ").strip().lower()

# Check each file extension from the problem specification one by one
if filename.endswith(".gif"):
    print("image/gif")
# Combine .jpg and .jpeg since both output the exact same media type
elif filename.endswith(".jpg") or filename.endswith(".jpeg"):
    print("image/jpeg")
elif filename.endswith(".png"):
    print("image/png")
elif filename.endswith(".pdf"):
    print("application/pdf")
elif filename.endswith(".txt"):
    print("text/plain")
elif filename.endswith(".zip"):
    print("application/zip")
# If the file ends with something else (or has no extension at all)
else:
    # Print the default catch-all media type
    print("application/octet-stream")
