from post_to_text_class import *
import json


input1 = input("Would you like to write your Post.IO to a file?: ")

while input1 != 'no':
    input2 = input("What is your post code?: ")
    if input2 != 'exit':
        get_post_json(input2)

        input3 = input('What file would you like to write this to?: ')
        if input3 != 'none':
            open_write_post_file(input3, get_post_json(input2))

        else:
            break
    else:
        break




