# AutoSwiper

AutoSwiper is a dating website in which you create a profile for yourself and upload photos of people you find attractive. AutoSwiper will use facial recognition software to automatically generate matches with other users based on the people that you find attractive. 

## How It Works

The facial recognition software looks at the faces of the photos that you provide when creating your account. These photos are used as a training set for building a PyTorch MTCNN classifier, which then searches through the lists of user profiles to find faces which match your training set a certain threshold. Users who's profile match with your preferences are then stored on your profile. If two users match, then they would then be able to open up a chat with each other. 

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