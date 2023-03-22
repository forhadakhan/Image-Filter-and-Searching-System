import os
import face_recognition
from shutil import copyfile
from PIL import Image, ImageDraw


def main():
        
        print("\n")
        print("________________________________________")
        print("________________  MENU  ________________")
        print()
        print(" 1. Separate images of a person")
        print(" 2. Separate images of a group of people")
        print(" 3. Identify known persons in a image")
        print(" 0. Exit")
        print("\n")

        cmd = input(" Which operation you would like to run? \n _> ")
        
        if cmd == '0':
            print("\n !! Program Closed.")
            exit()
        elif cmd == '1':
            separate_images_of_a_person()
        elif cmd == '2':
            separate_images_of_a_group()
        elif cmd == '3':
            identify_known_persons()
        else:
            print("\n== Invalid Input ==\n")
            # Return to main()
            main()
## end of main()


def separate_images_of_a_person():

    print("\n Starting the operation.\n")

    total_face_count = 0

    # Take location of all images to search
    source_directory = "./images/inputs/"
    
    # Take target persons image
    target_file_directory = "./images/training/"
    target_file_name = input(f"Enter the target file name (with extension) located in '{target_file_directory}' \n _> ")
    if not os.path.isfile(target_file_directory + target_file_name):
        print("\n !! Photo not found. Try again.\n")
        # Try again
        separate_images_of_a_person()

    # Create a destination directory to store target images
    destination_directory = "./images/outputs/" + target_file_name.split('.')[0] + "/"
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    # Create an encoding of target facial features that can be compared to other faces
    picture_of_target = face_recognition.load_image_file(target_file_directory + target_file_name)
    target_face_encoding = face_recognition.face_encodings(picture_of_target)[0]

    # Iterate through all the pictures in source directory
    for file_name in os.listdir(source_directory):

        # Check if the file is an image
        if file_name.endswith(".jpg") or file_name.endswith(".jpeg") or file_name.endswith(".png"):
            print("Checking:", file_name)
            # Store file directory
            current_file_directory = os.path.join(source_directory, file_name)
        else:
            print("NOT AN IMAGE -", file_name)
            continue

        # Load new/current picture from source directory
        new_image = face_recognition.load_image_file(current_file_directory)
        total_face_count += len(face_recognition.face_locations(new_image))

        # Iterate through every face detected in the new picture
        for face_encoding in face_recognition.face_encodings(new_image):

            # Run the algorithm of face comaprison for the detected face, with 0.5 tolerance.
            # Higher tolerance tells the algorithm to be less strict, while lower means the opposite.
            results = face_recognition.compare_faces([target_face_encoding], face_encoding, 0.5)

            # Save the image to destination directory if there is a match
            if results[0] == True:
                copyfile(current_file_directory, destination_directory + file_name)

    print("\n Operation Completed.")
    print(f" Total {total_face_count} face checked.")
    print(f" Check '{destination_directory}' directory to see outputs")
## end of separate_images_of_a_person()


