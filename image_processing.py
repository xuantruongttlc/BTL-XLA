from PIL import Image
import cv2
import numpy as np

def negative_transform(Img):
    negative_transform = 255 - Img
    return negative_transform

def thresholding_image(img):
    ret, binary_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    return binary_img

def log_transform(image):
    c = 255 / (np.log(1 + np.max(image)))
    logarithmic_image = c * np.log1p(image)
    logarithmic_image = np.array(logarithmic_image, dtype=np.uint8)
    return logarithmic_image

def histogram_equalizing(img):
        # Chuyển đổi ảnh thành ảnh grayscale nếu nó không phải là ảnh đen trắng
        if len(img.shape) > 2:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Chuyển đổi kiểu dữ liệu của ảnh thành uint8 nếu nó không phải là kiểu uint8
        if img.dtype != np.uint8:
            img = img.astype(np.uint8)

        # Kiểm tra xem ảnh có phải là ảnh grayscale không
        assert len(img.shape) == 2, "Chỉ hỗ trợ ảnh grayscale"

        # Áp dụng equalizeHist
        img_hist = cv2.equalizeHist(img)
        return img_hist

def average_filter(img_raw):
    img = cv2.cvtColor(img_raw, cv2.COLOR_BGR2GRAY)
    m, n = img.shape

    mask = np.ones([3, 3], dtype=int)
    mask = mask / 9
    img_new = np.zeros([m, n])

    for i in range(1, m - 1):
        for j in range(1, n - 1):
            temp = img[i - 1, j - 1] * mask[0, 0] + img[i - 1, j] * mask[0, 1] + img[i - 1, j + 1] * mask[0, 2] + img[
                i, j - 1] * mask[1, 0] + img[i, j] * mask[1, 1] + img[i, j + 1] * mask[1, 2] + img[i + 1, j - 1] * mask[
                       2, 0] + img[i + 1, j] * mask[2, 1] + img[i + 1, j + 1] * mask[2, 2]

            img_new[i, j] = temp

    img_new = img_new.astype(np.uint8)
    return img_new


def weighted_averaging(img_raw):
    kernel = (
            np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]], dtype=np.float32) / 16
    )
    processedImage = cv2.filter2D(img_raw, -1, kernel)
    return processedImage


def median_filter(img_raw):
    img = cv2.cvtColor(img_raw, cv2.COLOR_BGR2GRAY)
    m, n = img.shape

    img_new1 = np.zeros([m, n])
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            temp = [img[i - 1, j - 1],
                    img[i - 1, j],
                    img[i - 1, j + 1],
                    img[i, j - 1],
                    img[i, j],
                    img[i, j + 1],
                    img[i + 1, j - 1],
                    img[i + 1, j],
                    img[i + 1, j + 1]]

            temp = sorted(temp)
            img_new1[i, j] = temp[4]

    img_new1 = img_new1.astype(np.uint8)
    return img_new1

def laplacian_operator(img_raw):
    gray_image = cv2.cvtColor(img_raw, cv2.COLOR_BGR2GRAY)
    laplace = cv2.Laplacian(gray_image, cv2.CV_64F)
    laplace = laplace.astype(np.uint8)

    return laplace
def canny_operator(img_raw):
    img = cv2.cvtColor(img_raw, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img, (3, 3), 0)

    canny = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)
    canny = canny.astype(np.uint8)

    return canny

def otsu_algorithm(img_raw):
    if len(img_raw.shape) == 3:
        img_gray = cv2.cvtColor(img_raw, cv2.COLOR_BGR2GRAY)
    else:
        img_gray = img_raw

        # Áp dụng thuật toán OTSU
    _, threshold_image = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Chuyển đổi ảnh xám thành ảnh màu để hiển thị
    threshold_image_color = cv2.cvtColor(threshold_image, cv2.COLOR_GRAY2BGR)

    return threshold_image_color
