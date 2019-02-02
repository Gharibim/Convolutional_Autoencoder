# imports
import sys
import logging
import numpy as np
import tflearn
from keras.preprocessing import image

import train_encoder

# setup
logging.basicConfig(level=logging.DEBUG)
np.set_printoptions(threshold=sys.maxsize)



# functions
def get_img(img_path):
    logging.debug('loading image at '.format(img_path))
    img = image.load_img(img_path,
                         target_size=train_encoder.IMAGE_INPUT_SIZE)

    return np.expand_dims(image.img_to_array(img), axis=0)


def main():
    model = train_encoder.build_model()
    model = tflearn.DNN(model)

    logging.info('loading checkpoint')
    checkpoint_path = sys.argv[1]
    model.load(checkpoint_path)

    img_path = sys.argv[2]
    img_arr = get_img(img_path)

    logging.info('getting output')
    pred = model.predict(img_arr)

    logging.debug('saving output to output.jpg')
    pred = pred[0].tolist()
    # print(pred.tolist())
    
    #Write the vector to a file
    # with open('output.txt', 'w') as f:
    #     for item in pred.tolist():
    #         f.write("%s\n" % item)



    Input = pred.tolist()
    pred_img = image.array_to_img(pred)
    pred_img.save('output.jpg')


if __name__ == '__main__':
    main()