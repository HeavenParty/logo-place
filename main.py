import os
from PIL import Image

input_dir = './input/pictures/'
output_dir = './output'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

top_right: bool = False
top_right_image: Image.Image
if os.path.exists("./input/top_right.png"):
    top_right = True
    top_right_image = Image.open("./input/top_right.png")

bottom_right: bool = False
bottom_right_image: Image.Image
if os.path.exists("./input/bottom_right.png"):
    bottom_right = True
    bottom_right_image = Image.open("./input/bottom_right.png")

# Loop through the input pictures directory
for entry in os.scandir("./input/pictures/"):
    if entry.is_file():
        print(entry.path)
        if entry.name.lower().endswith('.png') or entry.name.lower().endswith('.jpg') or entry.name.lower().endswith("jpeg"):
            # Open the input picture
            picture = Image.open(os.path.join("./input/pictures/", entry.name))

            # Resize the logo to fit on the picture

            if bottom_right:
                scaleproportion: float = 3
                if (picture.width > picture.height):
                    scaleproportion = 4
                
                aspect_ratio: float = picture.width / picture.height
                new_width: int = round(picture.width / scaleproportion)
                new_height: int = round(bottom_right_image.height * (new_width / bottom_right_image.width))

                resized_pic: Image.Image = bottom_right_image.resize((new_width, new_height))
                position: tuple = (picture.width - resized_pic.width, picture.height - new_height)
                picture.paste(resized_pic, position, resized_pic)

            if top_right:
                scaleproportion: float = 3
                if (picture.width > picture.height):
                    scaleproportion = 4
                
                aspect_ratio: float = picture.width / picture.height
                new_width: float = picture.width / scaleproportion
                new_height: float = top_right_image.height * (new_width / top_right_image.width)
                new_sizes = (round(new_width), round(new_height))

                resized_pic: Image.Image = top_right_image.resize(new_sizes)
                position: tuple = (picture.width - resized_pic.width, 0)
                picture.paste(resized_pic, position, resized_pic)

            # Paste the logo onto the picture

            # Save the output picture

            picture.save(os.path.join("./output/", entry.name))

            # Close the images
            picture.close()
