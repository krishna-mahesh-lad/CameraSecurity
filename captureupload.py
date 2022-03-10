import cv2
import random
import time
import dropbox

start_time = time.time()
def snapshot():
    number = random.randint(0, 100)
    cap = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame = cap.read()
        img_name = 'Img' + str(number) + '.jpg'
        cv2.imwrite(img_name, frame)
        start_time = time.time
        result = False
    return img_name
    print('Your snip has been taken :3')
    cap.release()
    cv2.destroyAllWindows()

def uploadFiles(img_name):
    access_token = 'sl.BDiJTnrryASZXM3pZ4lBLBDEo7lppaUjGflqxw_qfE4zE6cMFiXychMWqSuXu0ooOEjJ2w02euRjfGp4a7EjD86RdPjf1z8Sifj2ZBZGDTuTtrfrTRJDqmORs9uJmbpPRWuva5c'
    file_from = img_name
    file_to = '/Security8110/' + (img_name)
    dbx = dropbox.Dropbox(access_token)
    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print('Files successfully uploaded')

def main():
    while(True):
        if((time.time() - start_time) >= 5):
            name = snapshot()
            uploadFiles(name)

main()