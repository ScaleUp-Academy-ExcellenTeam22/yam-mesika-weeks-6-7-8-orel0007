# Install pillow library
from PIL import Image
#add commnet for new pull request

# load image
def decipher_image_string(image_path):
    """
    The function use Pillow python library, for use it need to install this library.
    Pillow library allow to iterate over the image pixel and check if its white or black.
    Convert all the black pixel by their row place to char by ascii table using chr
    :return:string by convert the row black pixel to ascii.
    """
    img = Image.open(image_path).convert('RGB')
    pixel = img.load()
    row, col = img.size[0], img.size[1]
    return "".join([chr(j) for i in range(row) for j in range(col) if pixel[i, j] != (255, 255, 255)])


if __name__ == "__main__":
    print(decipher_image_string('code.png'))
