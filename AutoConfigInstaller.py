import collections
import glob
import os
import shutil
import pathlib
from winregistry import WinRegistry
from valve_keyvalues_python.keyvalues import KeyValues
import platform

if platform.architecture()[0] == "64bit":
    strSteamInstallPath = r"HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Valve\Steam"
else:
    strSteamInstallPath = r"HKEY_LOCAL_MACHINE\SOFTWARE\Valve\Steam"

strSteamInstallPath = r"HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Valve\Steam"
if __name__ == "__main__":
    with WinRegistry() as client:
        steamPath = client.read_entry(strSteamInstallPath, "InstallPath")

strSteamLibraryPath = steamPath.value + r"\steamapps\libraryfolders.vdf"

filename_vdf = strSteamLibraryPath

kv = KeyValues(filename=filename_vdf)

h = collections.OrderedDict(kv["libraryfolders"])
disksNumbers = list(h.items())

disk = 0
d = collections.OrderedDict(kv["libraryfolders"][str(disk)]["apps"])
items = list(d.items())

for disk in range(len(disksNumbers)):
    i = 0
    d = kv["libraryfolders"][str(disk)]["apps"]
    items = list(d.items())
    for i in range(len(items)):
        if items[i][0] != "730":
            i = i + 1
        else:
            GamesLibPath = kv["libraryfolders"][str(disk)]["path"]
    disk = str(disk) + "1"
    total = sum(int(j) for j in disk)
    disk = total

src_folder = pathlib.Path().resolve()
main_src_folder = str(src_folder)
background_src_folder = str(src_folder)
cfg_dst_folder = GamesLibPath + r"\steamapps\common\Counter-Strike Global Offensive\csgo\cfg\\"
background_dst_folder = GamesLibPath + r"\steamapps\common\Counter-Strike Global Offensive\csgo\panorama\videos\\"
video_dst_folder = steamPath.value + r'\userdata'

# list file and directories
res = os.listdir(video_dst_folder)
print(res)

# Search files with the specified extension/name in source directory
pattern_1 = main_src_folder + r'\video*'
pattern_2 = "\*.cfg"
pattern_3 = "\*.webm"
main_files = glob.glob(main_src_folder + pattern_2)
background_files = glob.glob(background_src_folder + pattern_3)

# prints all directories in a path, copies them and iterates to get to each account and paste video.txt
for i in range(len(res)):
    video_updated_folder = steamPath.value + r'\userdata' + '\x5c' + res[i] + r'\730\local\cfg\\'
    print(video_updated_folder)
    # move file whose name starts with specified name
    for file in glob.iglob(pattern_1, recursive=True):
        # extract file name form file path
        file_name = os.path.basename(file)
        shutil.copy2(file, video_updated_folder + file_name)
        print('Copied:', file)

# move the files with cfg extension
for file in main_files:
    file_name = os.path.basename(file)
    shutil.copy2(file, cfg_dst_folder + file_name)
    print('Copied:', file)

# move the files with webm extension
for file in background_files:
    file_name = os.path.basename(file)
    shutil.copy2(file, background_dst_folder + file_name)
    print('Copied:', file)