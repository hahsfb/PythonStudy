from django.shortcuts import render
from .model import Person, Video
import cv2
import numpy as np
import imutils
from .motion_detector import runCamera


def show_main(request):
    personData = Person.objects.raw("SELECT * FROM reko_people")
    # te = Person.objects.get(people_id=1).age
    # te1 = Person.objects.select_related('age').get(people_id=1)
    # age = Person.objects.filter(peopple_id=1).values('age')

    # pp = Video.objects.select_related().filter(video_id=11)
    # # p.name for p in pp
    # for p in pp:
    #     print(p)
    # # print(pp)
    #
    # age1 = personData[0]
    # print(age1.sex)
    # print(age1.age)
    # for p in age1:
    #     print(p.sex)
    #     print(p.age)
    return render(request, 'main.html', {'title': 'Hello World!!', "msg": "Good"})


def deal_video(request):
    camera = cv2.VideoCapture(0)  # 参数0表示第一个摄像头
    # camera = cv2.VideoCapture("D:/Document/WeChat Files/hsfbhao539/Files/office/foreground.avi")
    # 判断视频是否打开
    if camera.isOpened():
        print('Open')
    else:
        print('摄像头未打开')

    # 测试用,查看视频size
    size = (int(camera.get(cv2.CAP_PROP_FRAME_WIDTH)), int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    print('size:'+repr(size))

    es = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (10, 10))
    kernel = np.ones((5, 5), np.uint8)
    background = None

    while True:
        # 读取视频流
        grabbed, frame_lwpCV = camera.read()
        # 对帧进行预处理，先转灰度图，再进行高斯滤波。
        # 用高斯滤波进行模糊处理，进行处理的原因：每个输入的视频都会因自然震动、光照变化或者摄像头本身等原因而产生噪声。对噪声进行平滑是为了避免在运动和跟踪时将其检测出来。
        # frame_lwpCV = imutils.resize(frame_lwpCV, width=500)
        gray_lwpCV = cv2.cvtColor(frame_lwpCV, cv2.COLOR_BGR2GRAY)
        gray_lwpCV = cv2.GaussianBlur(gray_lwpCV, (21, 21), 0)

        # 将第一帧设置为整个输入的背景
        if background is None:
            background = gray_lwpCV
            continue
        # 对于每个从背景之后读取的帧都会计算其与北京之间的差异，并得到一个差分图（different map）。
        # 还需要应用阈值来得到一幅黑白图像，并通过下面代码来膨胀（dilate）图像，从而对孔（hole）和缺陷（imperfection）进行归一化处理
        diff = cv2.absdiff(background, gray_lwpCV)
        diff = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]  # 二值化阈值处理
        # diff = cv2.adaptiveThreshold(diff, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
        diff = cv2.dilate(diff, es, iterations=2)  # 形态学膨胀n

        # 显示矩形框  # 该函数计算一幅图像中目标的轮廓
        image, contours, hierarchy = cv2.findContours(diff.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for c in contours:
            if cv2.contourArea(c) < 1500:  # 对于矩形区域，只显示大于给定阈值的轮廓，所以一些微小的变化不会显示。对于光照不变和噪声低的摄像头可不设定轮廓最小尺寸的阈值
                continue
            (x, y, w, h) = cv2.boundingRect(c)  # 该函数计算矩形的边界框
            cv2.rectangle(frame_lwpCV, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow('contours', frame_lwpCV)
        cv2.imshow('dis', diff)

        key = cv2.waitKey(1) & 0xFF
        # 按'q'健退出循环
        if key == ord('q'):
            break
    # When everything done, release the capture
    camera.release()
    cv2.destroyAllWindows()


def deal_video1(request):
    runCamera()


def aa(request):
    cv2.ocl.setUseOpenCL(False)
    cap = cv2.VideoCapture("D:/Document/WeChat Files/hsfbhao539/Files/office/foreground.avi")
    #cap = cv2.VideoCapture("D:/Document/WeChat Files/hsfbhao539/Files/office/foreground.avi")

    # 方法一：
    fgbg1 = cv2.BackgroundSubtractorMOG()

    # 方法二：
    fgbg2 = cv2.BackgroundSubtractorMOG2()

    # 方法三：  需要OpenCV3.0
    #kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
    #fgbg3 = cv2.BackgroundSubtractorGMG()

    while True:
        ret, frame = cap.read()
        if ret:
            fg_mask1 = fgbg1.apply(frame)
            fg_mask2 = fgbg2.apply(frame)

            #fgmask3 = fgbg3.apply(frame)
            #fgmask3 = cv2.morphologyEx(fgmask3, cv2.MORPH_OPEN, kernel)

            result = np.hstack((fg_mask1, fg_mask2))
            cv2.imshow('frame', result)

            k = cv2.waitKey(30) & 0xff
            if k == 27:
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()

