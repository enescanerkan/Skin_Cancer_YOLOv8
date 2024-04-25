## Cilt kanseri tespiti

Cilt kanseri tespiti için YOLOv8'in Colab ortamında hazırlanması ve eğitilmesi için kullandığım kodlar ve eğitim ayarlarım:
(her model için ayrı data klasörü kullanılmıştır diğer ayarlar aynıdır)

Data = Pedro Hispano Hastanesi PH2 veri seti
Veri seti içerisindeki cilt lezyonu görüntüleri makesense ortamında etiketlenerek coco formatında txt dosyaları ve bu etiketlere ait görüntüler elde edilmiştir. Elde edilen bu etiketler ve görüntüler Data Augmentation kütüphanesi kullanılarak çoğaltılmıştır , veri seti çoğaltıldıktan sonra  colab ortamında Yolov8l modeli kullanılarak ,   cilt kanserinde kullanılan veri seti içerisinde sınıflar  için eğitilmiştir. Daha sonra eğitilen modeller PYQT5 kütüphanesi kullanılarak oluşturulan Gui üzerinde test edilmiştir.

## EĞİTİM GÖRÜNTÜLERİ VE ARAYÜZ:

https://github.com/enescanerkan/Tez/issues/1#issue-2263033073

