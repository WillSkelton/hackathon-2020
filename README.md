# AutoSwiper

AutoSwiper is a dating website in which you create a profile for yourself and upload photos of people you find attractive. AutoSwiper will use facial recognition software to automatically generate matches with other users based on the people that you find attractive. 

## How It Works

The facial recognition software looks at the faces of the photos that you provide when creating your account. PyTorch provides a pretrained MTCNN classifier which recognizes faces. This classifier is then applied to images containing faces and extracts the face from them. This eliminates people uploading photos which do not contain their faces. A separate facial recognition libarary then searches through the lists of user profiles to find faces which are similar the images provided by the user. Matches found are then stored on your profile. If two users match, then they would then be able to open up a chat with each other. 

## Getting Started

Since this project uses GO, use the following command to launch the website:
```
go run main.go
```

## Dependencies

AutoSwiper requires **Python** and **GO** in order to run the website and backend.

AutoSwiper makes use of both PyTorch and a facial recognition Python library for generating matches.
As such, you will need the following Python modules in order to run this project:

```
pip install facenet-pytorch
```
```
pip install face-recognition
```

## Developers
 
Mitchell Greer

Will Skelton

Bryce Turley