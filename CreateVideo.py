import os
import cv2

path = "Imagens/"

imagens = []
for file in os.listdir(path):
    name, extension = os.path.splitext(file)
    if extension.lower() in ['.jpg', '.jpeg', '.png', '.bmp']:
        file_name = os.path.join(path, file)
        print(file_name)
        imagens.append(file_name)

count = len(imagens)

frame = cv2.imread(imagens[0])
size = (frame.shape[1], frame.shape[0])
print(size)

out = cv2.VideoWriter('Project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

for i in range(count):
    image = cv2.imread(imagens[i])
    out.write(image)

out.release()
print("Concluído")