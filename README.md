## Cilt kanseri tespiti

Cilt kanseri tespiti için YOLOv8'in Colab ortamında hazırlanması ve eğitilmesi için kullandığım kodlar ve eğitim ayarlarım:
(her model için ayrı data klasörü kullanılmıştır diğer ayarlar aynıdır)

Veri seti olarak Pedro Hispano Hastanesi PH2 veri seti kullanılmıştır.
Veri seti içerisindeki cilt lezyonu görüntüleri makesense ortamında etiketlenerek coco formatında txt dosyaları ve bu etiketlere ait görüntüler elde edilmiştir. Elde edilen bu etiketler ve görüntüler Data Augmentation kütüphanesi kullanılarak çoğaltılmıştır , veri seti çoğaltıldıktan sonra  colab ortamında Yolov8l modeli kullanılarak ,   cilt kanserinde kullanılan veri seti içerisinde sınıflar  için eğitilmiştir. Daha sonra eğitilen modeller PYQT5 kütüphanesi kullanılarak oluşturulan Gui üzerinde test edilmiştir.

## EĞİTİM GÖRÜNTÜLERİ:

![image](https://github.com/user-attachments/assets/ccfb5bd8-e747-41ce-ac41-d9bfebba418f)
![image](https://github.com/user-attachments/assets/09ad22df-15c9-418d-9095-b61d6c6a45aa)
![image](https://github.com/user-attachments/assets/38147ee0-cfda-4073-ad8b-7afd8b42e228)
![image](https://github.com/user-attachments/assets/21e53a2b-ff5d-4c65-b751-4424f94c66fc)
![image](https://github.com/user-attachments/assets/78958f2b-7c99-460e-bb00-6af40a273161)
![image](https://github.com/user-attachments/assets/85fc2845-c6fa-41cd-9ab4-459cd6bf6783)
![image](https://github.com/user-attachments/assets/75d6277e-de9c-4c17-b707-0cbccc7645db)

## KARAR DESTEK ARAYÜZÜ:

![image](https://github.com/user-attachments/assets/73ed5dfd-cf32-49d9-bc41-b6db62c8f512)
![image](https://github.com/user-attachments/assets/e9a166e3-5585-4f7c-b064-d39fcdde36b8)
![image](https://github.com/user-attachments/assets/2ef9b900-c003-4248-9c33-373615177d28)







