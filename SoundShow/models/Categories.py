import os
from PIL import Image
# This class is suppsoed to represent a Category model
# This entire folder might end up ebign removed Im just playing around with
# something called the Object Relation Model
# Dont Worry about anything here

class Category:
    def __init__(self, cat_name):
        self.cwd = os.path.dirname(__file__)
        self.rel_path = "../images/"
        self.abs_file_path = os.path.join(self.cwd, self.rel_path)
        self.image_file = cat_name + ".jpg"
        self.cat_name = cat_name
        self.image_path = self.abs_file_path + self.image_file
    def jsonify(self):
        return {
            "cat_name" : self.cat_name,
            "path" : self.image_path
        }

if __name__ == "__main__":
    data = Category("art").jsonify()
    path = data["path"]
    print(data)
    # im = Image.open(path)
    # im.show()