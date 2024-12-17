from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

model = load_model('./epoch_001/model.h5')
image_path ="ReceivedImage.png"

# 이미지 전처리
img = image.load_img(image_path, target_size=(224, 224))  # 이미지 불러오기 및 크기 조정
img_array = image.img_to_array(img)  # 이미지를 numpy 배열로 변환
img_array = np.expand_dims(img_array, axis=0)  # 배치 차원 추가
img_array /= 255.0  # 정규화

# 예측 수행
prediction = model.predict(img_array)

# 결과 해석
if prediction[0][0] > 0.5:
    print("이 이미지는 개(Dog)입니다.")
else:
    print("이 이미지는 고양이(Cat)입니다.")
