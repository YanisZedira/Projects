from calendar import month_name
import pandas as pd
import numpy
import matplotlib.pyplot as plt

class DataPreparation:
    def __init__(self, csv_path):
        self.dataset_df = pd.read_csv(csv_path)
        self.dataset_df["Years"] = pd.to_datetime(self.dataset_df["Years"])
        number_of_rows = len(self.dataset_df)
        self.dataset_df["index_mesure"] = numpy.arange(0, number_of_rows, 1)
        
        self.dataset_df["month_names"] = self.dataset_df["Years"].dt.strftime("%B")
        hot_encoding = pd.get_dummies(self.dataset_df["month_names"], dtype=int)
        self.dataset_df = pd.concat([self.dataset_df, hot_encoding], axis=1)
        
        """pour afficher seulement jusqu'en 2007.Retirer les commentaires et le texte
        
        self.dataset_df = self.dataset_df[self.dataset_df["Years"].dt.year <= 2006]
        """
        

        print(self.dataset_df)
        self.prepare_data()
        
    def prepare_data(self):
        number_of_rows = len(self.dataset_df)
        
        dataset_train_df = self.dataset_df.iloc[:int(number_of_rows * 0.75)]
        dataset_test_df = self.dataset_df.iloc[int(number_of_rows * 0.75):]

        month_columns = [col for col in self.dataset_df.columns if col in month_name[1:]]
        self.x_train = dataset_train_df[['index_mesure'] + month_columns].values
        self.y_train = dataset_train_df[['Sales']].values
        self.x_test = dataset_test_df[['index_mesure'] + month_columns].values
        self.y_test = dataset_test_df[['Sales']].values

    def show_graph(self):
        plt.figure(figsize=(15, 6))
        plt.plot(self.dataset_df["Years"], self.dataset_df["Sales"], "b.--", label='Time series data')
        plt.xlabel('')
        plt.ylabel('')
        plt.title('Time Series Data')
        plt.legend()
        plt.show()