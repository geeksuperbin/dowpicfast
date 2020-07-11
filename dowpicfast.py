import requests 
import random
import string


def download(img_link):
    from urllib.request import urlretrieve
    import os 
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 16))
    urlretrieve(img_link, './pics/'+ ran_str +'.jpg') 





def read_file(file):
    pics = [];
    f = open(file, "r")
    for x in f:
        pics.append(x.strip())

    return pics



if __name__ == "__main__":
    pics = read_file('./yourseed')
    c = 0
    for pic in pics:
        download(pic)
        c = c + 1
        print(str(c) + ' ==== ' + pic)
    