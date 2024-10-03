import os

def get_images_as_list(directory): #get images and checks if the file name after . is accepted
    accepted_files = {'png', 'jpg', 'jpeg', 'gif'} #we need gif? add more if needed
    images_list = []

    for file in os.listdir(directory):
        if file.split('.')[-1].lower() in accepted_files: #returns only correct file types
            images_list.append(file)
    return images_list



