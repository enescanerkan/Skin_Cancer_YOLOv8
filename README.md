## Cilt kanseri tespiti

Cilt kanseri tespiti için YOLOv8'in Colab ortamında hazırlanması ve eğitilmesi için kullandığım kodlar ve eğitim ayarlarım:



from google.colab import drive
drive.mount("/content/drive")


%pwd



%cd /content/drive/MyDrive/yolov8/1_object_detection



!unzip data/Asymetry.zip -d ./data



%pip install ultralytics

import ultralytics
ultralytics.checks()


!yolo detect train data=data/config.yaml model=yolov8l.pt epochs=200 imgsz=640 workers=8 batch=8 device=0 name=asymetry_detection


!yolo detect predict model=../best.pt source=inference save=True

[Uploa{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"gpuType":"T4","authorship_tag":"ABX9TyPGOdTRDMJo28+4zu+B6y6s"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"},"accelerator":"GPU"},"cells":[{"cell_type":"code","execution_count":null,"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"6OrClrrAH8jW","executionInfo":{"status":"ok","timestamp":1701790646793,"user_tz":-180,"elapsed":23514,"user":{"displayName":"enes erkan","userId":"09368155740737015131"}},"outputId":"4481de4b-c6c4-4dcc-b4da-44aaeb4b251d"},"outputs":[{"output_type":"stream","name":"stdout","text":["Mounted at /content/drive\n"]}],"source":["from google.colab import drive\n","drive.mount(\"/content/drive\")"]},{"cell_type":"code","source":["%pwd"],"metadata":{"colab":{"base_uri":"https://localhost:8080/","height":35},"id":"tgMYXutrIBxn","executionInfo":{"status":"ok","timestamp":1701782259604,"user_tz":-180,"elapsed":613,"user":{"displayName":"enes erkan","userId":"09368155740737015131"}},"outputId":"6cfc84d3-477c-4296-b7c5-0f6c04dc699f"},"execution_count":null,"outputs":[{"output_type":"execute_result","data":{"text/plain":["'/content'"],"application/vnd.google.colaboratory.intrinsic+json":{"type":"string"}},"metadata":{},"execution_count":2}]},{"cell_type":"code","source":["%cd /content/drive/MyDrive/YOLOv8/1_object_detection"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"Vo7ocGs1ICL9","executionInfo":{"status":"ok","timestamp":1701782261543,"user_tz":-180,"elapsed":292,"user":{"displayName":"enes erkan","userId":"09368155740737015131"}},"outputId":"53d12db5-eceb-4d58-a12f-4d77c3538bcf"},"execution_count":null,"outputs":[{"output_type":"stream","name":"stdout","text":["/content/drive/MyDrive/YOLOv8/1_object_detection\n"]}]},{"cell_type":"code","source":["%pip install ultralytics\n","\n","import ultralytics\n","ultralytics.checks()"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"RZbiIMP4IGE3","executionInfo":{"status":"ok","timestamp":1701782286638,"user_tz":-180,"elapsed":17631,"user":{"displayName":"enes erkan","userId":"09368155740737015131"}},"outputId":"b3da5c85-a7dc-4efb-adbf-5c406ce3aa7b"},"execution_count":null,"outputs":[{"output_type":"stream","name":"stdout","text":["Ultralytics YOLOv8.0.222 🚀 Python-3.10.12 torch-2.1.0+cu118 CPU (Intel Xeon 2.20GHz)\n","Setup complete ✅ (2 CPUs, 12.7 GB RAM, 26.9/107.7 GB disk)\n"]}]},{"cell_type":"code","source":["!unzip data/Asymetry.zip -d ./data"],"metadata":{"id":"n7vRAxS9IMvu"},"execution_count":null,"outputs":[]},{"cell_type":"code","source":["!yolo detect train data=data/config.yaml model=yolov8l.pt epochs=200 imgsz=640 workers=8 batch=8 device=0 name=yolov8_Asymetry_detection"],"metadata":{"id":"Ea-LaJgcIOL0"},"execution_count":null,"outputs":[]}]}ding object_detection.ipynb…]()



