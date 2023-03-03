

if __name__ == '__main__':
    from PIL import Image
    for i in range(0,108):
        img = Image.open(f'./img/KR_6277908244/{i}.png')

        img_resize = img.resize((512, 512))
        img_resize.save(f'./img/KR_6277908244/{i}.png')

    # from PIL import Image
    #
    # for i in range(0, 32):
    #     img = Image.open(f'C:/Users/bitcamp/Desktop/yolov5-master/data/images/train/{i}.png')
    #
    #     img_resize = img.resize((512, 512))
    #     img_resize.save(f'C:/Users/bitcamp/Desktop/yolov5-master/data/images/train/{i}.png')

