from interface import *
import os
from PIL import Image

WIDTH, HEIGHT = photo_label.geometry().width(), photo_label.geometry().height()

def filter(all_object):
    exp = [".jpeg",".jpg",".png",".gif",".bmp"]
    result = list()
    for file in all_object:
        for ex in all_object:
            for ex in exp:
                if file.endswith(ex):
                    result.append(file)

    return result

def choose_workdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
    list_photo.addItems(filter(os.listdir()))

def show_photo():
    global name_photo
    name_photo = list_photo.currentItem().text()
    photo.load(os.path.join(workdir, name_photo))
    photo_label.setPixmap(photo.scaled(WIDTH, HEIGHT, aspectRatioMode=Qt.KeepAspectRatio))

def make_left():
    abs_path_photo = os.path.join(workdir, name_photo)
    with Image.open(abs_path_photo) as photo_obj:
        photo_left = photo_obj.transpose(Image.ROTATE_90)
        new_abs_path_photo = os.path.join(workdir, "image", "left_" + name_photo)
        photo_left.save(new_abs_path_photo)
    photo_label.setPixmap(photo.load(new_abs_path_photo).scaled(WIDTH, HEIGHT, aspectRatioMode=Qt.KeepAspectRation))


folder.clicked.connect(choose_workdir)
list_photo.clicked.connect(show_photo)

window.show()
app.exec_()