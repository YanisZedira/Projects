from data_preparation import DataPreparation
from Additif import AdditifModel

csv_path = r"C:\Users\pc\Desktop\TP HETIC\MathsIA\Additif\vente_maillots_de_bain(1).csv"
data_preparation_object = DataPreparation(csv_path)
regression_object = AdditifModel(data_preparation_object)
regression_object.show_model_predictions()



#YANIS, AYMEN DIA1