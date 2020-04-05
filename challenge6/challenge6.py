import zipfile

with zipfile.ZipFile('challenge6.zip', 'w') as myzip:
    myzip.write('channel.jpg')
    print(myzip.infolist)
    print(myzip.compress_size)
    print(myzip.infolist)
    myzip.close()
