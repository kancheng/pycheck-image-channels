# pycheck-image-channels
Check the number of image channels

## Demo

```
(yolov8) koala@DESKTOP:/mnt/e/image-channels$ python3 main.py
INFO. IMG.: carvana_img.jpg; Channels :  3 ; Details :  (<PIL.Image.Image image mode=L size=1918x1280 at 0x7FDE9BF37FA0>, <PIL.Image.Image image mode=L size=1918x1280 at 0x7FDE9BF37F70>, <PIL.Image.Image image mode=L size=1918x1280 at 0x7FDE22118760>)
INFO. IMG.: carvana_mask.gif; Channels :  1 ; Details :  (<PIL.Image.Image image mode=P size=1918x1280 at 0x7FDE9BF373D0>,)
INFO. IMG.: coco128.jpg; Channels :  3 ; Details :  (<PIL.Image.Image image mode=L size=640x480 at 0x7FDE9BF37FD0>, <PIL.Image.Image image mode=L size=640x480 at 0x7FDE9BF37FA0>, <PIL.Image.Image image mode=L size=640x480 at 0x7FDE9BF375B0>)
INFO. IMG.: mvtec_ad_img1.png; Channels :  3 ; Details :  (<PIL.Image.Image image mode=L size=900x900 at 0x7FDE9BF37F70>, <PIL.Image.Image image mode=L size=900x900 at 0x7FDE221187C0>, <PIL.Image.Image image mode=L size=900x900 at 0x7FDE221189A0>)
INFO. IMG.: mvtec_ad_img2.png; Channels :  3 ; Details :  (<PIL.Image.Image image mode=L size=900x900 at 0x7FDE9BF37F70>, <PIL.Image.Image image mode=L size=900x900 at 0x7FDE221187C0>, <PIL.Image.Image image mode=L size=900x900 at 0x7FDE22118880>)
INFO. IMG.: mvtec_ad_mask.png; Channels :  1 ; Details :  (<PIL.Image.Image image mode=L size=900x900 at 0x7FDE9BF37F70>,)
INFO. IMG.: salt_img.png; Channels :  4 ; Details :  (<PIL.Image.Image image mode=L size=101x101 at 0x7FDE9BF37FA0>, <PIL.Image.Image image mode=L size=101x101 at 0x7FDE9BF375B0>, <PIL.Image.Image image mode=L size=101x101 at 0x7FDE22118790>, <PIL.Image.Image image mode=L size=101x101 at 0x7FDE22118A60>)
INFO. IMG.: salt_mask.png; Channels :  1 ; Details :  (<PIL.Image.Image image mode=I;16 size=101x101 at 0x7FDE9BF375B0>,)
INFO. IMG.: brats_img_flair.jpg; Channels :  1 ; Details :  (<PIL.Image.Image image mode=L size=240x240 at 0x7FDE9BF37FA0>,)
INFO. IMG.: brats_mask_seg.jpg; Channels :  1 ; Details :  (<PIL.Image.Image image mode=L size=240x240 at 0x7FDE9BF375B0>,)
INFO. IMG.: brats_img_t1.jpg; Channels :  1 ; Details :  (<PIL.Image.Image image mode=L size=240x240 at 0x7FDE9BF37FA0>,)
INFO. IMG.: brats_img_t1ce.jpg; Channels :  1 ; Details :  (<PIL.Image.Image image mode=L size=240x240 at 0x7FDE9BF375B0>,)
INFO. IMG.: brats_img_t2.jpg; Channels :  1 ; Details :  (<PIL.Image.Image image mode=L size=240x240 at 0x7FDE9BF37FA0>,)
```

## Datasets

- https://www.kaggle.com/competitions/carvana-image-masking-challenge/

- https://www.kaggle.com/competitions/tgs-salt-identification-challenge/

- https://www.mvtec.com/company/research/datasets/mvtec-ad

- https://www.kaggle.com/code/miladlink/brats-nifti-to-jpg/notebook

## Details

U-Net 是一種常用於圖像分割的卷積神經網絡架構，特別適合於醫療影像處理。它的設計有兩個主要部分：編碼器（下採樣）和解碼器（上採樣）。

### 進去的通道（輸入層）
進入 U-Net 的圖像通常是多通道的，例如：
- 彩色圖像通常有 3 個通道（R、G、B）。
- 如果是灰階圖像，則只有 1 個通道。

在這一層，輸入的通道數決定了網絡能夠處理的圖像特徵。例如，如果輸入是一張 RGB 圖像，則第一層卷積會接收 3 個通道的數據。

### 出來的通道（輸出層）
U-Net 的輸出通常是每個像素的類別標籤。這裡的通道數量通常等於你想要分割的類別數。例如：
- 對於二分類問題（如前景和背景），輸出可能只有 1 個通道，並使用 sigmoid 激活函數。
- 對於多分類問題（如分割多種組織），則輸出可能有多個通道，與類別數相同，通常使用 softmax 激活函數。

### 總結
- **進去的通道**：通常代表圖像的顏色通道數（如 RGB 的 3 個通道）。
- **出來的通道**：代表需要分割的類別數，通常是對應每個類別的預測結果。

這樣的設計使得 U-Net 能夠有效地學習和預測每個像素的類別，達到高效的圖像分割效果。
