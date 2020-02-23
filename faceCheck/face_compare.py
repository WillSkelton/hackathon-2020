from facenet_pytorch import InceptionResnetV1
from facenet_pytorch import MTCNN
import face_recognition
from PIL import Image
import sys
import os
import torch


def checkForFace(filepath):

    img = Image.open(filepath)

    # number of threads
    workers = 0 if os.name == 'nt' else 4

    # tell py torch what device
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

    # create the "classifier"
    mtcnn = MTCNN(device=device)

    # Get the training for the classifier
    resnet = InceptionResnetV1(pretrained='vggface2').eval().to(device)

    _, prob = mtcnn(img, return_prob=True)

    if prob != None:
        prob = True
    else:
        prob = False

    return prob


def compare(img_1_filepath, img_2_filepath):

    known_image = face_recognition.load_image_file(img_1_filepath)
    unknown_image = face_recognition.load_image_file(img_2_filepath)

    img_1_encoding = face_recognition.face_encodings(
        known_image)
    if len(img_1_encoding) == 0:
        return "No face"
    else:
        img_1_encoding = img_1_encoding[0]

    img_2_encoding = face_recognition.face_encodings(
        unknown_image)
    if len(img_2_encoding) == 0:
        return "No face"
    else:
        img_2_encoding = img_2_encoding[0]

    results = face_recognition.compare_faces(
        [img_1_encoding], img_2_encoding, tolerance=0.75)

    return results


def compareDir(dir, picture):

    compare_pictures = os.listdir(dir)

    matches = []
    path = os.path.dirname(dir)

    for pic in compare_pictures:
        if str(path) + "/" + str(pic) != picture and compare(str(path) + "/" + str(pic), picture) == [True]:
            matches.append(pic)

    return matches
