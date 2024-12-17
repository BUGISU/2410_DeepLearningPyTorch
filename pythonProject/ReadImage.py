from PIL import Image
import numpy as np

image_path ="CapturedImage.png"
image = Image.open(image_path)
image_data = np.array(image)

print(f"Image shape ; {image_data.shape}")

import cv2

# 이미지 로드
image = cv2.imread("ReceivedImage.png")

# 흑백으로 변환
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 처리 결과 저장
cv2.imwrite("ProcessedGrayImage.png", gray_image)
