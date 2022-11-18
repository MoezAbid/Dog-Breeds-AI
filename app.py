import gradio as gr
import os
import numpy as np
import keras
import cv2
from keras.preprocessing.image import ImageDataGenerator
from keras.applications import MobileNetV2
from keras.applications.mobilenet_v2 import preprocess_input
from keras.models import Sequential
from keras.layers import Input, Lambda, GlobalAveragePooling2D, Dropout, Dense
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint
from PIL import Image
model = keras.models.load_model('./model/')

class_mapping = {0: 'Afghan',
 1: 'African Wild Dog',
 2: 'Airedale',
 3: 'American Hairless',
 4: 'American Spaniel',
 5: 'Basenji',
 6: 'Basset',
 7: 'Beagle',
 8: 'Bearded Collie',
 9: 'Bermaise',
 10: 'Bichon Frise',
 11: 'Blenheim',
 12: 'Bloodhound',
 13: 'Bluetick',
 14: 'Border Collie',
 15: 'Borzoi',
 16: 'Boston Terrier',
 17: 'Boxer',
 18: 'Bull Mastiff',
 19: 'Bull Terrier',
 20: 'Bulldog',
 21: 'Cairn',
 22: 'Chihuahua',
 23: 'Chinese Crested',
 24: 'Chow',
 25: 'Clumber',
 26: 'Cockapoo',
 27: 'Cocker',
 28: 'Collie',
 29: 'Corgi',
 30: 'Coyote',
 31: 'Dalmation',
 32: 'Dhole',
 33: 'Dingo',
 34: 'Doberman',
 35: 'Elk Hound',
 36: 'French Bulldog',
 37: 'German Sheperd',
 38: 'Golden Retriever',
 39: 'Great Dane',
 40: 'Great Perenees',
 41: 'Greyhound',
 42: 'Groenendael',
 43: 'Irish Spaniel',
 44: 'Irish Wolfhound',
 45: 'Japanese Spaniel',
 46: 'Komondor',
 47: 'Labradoodle',
 48: 'Labrador',
 49: 'Lhasa',
 50: 'Malinois',
 51: 'Maltese',
 52: 'Mex Hairless',
 53: 'Newfoundland',
 54: 'Pekinese',
 55: 'Pit Bull',
 56: 'Pomeranian',
 57: 'Poodle',
 58: 'Pug',
 59: 'Rhodesian',
 60: 'Rottweiler',
 61: 'Saint Bernard',
 62: 'Schnauzer',
 63: 'Scotch Terrier',
 64: 'Shar_Pei',
 65: 'Shiba Inu',
 66: 'Shih-Tzu',
 67: 'Siberian Husky',
 68: 'Vizsla',
 69: 'Yorkie'}

labels = list(class_mapping.values())

def predict(inp):
    img = inp.resize((224, 224))
    img = np.array(img).reshape(1, 224, 224, 3)
    predictions = model.predict(img)
    prediction = np.array(predictions)[0]
    confidences = {labels[i]: float(prediction[i]) for i in range(70)}
    return confidences

def get_example_images():
    examples = os.listdir("./examples")
    for i in range(len(examples)):
        examples[i] = "./examples/" + examples[i]
    return examples

demo = gr.Interface(fn=predict,
            title="Dog Breed Classifier",
            inputs=gr.inputs.Image(type="pil"),
            outputs=gr.outputs.Label(num_top_classes=6),
            examples = get_example_images()
            )
             
demo.launch()