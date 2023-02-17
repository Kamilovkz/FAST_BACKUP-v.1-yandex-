import os
import zipfile
import datetime
import yadisk

def main():
    run = Search()
    run.engine()

import os
import datetime
import zipfile
import yadisk

def main():
    search = Search(input_dir='/path/to/search/directory', yadisk_token='PASTHEREYOURAPI')
    search.create_archive()

class Search:
    def __init__(self, input_dir, yadisk_token):
        self.input_dir = input_dir
        self.yadisk_token = yadisk_token

    def search_files(self):
        poisk = []
        for address, dirs, files in os.walk(self.input_dir):
            for file in files:
                #Solving problem with duplicates
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
                    yield os.path.join(address, file), file_name

    def create_archive(self):
        archive_name = '{}.zip'.format(str(datetime.datetime.now()).replace("-","").replace('.', '').replace(':',''))
        with zipfile.ZipFile(archive_name, 'w') as archive:
            for file_path, file_name in self.search_files():
                archive.write(file_path, file_name)
                print(file_name, ' is copied')
        print('Archive is created!')
        # Send archive to Yandex cloud using yadisk library
        yandex = yadisk.YaDisk(token=self.yadisk_token)
        yandex.upload(archive_name, '/' + archive_name)
        print('Archive successfully sent')
        # Delete archive
        os.remove(archive_name)
        print('Archive successfully deleted from folder')


if __name__ == "__main__":
    main()
