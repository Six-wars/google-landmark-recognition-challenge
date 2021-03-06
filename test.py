from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
import numpy as np

model = load_model('last_model.h5')

# dimensions of our images.
img_width, img_height = 250, 250

test_data_dir = 'test_images'

test_datagen = ImageDataGenerator(rescale=1. / 255)

test_generator = test_datagen.flow_from_directory(
    test_data_dir,
    target_size=(img_width, img_height))
    
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

#scoreSeg = model.evaluate_generator(test_generator,100)
#print("Accuracy = ",scoreSeg[1])

predict = model.predict_generator(test_generator)

np.save('prediction.npy', predict)

