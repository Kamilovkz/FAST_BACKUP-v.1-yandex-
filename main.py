import os, shutil
import zipfile
import datetime
import yadisk

def main():
    seacrh()

def search():
    poisk = []
    with zipfile.ZipFile('{}.zip'.format(str(datetime.datetime.now()).replace("-","").replace('.', '').replace(':','')), 'w') as archive:
        for address, dirs, files in os.walk(input('Enter way: ')):
            for file in files:
                #Solving problem with dublicates
                file_name = file.split('\\')[-1]
                count = 1
                for f in poisk:
                    if f == file_name:
                        if f'({count - 1})' in file_name:
                            file_name = file_name.replace(f'({count - 1})', '')
                        file_name = f'({count}).'.join(file_name.split('.'))
                        count += 1
                #File extensions
                if file_name.endswith(".docx") or file_name.endswith(".doc") or file_name.endswith(".pdf"):
                    poisk.append(file_name)
                    archive.write(os.path.join(address,file), file_name)
                    print(file_name, ' is copied')
    print('Archive is created!')
    # Send atchive to Yandex cloud using yadisc library
    yandex = yadisk.YaDisk(token='PASTHEREYOURAPI')
    yandex.upload(archive.filename, '/' + archive.filename)
    print('Archive successfully sent')
    # Delete archive
    os.remove(archive.filename)
    print('Archive successfully deleted from folder')

if __name__ == "__main__":
    main()
