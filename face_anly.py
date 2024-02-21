import cv2
import numpy as np

# 分類器のパスを指定（OpenCVに含まれるhaarcascade_frontalface_default.xmlを使用）
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 顔を検出したい画像を読み込む
img = cv2.imread('20230225_220135.jpg')  # 'your_image_path.jpg'を画像のパスに置き換える

# 画像のサイズを調整するための比率を計算（ここでは画像の幅を500ピクセルにする例）
scale_percent = 500 / img.shape[1]  # 幅に対するスケール比率
width = int(img.shape[1] * scale_percent)
height = int(img.shape[0] * scale_percent)
dim = (width, height)

# 画像のリサイズ
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

# グレースケール画像に変換（顔検出の精度向上のため）
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

# 顔を検出
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# 検出された顔の周囲に矩形を描画
for (x, y, w, h) in faces:
    cv2.rectangle(resized, (x, y), (x+w, y+h), (255, 0, 0), 2)

# 結果を表示
cv2.imshow('Face Detected', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()