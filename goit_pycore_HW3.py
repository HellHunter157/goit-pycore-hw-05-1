import os
import shutil
file = "source_dir"
nwfle = "dist"




def cpy(fldrfile, distfile):
    for item in os.listdir(fldrfile):
        full_path = os.path.join(fldrfile, item)
        if os.path.isdir(full_path):
            cpy(full_path, distfile)
        else:
            ext = os.path.splitext(item)[1][1:] or "no_extension"
            flext = os.path.join(distfile, ext)
            if not os.path.exists(flext):
                os.makedirs(flext)
            shutil.copy(full_path, flext)





cpy(file, nwfle)
print('aafafv')