## Skin Cancer Detection

The YOLOv8 model has been prepared and trained in the Colab environment for skin cancer detection. (Cilt kanseri tespiti için YOLOv8'in Colab ortamında hazırlanması ve eğitilmesi.)

The Pedro Hispano Hospital PH2 dataset was used as the dataset. (Veri seti olarak Pedro Hispano Hastanesi PH2 veri seti kullanılmıştır.)

The skin lesion images in the dataset were labeled using the makesense environment, resulting in coco format text files and corresponding images. (Veri seti içerisindeki cilt lezyonu görüntüleri makesense ortamında etiketlenerek coco formatında txt dosyaları ve bu etiketlere ait görüntüler elde edilmiştir.)

The obtained labels and images were augmented using the Data Augmentation library. (Elde edilen bu etiketler ve görüntüler Data Augmentation kütüphanesi kullanılarak çoğaltılmıştır.)

After augmenting the dataset, the YOLOv8l model was used in the Colab environment to train on the dataset used for skin cancer. (Veri seti çoğaltıldıktan sonra colab ortamında Yolov8l modeli kullanılarak, cilt kanserinde kullanılan veri seti içerisinde sınıflar için eğitilmiştir.)

Subsequently, the trained models were tested on a GUI created using the PyQt5 library. (Daha sonra eğitilen modeller PYQT5 kütüphanesi kullanılarak oluşturulan GUI üzerinde test edilmiştir.)

## TRAINING IMAGES (EĞİTİM GÖRÜNTÜLERİ):

![image](https://github.com/user-attachments/assets/ccfb5bd8-e747-41ce-ac41-d9bfebba418f)
![image](https://github.com/user-attachments/assets/09ad22df-15c9-418d-9095-b61d6c6a45aa)
![image](https://github.com/user-attachments/assets/38147ee0-cfda-4073-ad8b-7afd8b42e228)
![image](https://github.com/user-attachments/assets/21e53a2b-ff5d-4c65-b751-4424f94c66fc)
![image](https://github.com/user-attachments/assets/78958f2b-7c99-460e-bb00-6af40a273161)
![image](https://github.com/user-attachments/assets/85fc2845-c6fa-41cd-9ab4-459cd6bf6783)
![image](https://github.com/user-attachments/assets/75d6277e-de9c-4c17-b707-0cbccc7645db)

## DECISION SUPPORT INTERFACE(KARAR DESTEK ARAYÜZÜ):

![image](https://github.com/user-attachments/assets/73ed5dfd-cf32-49d9-bc41-b6db62c8f512)
![image](https://github.com/user-attachments/assets/e9a166e3-5585-4f7c-b064-d39fcdde36b8)
![image](https://github.com/user-attachments/assets/2ef9b900-c003-4248-9c33-373615177d28)

## FINDINGS AND CONCLUSION (ÇIKARILAN BULGULAR VE SONUÇ):
In this study, it has been demonstrated that skin cancer detection can be performed using the YOLOv8 deep learning algorithm, and a user interface can be created to support physicians, achieving good results based on the accuracy rates obtained. (Bu çalışmada YOLOv8 derin öğrenme algoritmasıyla cilt kanseri tespiti yapılabileceği ve hekimlere destek olacak şekilde bir arayüz oluşturulabileceği konusunda alınan doğruluk oranları sonucunda iyi bir sonuç alınmıştır.)

In future studies, developments can be made to train segmentation models to track parameters such as diameter, width, or size of skin lesions and to monitor them over certain periods. (Devam edilecek çalışmalarda cilt lezyonunun segmentasyon modelleriyle çapı, eni veya büyüklüğü gibi parametreleri takip etmek adına eğitim yapılıp belli süreçlerde takip edilebilmesi adına geliştirmeler yapılabilir.)







