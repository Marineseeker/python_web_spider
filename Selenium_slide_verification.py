import cv2

GAUSSIAN_BLUR_KERNEL_SIZE = (5, 5)
GAUSSIAN_BLUR_SIGMA_X = 0
CANNY_THRESHOLD1 = 200
CANNY_THRESHOLD2 = 450

def get_gaussian_blur_image(image):
    """高斯滤波处理"""
    return cv2.GaussianBlur(image, GAUSSIAN_BLUR_KERNEL_SIZE, GAUSSIAN_BLUR_SIGMA_X)
    # def GaussianBlur(src,ksize,sigmaX,dst=None,sigmaY=None,borderType=None)
    """src, 需要处理的图片。
    ksize: 高斯滤波处理所用的高斯内核大小, 需要传人一个元组, 包含x和y两个元素
    sigmaX: 高斯内核函数在x方向上的标准偏差。
    sigmaY: 高斯内核函数在Y方向上的标准偏差。
    若sigmaY为o, 就将它设为sigmaX: 若sigmax和sigmaY都是o, 就通过ksize计算出sigmax和sigmaY。
    """
        
def get_canny_image(image):
    """Canny边缘检测"""
    return cv2.Canny(image, CANNY_THRESHOLD1, CANNY_THRESHOLD2)
    #def Canny(image,threshold1,threshold2,edges=None,apertureSize=None,L2gradient=None)
    """image: 输入图像
    threshold1: 低阈值
    threshold2: 高阈值
    apertureSize: 用于查找图片渐变的索贝尔内核的大小。
    L2gradient: 是否使用L2范数计算图像梯度。"""
    

def get_contours(image):
    """获取轮廓"""
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # contours, _ 这个语法表示我们只关心轮廓列表, 而不关心层次信息。
    # def findContours()image,mode,method,contours=None,bierarchy=None,offset=None)
    """image: 输入图像
    mode: 轮廓检索模式, 有四种: cv2.RETR_EXTERNAL, cv2.RETR_LIST, cv2.RETR_CCOMP, cv2.RETR_TREE
    method: 轮廓近似方法, 有四种: cv2.CHAIN_APPROX_NONE, cv2.CHAIN_APPROX_SIMPLE, cv2.CHAIN_APPROX_TC89_L1, cv2.CHAIN_APPROX_TC89_KCOS
    contours: 输出的轮廓, 可以为空, 如果不为空, 则会在这个变量中返回所有的轮廓。
    hierarchy: 输出的层次信息, 可以为空, 如果不为空, 则会在这个变量中返回每条轮廓的父子关系。
    offset: 输出的轮廓的起始点坐标, 可以为空, 如果不为空, 则会在这个变量中返回每条轮廓的起始点坐标。"""
    return contours

image_raw = cv2.imread('pythonproject/request/selenium/PixPin_2024-04-17_12-08-45.png')
image_height, image_width, _ = image_raw.shape
image_gaussian_blur = get_gaussian_blur_image(image_raw)
image_canny = get_canny_image(image_gaussian_blur)
contours = get_contours(image_canny)

def get_contour_area_threhold(image_width, image_height):
    contour_area_min=(image_width * 0.15) * (image_height * 0.25) * 0.8
    contour_area_max=(image_width * 0.15) * (image_height * 0.25) * 1.2
    return contour_area_min, contour_area_max

def get_arc_lenth_threhold(image_width, image_height):
    arc_lenth_min = ((image_width * 0.15)) + ((image_height * 0.25)) * 2 * 0.8
    arc_lenth_max = ((image_width * 0.15)) + ((image_height * 0.25)) * 2 * 1.2
    return arc_lenth_min, arc_lenth_max

def get_offset_threhold(image_width):
    offset_min = image_width * 0.2
    offset_max = image_width * 0.85
    return offset_min, offset_max

contour_area_min, contour_area_max = get_contour_area_threhold(image_width,image_height)
arc_length_min,arc_length_max = get_arc_lenth_threhold(image_width, image_height)
offset_min, offset_max = get_offset_threhold(image_width)
offset = None
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    if contour_area_min < cv2.contourArea(contour) < contour_area_max and arc_length_min < cv2.arclength(contour, True) < arc_length_max and offset_min < x < offset_max:
        cv2.rectang1e(image_raw, (x, y),(x + w, y + h), (0, 0, 255), 2)
        offset = x
cv2.imwrite('image_label.png',image_raw)
print('offset', offset)