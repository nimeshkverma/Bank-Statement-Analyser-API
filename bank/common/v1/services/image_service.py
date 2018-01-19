from PIL import Image


class ImageResizer(object):

    def __init__(self, image_path, size):
        self.image_path = image_path
        self.size = size

    def resize(self):
        try:
            im = Image.open(self.image_path)
            im.thumbnail(self.size, Image.ANTIALIAS)
            im.save(self.image_path, "JPEG")
        except IOError:
            print "cannot create thumbnail for '%s'" % infile
