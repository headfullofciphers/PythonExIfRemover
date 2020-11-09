# -*- coding: utf-8 -*-
from exif import Image
import taglib
import shutil
import os

def clear_vid(filename):
    file_mod = filename.split('.')
    file_mod = file_mod[0]+_cleaned+'.'+file_mod[1]
    
    shutil.copyfile(filename, file_mod) #shutil.copy does not copy metadata
    #just to make sure:
    v = taglib.File(file_mod)
    keys = v.tags.keys()
    for tag in list(keys):
        del v.tags[tag]
    v.save()
    
def clear_img(filename):
    file_mod = filename.split('.')
    file_mod = file_mod[0]+_cleaned+'.'+file_mod[1]
   
    with open(filename, 'rb') as image_file:
        my_image = Image(image_file)
    
    
    for element in dir(my_image):
        try:
            print(f"{element}:  {my_image[element]}")
            del my_image[element]
        except:
            print(f"{element} unknown")
    
    with open(file_mod, 'wb') as new_image_file:
    	new_image_file.write(my_image.get_file())
    print(f'File {filename} cleared and saved as a {file_mod}')


directory = r'D:\HFOC\arts\'
img_extenstions = ('.jpg','.JPG','.png','.PNG')
video_extenstions = ('.avi', '.AVI', '.mp4', '.MP4')
_cleaned = '_cleaned'

all_imgs = []
all_videos = []

cleaned_imgs = []
cleaned_videos = []
need_cleaning = []

for subdir, dirs, files in os.walk(directory):
    for filename in files:
        filepath = subdir + os.sep + filename
        if filepath.endswith(img_extenstions):
            all_imgs.append(filepath)
        elif filepath.endswith(video_extenstions):
            all_videos.append(filepath)



for img in all_imgs[:]:
    if img.split(os.sep)[-1].split('.')[-2].endswith(_cleaned):
        cleaned_imgs.append(img.split(os.sep)[-1].split('.')[-2].replace(_cleaned, ''))
 
for video in all_videos[:]:
    if video.split(os.sep)[-1].split('.')[-2].endswith(_cleaned):
        cleaned_videos.append(video.split(os.sep)[-1].split('.')[-2].replace(_cleaned, ''))

if len(cleaned_imgs)>0:
    for img in all_imgs:
            for cleaned in cleaned_imgs:
                if not img.split(os.sep)[-1].split('.')[-2].startswith(cleaned):
                    need_cleaning.append(img)
else:
    need_cleaning += all_imgs

if len(cleaned_videos)>0:
    for video in all_videos:
        for cleaned in cleaned_videos:
            if not video.split(os.sep)[-1].split('.')[-2].startswith(cleaned):
                need_cleaning.append(video)
else:
    need_cleaning += all_videos

for media in need_cleaning:
    if media.endswith(img_extenstions):
        try:
            clear_img(media)
        except Exception:
            pass
    elif media.endswith(video_extenstions):
        clear_vid(media)




