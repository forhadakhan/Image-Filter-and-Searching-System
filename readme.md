# Image Filter and Searching System

This was a class project of mine from 2020. My goal was to create a system that will be able to find and separate a specific person or a group of people's images from a local folder where exists thousands of images of various peoples.
To do so, I used python and a library called '[face_recongnition](https://pypi.org/project/face-recognition/)'.


### Features:  
<ul>
  <li> It's a console-based program </li>
  <li> Consists of three options: </li>
  <ol>
    <dl>
        <dt>1. Separate images of a person:</dt>
        <dd>This function takes the image name of the target person (located in <code>./images/training/</code> directory) and searches all the images available in the <code>./images/inputs/</code> directory. As output, it copies all of those images which consists target person and save in a folder at <code>./images/outputs/</code> directory.</dd>
    </dl>
  </ol>
  <ol>
      <dl>
        <dt>2. Separate images of a group of people:</dt>
        <dd>This function takes all the images located in the <code>./images/training/</code> directory as target person image and searches all the images available in the <code>./images/inputs/</code> directory. As output, it copies all of those images which consists target person, and saves them in a folder at the <code>./images/outputs/</code> directory.</dd>
      </dl>
  </ol>
  <ol>
    <dl>
      <dt>3. Identify known persons in an image:</dt>
      <dd>This function takes all the images available in the <code>./images/training/</code> directory as known persons and search all the images available in the <code>./images/inputs/</code> directory. As output, it shows each image with an identified person, if the person is known then it will show the person (image) name otherwise it will show unknown. It also saves an identified copy of those images in a folder at the <code>./images/outputs/</code> directory.</dd>
    </dl>
  </ol>    
</ul>

<br><br>


### To run this program you need:  
  - Python 3  and  
  - [face_recongnition](https://pypi.org/project/face-recognition/) installed  


### Procedure to run:
  - Download or Clone this repository.  
  - Put all the images you wanna search or filter at <code>./images/inputs/</code> directory.  
  - Put all the target person's image (training images) at <code>./images/training/</code> directory.
  - Run the `main.py` file.
  - Follow instructions shown in the console.

