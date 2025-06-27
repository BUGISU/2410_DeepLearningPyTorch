# 🖼️ Image Classification via Socket & CNN

본 프로젝트는 TCP 소켓 통신을 통해 이미지를 수신하고, CNN 모델을 활용하여 개/고양이 이미지를 분류하는 전체 파이프라인을 구현합니다.  
이미지 전송 → 수신 및 저장 → 전처리 → 분류 모델 학습/추론의 순서로 구성됩니다.

---

## 📁 프로젝트 구조

```

.
├── PythonServer.py           # TCP 이미지 수신 서버
├── ReadImage.py              # 수신된 이미지 전처리 (흑백 변환 등)
├── test-modelData.py         # CNN 모델 학습 (Cats vs Dogs 데이터셋)
├── test-SampleData.py        # 수신 이미지 분류 예측
├── ReceivedImage.png         # 수신된 이미지 파일 (자동 생성)
├── ProcessedGrayImage.png    # 흑백 변환된 이미지 파일 (자동 생성)
└── epoch\_001/model.h5        # 저장된 모델 파일 (자동 생성)

````

---

## 🚀 실행 흐름

```mermaid
graph TD
A[클라이언트 전송 이미지] --> B[1. PythonServer.py (수신)]
B --> C[2. ReadImage.py (흑백 저장)]
B --> D[4. test-SampleData.py (이미지 분류)]
E[3. test-modelData.py (CNN 학습)] --> D
````

---

## 🛠️ 주요 기술

* **Python 3.8+**
* `socket`, `struct`, `PIL`, `cv2`, `numpy`
* `tensorflow.keras` (CNN 모델 학습 및 예측)
* `ImageDataGenerator` (데이터 전처리 및 증강)

---

## ⚙️ 설치 및 실행

### 1. 의존성 설치

```bash
pip install pillow opencv-python tensorflow numpy
```

### 2. 서버 실행 (이미지 수신)

```bash
python PythonServer.py
```

> 클라이언트에서 이미지를 전송하면 `ReceivedImage.png`로 저장됩니다.

### 3. 이미지 전처리

```bash
python ReadImage.py
```

### 4. CNN 모델 학습 (최초 1회)

```bash
python test-modelData.py
```

> 결과 모델은 `./epoch_001/model.h5`로 저장됩니다.

### 5. 수신 이미지 분류 실행

```bash
python test-SampleData.py
```

> 출력 예:

```
이 이미지는 개(Dog)입니다.
```

---

## 📷 예시 결과

* **수신 이미지 (ReceivedImage.png)**
  ![수신 이미지](./ReceivedImage.png)

* **흑백 변환 (ProcessedGrayImage.png)**
  ![흑백 이미지](./ProcessedGrayImage.png)

---

## 📌 주의사항

* `test-modelData.py`는 인터넷에서 받은 Kaggle의 Cats vs Dogs 데이터셋을 사용합니다.
  [데이터셋 링크](https://www.microsoft.com/en-us/download/details.aspx?id=54765)
* `PythonServer.py`는 단일 연결만 처리하므로 여러 클라이언트 접속은 지원하지 않습니다.
* `test-SampleData.py` 실행 전에는 반드시 모델이 학습되어 있어야 합니다.

---

## 🧪 TODO / 개선사항

* 클라이언트 송신 코드 추가
* 다중 연결 지원 (`asyncio` 또는 `select`)
* 모델 예측 결과 시각화 GUI
* TensorBoard 학습 시각화

---



