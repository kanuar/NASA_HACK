from zipfile import ZipFile

def downloader(k):
    wget.download(k)
    f1=str(i)+'-Data.zip'
    f2=str(i)+'-ImageSet.zip'
    with ZipFile(f1,'r') as zipobj:
        zipobj.extractall()
    with ZipFile(f2,'r') as zipobj:
        zipobj.extractall()
