import dropbox

class managefiles:
    def __init__ (self,accesstoken):
        self.accesstoken=accesstoken

    def uploadfiles(self,src,dest):
        dbx=dropbox.Dropbox(self.accesstoken)
        f=open(src,"rb")
        dbx.files_upload(f.read(),dest)

def main():
    accesstoken="sl.BAv3xwwZDLctvepIkj5wwISuZ6gwpn6UzxAp4jD9x4JrqNo0iYIUC8NHh7tYXW8p_Y3cFtAZBEqdcrhI_jc4AFWU_gOCZMQi9puW5V7JGfGGCZLc7lO4fTJAbQEgv6e4CQ5F2G4"
    obj1=managefiles(accesstoken)

    src="riddles.docx"
    dest="/pythonfiles/riddles.txt"
    obj1.uploadfiles(src,dest)
    print("files have been moved to dropbox")

main()
