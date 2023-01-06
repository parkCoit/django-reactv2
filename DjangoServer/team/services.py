import cv2
import numpy as np
from matplotlib import pyplot as plt

if __name__ == '__main__':

    img_rgb = cv2.imread(r'C:\Users\bitcamp\django-react\DjangoServer\team\img\KR_6277840301\0.png')

    # # inRange 함수 이용하여 색으로 뽑기
    # src_hsv = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2HSV)
    # dst1 = cv2.inRange(img_rgb, (0, 0, 0), (212, 41, 41))
    # dst2 = cv2.inRange(src_hsv, (0, 0, 0), (225, 50, 45))
    #
    # cv2.imshow('src', img_rgb)
    # cv2.imshow('dst1', dst1)
    # cv2.imshow('dst2', dst2)
    # cv2.waitKey()
    #
    # cv2.destroyAllWindows()

    #gray
    # img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    # edges = cv2.Canny(np.array(img_gray), 50, 51)
    # plt.subplot(121), plt.imshow(img_gray, cmap='gray')
    # plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    # plt.subplot(122), plt.imshow(edges, cmap='gray')
    # plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    #
    # lines = cv2.HoughLinesP(edges, 1, np.pi / 180., 10, minLineLength=50, maxLineGap=5)
    # if lines is not None:
    #     for i in range(lines.shape[0]):
    #         pt1 = (lines[i][0][0], lines[i][0][1])
    #         pt2 = (lines[i][0][2], lines[i][0][3])
    #         cv2.line(img_gray, pt1, pt2, (255, 0, 0), 2, cv2.LINE_AA)
    #
    # plt.show()

    # matchTemplate함수 사용하여
    template = cv2.imread(r'C:\Users\bitcamp\django-react\DjangoServer\team\labels\빨강와드.png')
    h, w = template.shape[:-1]

    res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
    threshold = .48
    loc = np.where(res >= threshold)


    for pt in zip(*loc[::-1]):  # Switch collumns and rows
        print(pt)
        cv = cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    cv2.imwrite('ad.png', cv)