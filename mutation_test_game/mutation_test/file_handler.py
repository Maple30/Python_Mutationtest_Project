def handle_uploaded_file(f):
# try:
    print(f)
    with open('testfile/' + f.name, 'wb') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
# except:

    # print("NO file bro")