def separate_images_of_a_group():

    total_face_count = 0

    print("\n Starting the operation.\n")

    # Take target persons image location
    target_img_directory = "./images/training/"

    # Take location of all images to search
    source_directory = "./images/inputs/"

    # Create a destination directory to store target images
    destination_directory = "./images/outputs/new/"
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    # Iterate through all the pictures in target persons image directory and
    # Create an encoding of target peoples facial features that can be compared to other faces
    target_face_encodings = []
    for file_name in os.listdir(target_img_directory):
        picture_of_target = face_recognition.load_image_file(target_img_directory + file_name)
        target_face_encoding = face_recognition.face_encodings(picture_of_target)[0]
        target_face_encodings.append(target_face_encoding)


    # Iterate through all the pictures in source directory
    for file_name in os.listdir(source_directory):

        # Check if the file is an image
        if file_name.endswith(".jpg") or file_name.endswith(".jpeg") or file_name.endswith(".png"):
            print("Checking:", file_name)
            # Store file directory
            current_file_directory = os.path.join(source_directory, file_name)
        else:
            print("NOT AN IMAGE -", file_name)
            continue

        # Load new/current picture from source directory
        new_image = face_recognition.load_image_file(current_file_directory)
        total_face_count += len(face_recognition.face_locations(new_image))

        # Iterate through every face detected in the new picture
        for face_encoding in face_recognition.face_encodings(new_image):

            # Run the algorithm of face comaprison for the detected face, with 0.5 tolerance.
            # Higher tolerance tells the algorithm to be less strict, while lower means the opposite.
            results = face_recognition.compare_faces(target_face_encodings, face_encoding, 0.5)

            # Save the image to destination directory if there is a match
            if True in results:
                copyfile(current_file_directory, destination_directory + file_name)

    print("\n Operation Completed.")
    print(f" Total {total_face_count} face checked.")
    print(f" Check '{destination_directory}' directory to see outputs")
## end separate_images_of_a_group()


def identify_known_persons():

    total_face_count = 0

    print("\n Starting the operation.\n")
    
    # Take target persons image
    target_img_directory = "./images/training/"

    # Take location of all images to search
    source_directory = "./images/inputs/"

    # Create a destination directory to store target images
    destination_directory = "./images/outputs/identified/"
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    # Iterate through all the pictures in source directory, store persons name and
    # Create an encoding of target peoples facial features that can be compared to other faces
    target_face_encodings = []
    person_name= []
    for file_name in os.listdir(target_img_directory):
        picture_of_target = face_recognition.load_image_file(target_img_directory + file_name)
        target_face_encoding = face_recognition.face_encodings(picture_of_target)[0]
        target_face_encodings.append(target_face_encoding)
        person_name.append(file_name.split('.')[0])

    # Iterate through all the pictures in source directory
    for file_name in os.listdir(source_directory):

        # Check if the file is an image
        if file_name.endswith(".jpg") or file_name.endswith(".jpeg") or file_name.endswith(".png"):
            print("Checking:", file_name)
        else:
            print("NOT AN IMAGE -", file_name)
            continue
        
        # Load new/current image to find faces in
        new_image = face_recognition.load_image_file(source_directory + file_name)
        total_face_count += len(face_recognition.face_locations(new_image))

        # Find faces in new image
        new_face_locations = face_recognition.face_locations(new_image)
        new_face_encodings = face_recognition.face_encodings(new_image, new_face_locations)

        # Convert to PIL format
        pil_image = Image.fromarray(new_image)

        # Create a ImageDraw instance
        draw = ImageDraw.Draw(pil_image)

        # Loop through faces in new/current image
        for(top, right, bottom, left), face_encoding in zip(new_face_locations, new_face_encodings):
            
            # Run the algorithm of face comaprison for the detected face, with 0.5 tolerance.
            # Higher tolerance tells the algorithm to be less strict, while lower means the opposite.
            results = face_recognition.compare_faces(target_face_encodings, face_encoding, 0.5)

            name = "Unknown"

            # If there is a match
            if True in results:
                first_match_index = results.index(True)
                name = person_name[first_match_index]
            
            # Draw rectangle
            draw.rectangle(((left, top), (right, bottom)), outline=(255,255,0))

            # Show name
            text_width, text_height = draw.textsize(name)
            draw.rectangle(((left,bottom - text_height - 10), (right, bottom)), fill=(0,0,0), outline=(255,255,0))
            draw.text((left + 6, bottom - text_height - 5), name, fill=(255,255,0))

        del draw

        # Show image
        pil_image.show()

        # Save image
        pil_image.save(destination_directory + file_name)

    print("\n Operation Completed.")
    print(f" Total {total_face_count} face checked.")
    print(f" Check '{destination_directory}' directory to see outputs")
## end identify_known_persons()


# Call the main function:
if __name__ == "__main__":
    main()
