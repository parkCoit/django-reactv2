import sys

import cv2
import numpy as np
from matplotlib import pyplot as plt

if __name__ == '__main__':

    img_rgb = cv2.imread('./img/KR-6277840301/0.png')
    print(img_rgb.shape)

    # inRange 함수 이용하여 색으로 뽑기
    src_hsv = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2HSV)
    lower_red = np.array([90, 20, 20])
    upper_red = np.array([255, 100, 100])
    lower_blue = np.array([0, 20, 100])
    upper_blue = np.array([30, 170, 255])
    dst1 = cv2.inRange(src_hsv, lower_red, upper_red)
    dst2 = cv2.inRange(img_rgb, lower_blue, upper_blue)
    kernel = np.ones((5, 5), np.uint8)

    cv2.imshow('src', img_rgb)
    cv2.imshow('dst1', dst1)
    cv2.imshow('dst2', dst2)
    cv2.waitKey()

    cv2.destroyAllWindows()

    # gray
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
    # template = cv2.imread(r'C:\Users\bitcamp\django-react\DjangoServer\team\labels\빨강와드.png', 0)
    # w, h = template.shape[::-1]
    # print(w, h)
    #
    # res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF)
    # min_val, max_val, min_lod, max_lod = cv2.minMaxLoc(res)
    #
    # top_left = min_lod
    # bottom_right = (top_left[0] + w , top_left[1] + h)
    # cv2.rectangle(img_rgb, top_left, bottom_right, 255, 2)
    # plt.subplot(121),plt.imshow(res,cmap='gray')
    # plt.title('asd'),plt.xticks([]),plt.yticks([])
    # plt.subplot(122), plt.imshow(img_rgb, cmap='gray')
    # plt.title('zvzc'), plt.xticks([]), plt.yticks([])
    # plt.show()

    # img = cv2.medianBlur(img_rgb, 5 )
    # cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    #
    # circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=25, minRadius=0, maxRadius=0)
    #
    # circles = np.uint16(np.around(circles))
    #
    # for i in circles[0, :]:
    #     cv2.circle(cimg, (i[0], i[1]), i[2], (0, 153, 224), 2)
    #     cv2.circle(cimg, (i[0], i[1]), 2, (232, 61, 61), 3)
    #
    # cv2.imshow('img', cimg)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # import numpy as np
    # import cv2
    # from matplotlib import pyplot as plt
    # from PIL import Image
    #
    # from mss import mss
    # from detection import DetectionManager
    #
    #
    # def capture_screenshot():
    #     # Capture entire screen
    #     with mss() as sct:
    #         monitor = sct.monitors[1]
    #         sct_img = sct.grab(monitor)
    #         # Convert to PIL/Pillow Image
    #         return np.array(Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX'))
    #
    # icons_folder = 'icons'
    # minimap_ratio = 800 / 1080  # How big is the minimap width?
    # icon_ratio = 25 / 280  # 280 is the width/height of icons
    # icon_search_ratio = 0.5  # percentage of the champion icon to be used in matchTEmplate
    # threshold = 0.6  # threshold for matchTemplate
    #
    #
    # def main():
    #     dm = DetectionManager(icons_folder, minimap_ratio, icon_ratio, icon_search_ratio, threshold)
    #
    #     fig = plt.figure(figsize=(20, 20))
    #     ax1 = fig.add_subplot(2, 4, 1)
    #     ax2 = fig.add_subplot(2, 4, 2)
    #     ax3 = fig.add_subplot(2, 4, 3)
    #     ax4 = fig.add_subplot(2, 4, 4)
    #     ax5 = fig.add_subplot(2, 4, 5)
    #     ax6 = fig.add_subplot(2, 4, 6)
    #     ax7 = fig.add_subplot(2, 4, 7)
    #     ax8 = fig.add_subplot(2, 4, 8)
    #
    #     ax1.set_title('minimap')
    #     ax2.set_title('red filter')
    #     ax3.set_title('red contours')
    #     ax4.set_title('red detection')
    #     ax5.set_title('minimap')
    #     ax6.set_title('blue filter')
    #     ax7.set_title('blue contours')
    #     ax8.set_title('blue detection')
    #
    #     screenshot = capture_screenshot()
    #     minimap, icon_size = dm.get_minimap_and_icon_size(screenshot)
    #     icons = dm.get_icons(icon_size)
    #
    #     while True:
    #         screenshot = capture_screenshot()
    #         minimap, icon_size = dm.get_minimap_and_icon_size(screenshot)
    #
    #         red_filter_minimap = dm.filter_red(minimap)
    #         blue_filter_minimap = dm.filter_blue(minimap)
    #         red_contours_minimap, red_final_minimap = dm.find_champions(minimap, icons, red_filter_minimap, [0, 255, 0])
    #         blue_contours_minimap, blue_final_minimap = dm.find_champions(minimap, icons, blue_filter_minimap,
    #                                                                       [0, 255, 0])
    #
    #         ax1.imshow(minimap, interpolation='bilinear')
    #         ax2.imshow(red_filter_minimap, interpolation='bilinear')
    #         ax3.imshow(red_contours_minimap, interpolation='bilinear')
    #         ax4.imshow(red_final_minimap, interpolation='bilinear')
    #         ax5.imshow(minimap, interpolation='bilinear')
    #         ax6.imshow(blue_filter_minimap, interpolation='bilinear')
    #         ax7.imshow(blue_contours_minimap, interpolation='bilinear')
    #         ax8.imshow(blue_final_minimap, interpolation='bilinear')
    #
    #         fig.canvas.draw()
    #         fig.canvas.flush_events()
    #         plt.tight_layout()
    #         plt.pause(0.0001)
    #
    #
    # if __name__ == "__main__":
    #     main()