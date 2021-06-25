import dropbox
import os

class TransferData:
    def __init__(self,accessToken):
        self.accessToken = accessToken
    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.accessToken)

        for root, dirs, files in os.walk(file_from):
            for name in files:
                e = file_to + name
                f = open(os.path.join(root,name),'rb')
                dbx.files_upload(f.read(),e)

def main():
    access_token = "8UnBbc02DFcAAAAAAAAAAXGFNhwJBJVCuKiCHjSnpvUghbkgKOEyMYB9G2a0B6nP"
    transferData = TransferData(access_token)

    file_from = input('Enter file path to transfer : ')
    file_to = "/test_proj101/"

    transferData.upload_file(file_from,file_to)
    print('Files Have Been Moved')

main()
