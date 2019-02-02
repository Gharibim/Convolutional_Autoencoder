import math
import ast


def euclidean_distance(x, y):
    """ return euclidean distance between two lists """
    return math.sqrt(sum(pow(a - b, 2) for a, b in zip(x, y)))



def square_rooted(x):
    return round(math.sqrt(sum([a * a for a in x])), 3)

def cosine_similarity(x, y):
    numerator = sum(a * b for a, b in zip(x, y))
    denominator = square_rooted(x) * square_rooted(y)
    return round(numerator / float(denominator), 3)


def manhattan_distance(x, y):
    return sum(abs(a - b) for a, b in zip(x, y))


#To read the lists from the file
with open('output_pup.txt') as readdog:
    with open('output.txt') as readpup:
        dog = readdog.read().splitlines()
        dog = ast.literal_eval(dog[0])


        pup = readpup.read().splitlines()
        pup = ast.literal_eval(pup[0])

        # to calculate the euclidean_distance
        avg = 0
        for i in range(len(dog)):

            avg += euclidean_distance(dog[i], pup[i])
            avg = avg/len(dog)
        print(avg)




# ============ Get the vector from the original image

# import cv2
#
# img = cv2.imread("dog.jpg")
# print(img.shape)
#
# img_after = cv2.resize(img,(350,350))
# print(img_after.shape)
#
# raw = img_after.flatten()
# print(raw)

