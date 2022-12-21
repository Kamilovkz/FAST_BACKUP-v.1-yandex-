# fast backup files (solution by Kamilovkz)

Best solution for backup your files using Python (yandex)

Before run project do these few steps of instructions:
1. This is where we create the application, https://oauth.yandex.ru/. (Place where we save all files is Yandex Disc)
2. We need to specify the name, check the box "Platforms" - Web services, Accesses - Yandex Rest API (all), Yandex.Disk WebDAV API (all).
3. After that copy ID/ and go to https://oauth.yandex.ru/authorize?response_type=token&client_id=HEREYOURID
4. You will see a small API, paste this into the code on line 26 
5. After compiling, you can change types of files for searching (PDF & WORD in this project) 
After compilation, program delete archive files which was created before, and the archive sends to your Yandex Disk.
6. Enjoy!

Some results:
![12](https://user-images.githubusercontent.com/38252272/160374640-99099b60-4b32-4b5b-b2fc-d0fc3802f3ae.jpg)
