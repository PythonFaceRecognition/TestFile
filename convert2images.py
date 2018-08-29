import face_recognition
import cv2
import os
import dlib


'''def extract_face(img):
    face_locations = face_recognition.face_locations(frame)

    faces = []
    for top, right, bottom, left in face_locations:
        face = img[top: bottom, left:right]
        faces.append(face)

    return faces'''


# the folder containing all the input data
'''輸入的文件檔'''
input_folder = 'C:\\Users\\USER\\Desktop\\Face_Test_photo\\CBSR_database\\test_release\\test_release'

# the folder to store the output results
'''輸出文件檔'''
output_image_folder = 'C:\\Users\\USER\\Desktop\\TeacherCode\\TeacherdatabasePhoto'

# list all the item of the input folder
'''輸入資料夾內的項目'''
items = os.listdir(input_folder)
# make all the items full-path
'''所有項目之路徑'''
for i in range(len(items)):
    items[i] = '{0}\\{1}'.format(input_folder, items[i])

while len(items) > 0:
    # pop the first folder from folders
    '''第一份文件'''
    item = items.pop(0)
    # check the type of the item
    '''檢查題目項目類型'''
    if os.path.isdir(item):
        # the item is type of folder so append it to folders
        '''分類檔案'''
        # print('folder: {0}\n'.format(item))
        '''格式化操作'''
        # list all the items in the item
        '''列出項目'''
        sub_items = os.listdir(item)
        '''分項目格式化'''
        for i in range(len(sub_items)):
            ''''''
            items.append('{0}\\{1}'.format(item, sub_items[i]))
    elif os.path.isfile(item) :
        # the item is type of file so append it to folders
        print('file: {0}'.format(item))

        new_folder = item[:item.rfind('\\')]
        new_folder = new_folder.replace(input_folder, output_image_folder)
        filename_face = item[item.rfind('\\')+1:item.rfind('.avi')]
        if not os.path.exists(new_folder):
          os.makedirs(new_folder)
        print('New folder created: {}'.format(new_folder))

        # if item[-4:].lower() == '.avi':
        cap = cv2.VideoCapture(item)
        # 1. open the avi file and read each frame
        frame_no = 1
        detector = dlib.get_frontal_face_detector()
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                face_rects, scores, idx = detector.run(frame, 0)  # 取出所有偵測的結果
                for i, d in enumerate(face_rects):
                    x1 = d.left()
                    y1 = d.top()
                    x2 = d.right()
                    y2 = d.bottom()
                    crop_img = frame[y1-100:y2+100, x1-100:x2+200 ]
                    cv2.imwrite('{0}\\{1}_{2:0>3d}.png'.format(new_folder, filename_face, frame_no), crop_img)
            else:break
            frame_no = frame_no + 1
            cv2.imwrite('{0}\\{1}_{2:0>3d}.png'.format(new_folder, filename_face, frame_no), crop_img)
        frame_no = frame_no + 1
        cap.release()