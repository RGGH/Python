""" Create cropped image of input text """

# Version 0.03

from PIL import ImageFont, ImageDraw, Image

import os

output_file = 'H.png';
if os.path.exists(output_file):
    os.remove(output_file)
else:
    pass

used_font_size = []

# Supply multiple lines as long as they are seperated by a comma ','
#text = """Hello World Test Example Sentence, Hello World Test Example Sentence12, Hello World Test Example Sentence3"""

input_text = "Hello World , Nice!"# World Python !!!!! Mzwopqa"#, how are you?, this is sentence 3"#Example #in Python and Pillow for Omar using Python 3.10"

text_color_1 = "red"
text_color_2 = "yellow"
text_color_3 = "blue"
background_color = "green"

# Insert path/name of chosen font
font_file = "/usr/share/fonts/truetype/nexa-bold-italic.ttf"
# 
nexa = "nexa-bold-italic.ttf"

# -------------- functions ------------------- #

def check_multiline():

    """ Handles one line or 2 lines of text"""

    number_of_lines = 0
    
    # break string into multi-lines if comma present in text
    for i in enumerate(input_text.split(",")):
        number_of_lines += 1

    sentence_list = input_text.split(",")
  
    length_of_sentence = [len(i) for i in sentence_list]
    longest_sentence = sentence_list[length_of_sentence.index(max(length_of_sentence))]
    len_long_sent = len(longest_sentence)

    return number_of_lines, longest_sentence, len_long_sent, sentence_list


def gen_image(text):

    """Canvas is 800x600 and 
    cropped once text has been applied"""

    w = 800
    h = 600

    #text = "Hello World!!!"
    fontsize = 1  # starting font size

    # portion of image width you want text width to be
    img_fraction = 0.80
    image = Image.new("RGB", (w, h), background_color)

    font = ImageFont.truetype(nexa, fontsize)
    while font.getsize(text)[0] < img_fraction*image.size[0]:
        # iterate until the text size is just larger than the criteria
        fontsize += 1
        font = ImageFont.truetype(nexa, fontsize)

    # optionally de-increment to be sure it is less than criteria
    fontsize -= 1
    used_font_size.append(fontsize)
    
    font = ImageFont.truetype(nexa, fontsize)
    draw = ImageDraw.Draw(image)

    sentence_list = (check_multiline()[3])

    text_chars_wide = len((check_multiline()[1]))
    actual_text_width = text_chars_wide  * used_font_size[0]
    print(actual_text_width)

    # Process One Line - draw and crop
    if len(sentence_list)==1:
        text_1 = sentence_list[0]
        draw.text((w /2, h / 2), text=text_1, fill=text_color_1, font=font, anchor="mm")

        # calcs to crop to 10% all around for 1 line of text #
        box_upper = (h/2)-((used_font_size[0]*1.2)/2)
        box_lower = (h/2)+((used_font_size[0]*1.2)/2)
        box = (0, box_upper, w, box_lower)
    
    # Process Two Lines - draw and crop
    if len(sentence_list)==2:
        text_1 = sentence_list[0]
        draw.text((w /2, h *0.4), text=text_1, fill=text_color_1, font=font, anchor="mm")
        text_2 = sentence_list[1]
        draw.text((w /2, h *0.6), text=text_2, fill=text_color_2, font=font, anchor="mm")

        # calcs to crop to 10% all around for 2 lines of text #
        gap = (h-(2*used_font_size[0]))/3
        box_upper = (gap + (int(used_font_size[0]) * 0.5))
        box_lower = (h - box_upper)
        box = (0+2*used_font_size[0], box_upper, w-2*used_font_size[0], box_lower)
    
    croppedImage = image.crop(box)
    croppedImage.save('H.png') # save it

    # Debug info : 
    print(f"Actual font size = {used_font_size[0]}")
    print(f"Number of characters ={text_chars_wide}")


# Main Driver #
if __name__ == "__main__":

    gen_image(input_text)
