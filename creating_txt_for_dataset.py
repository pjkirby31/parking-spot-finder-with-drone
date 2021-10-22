import glob, os

# # Current directory
# current_dir = os.path.dirname(os.path.abspath(__file__))

# print(current_dir)

data_dir = '/content/Dataset'


# Create and/or truncate train.txt and test.txt
file_train = open('/content/gdrive/MyDrive/Parking_Spot/train.txt', 'w+')
file_valid = open('/content/gdrive/MyDrive/Parking_Spot/valid.txt', 'w+')


for pathAndFilename in glob.iglob(os.path.join(data_dir, 'train',"*.jpg")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))

    file_train.write(data_dir + "/" + 'train/' + title + '.jpg' + "\n")

for pathAndFilename in glob.iglob(os.path.join(data_dir, 'valid',"*.jpg")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))

    file_valid.write(data_dir + "/" + 'valid/' + title + '.jpg' + "\n")
