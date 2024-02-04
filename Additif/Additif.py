from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as numpy

class AdditifModel:
    def __init__(self, data_preparation_object):
        self.data_preparation_object = data_preparation_object
        self.model = LinearRegression()

        self.model.fit(data_preparation_object.x_train, data_preparation_object.y_train)

        y_train_predicted = self.model.predict(data_preparation_object.x_train)
        mean_train_absolute_error = numpy.mean(numpy.abs(y_train_predicted - data_preparation_object.y_train))
        print(f"sur le jeu de train : {mean_train_absolute_error=:.2f}")

        y_test_predicted = self.model.predict(data_preparation_object.x_test)
        mean_test_absolute_error = numpy.mean(numpy.abs(y_test_predicted - data_preparation_object.y_test))
        print(f"sur le jeu de test : {mean_test_absolute_error=:.2f}")

        self.show_model_predictions(y_train_predicted, y_test_predicted)

   

    def show_model_predictions(self, y_train_predicted=None, y_test_predicted=None):
        plt.figure(figsize=(15, 6))

        #TSD
        plt.plot(self.data_preparation_object.dataset_df["Years"].iloc[:int(len(self.data_preparation_object.dataset_df)*0.75)], self.data_preparation_object.dataset_df["Sales"].iloc[:int(len(self.data_preparation_object.dataset_df)*0.75)], color="blue", linestyle="dotted", marker="o", markersize=5 ,label='Time series data')

        #FAM
        plt.plot(self.data_preparation_object.dataset_df["Years"].iloc[:int(len(self.data_preparation_object.dataset_df)*0.75)], y_train_predicted, "c-", label='Fitted additive model')

       #TFD
        plt.plot(self.data_preparation_object.dataset_df["Years"].iloc[int(len(self.data_preparation_object.dataset_df)*0.75):], self.data_preparation_object.dataset_df["Sales"].iloc[int(len(self.data_preparation_object.dataset_df)*0.75):],color="gold", linestyle="dotted", marker="o", markersize=5, label='True future data') 
        
        #FAMD
        plt.plot(self.data_preparation_object.dataset_df["Years"].iloc[int(len(self.data_preparation_object.dataset_df)*0.75):], y_test_predicted, "r-", label='Forecasted additive model data')

        

        #interval de confiance de 95%
        minc = y_test_predicted[:, 0] + 1.96 * numpy.std(y_test_predicted[:, 0])
        maxc = y_test_predicted[:, 0] - 1.96 * numpy.std(y_test_predicted[:, 0])

        plt.fill_between(self.data_preparation_object.dataset_df["Years"].iloc[int(len(self.data_preparation_object.dataset_df)*0.75):], maxc, minc, color="lightgray", alpha=0.5, label="95% Confidence Interval")

        plt.xlabel('')
        plt.ylabel('')
        plt.title('')
        plt.legend()
        plt.show()