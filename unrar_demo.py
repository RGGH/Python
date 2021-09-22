# import rarfile
# rf = rarfile.RarFile("Wallpaper.rar")
# for f in rf.infolist():
#     print(f.filename, f.file_size)
#     if f.filename == "README":
#         print(rf.read(f))


# import zipfile
# with zipfile.ZipFile('Wallpaper.rar', 'r') as zip_ref:
#     zip_ref.extractall('.')

# import shutil
# shutil.unpack_archive('Wallpaper.rar', '.')

from rarfile import RarFile
with RarFile('Wallpaper.rar', 'r') as extr:
     extr.extractall()
