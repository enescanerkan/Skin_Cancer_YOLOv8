import gradio as gr
import cv2
from ultralytics import YOLO

type_path = r'C:\Users\Monster\PycharmProjects\pythonProject\NORBİT\models\type.pt' # Benin türü
asymetry_path = r'C:\Users\Monster\PycharmProjects\pythonProject\NORBİT\models\asymetry.pt' # Asimetri
dots_path = r'C:\Users\Monster\PycharmProjects\pythonProject\NORBİT\models\dots.pt' # Noktalar kürecik
pigment_network_path = r'C:\Users\Monster\PycharmProjects\pythonProject\NORBİT\models\pigment_network.pt' # Pigment ağı
regression_areas_path = r'C:\Users\Monster\PycharmProjects\pythonProject\NORBİT\models\regression_areas.pt' # Regresyon alanları
streak_path = r"C:\Users\Monster\PycharmProjects\pythonProject\NORBİT\models\streak.pt" # Çizgiler
blue_whitish_veil_path = r'C:\Users\Monster\PycharmProjects\pythonProject\NORBİT\models\blue-vihitish_veil.pt' # Mavi beyaz örtü

models_list = [type_path,
               asymetry_path,
               dots_path,
               pigment_network_path,
               regression_areas_path,
               streak_path,
               blue_whitish_veil_path]

type_dict = {
    "Common Nevus": "Yaygın Ben",
    "Atypical Nevus": "Atipik Ben",
    "Melanoma": "Melanom",
    "Blue-vihitish_veil_A": "Mavi beyaz örtü yok",
    "Blue-vihitish_veil_P": "Mavi beyaz örtü var",
    "Dots_AT": "Nokta A tipik",
    "Dots_T": "Nokta tipik",
    "Dots_A": "Nokta yok",
    "Pigment_AT": "Pigment A tipik",
    "Pigment_T": "Pigment tipik",
    "Pigment_A": "Pigment yok",
    "Regression_A": "Regresyon alanı yok",
    "Regression_P": "Regresyon alanı var",
    "Streaks_A": "Çizgi yok",
    "Streaks_T": "Çizgi var",
    "Streaks_AT": "Çizgi A tipik",
    "Asymetry_0": "Asimetri yok",
    "Asymetry_2": "Asimetri var",
    "Asymetry_1": "Asimetri A tipik"
}




def load_model(model_path):
    model = YOLO(model_path)
    return model

def predict(image, model_path):
    model = load_model(model_path)
    results = model(image)
    image = results[0].plot()
    for result in results:
        if result.boxes:
            box = result.boxes[0]
            class_id = int(box.cls)
            object_name = model.names[class_id]
            if object_name in type_dict:
                object_name = type_dict[object_name]
            return object_name, image
    return "No object detected", image

demo = gr.Interface(
    fn=predict,
    inputs=[gr.Image(), gr.Dropdown(models_list, label="Model")],
    outputs=["text", "image"],
    allow_flagging="never",
    analytics_enabled=False,
)

demo.launch(debug=True)
