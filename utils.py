import pickle
import json
# import config
import numpy as np

class Diabetes_pediction():

    def __init__(self,Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,
       BMI,DiabetesPedigreeFunction,Age):

       self.Pregnancies = Pregnancies
       self.Glucose = Glucose
       self.BloodPressure = BloodPressure
       self.SkinThickness = SkinThickness
       self.Insulin = Insulin
       self.BMI = BMI
       self.DiabetesPedigreeFunction = DiabetesPedigreeFunction
       self.Age = Age
        

    def load_model(self):
        with open(r'E:\Velocity\Diabetes_prediction\Project_app\Logistic_model.pkl', 'rb') as f:
            self.model = pickle.load(f)
        
        with open(r'E:\Velocity\Diabetes_prediction\Project_app\project_data.json', 'r') as f:
            self.json_data = json.load(f)

    def get_predicted_diabetis(self):
        self.load_model()

        test_array = np.zeros(len(self.json_data['columns']))
        test_array[0] = self.Pregnancies
        test_array[1] = self.Glucose
        test_array[2] = self.BloodPressure
        test_array[3] = self.SkinThickness
        test_array[4] = self.Insulin
        test_array[5] = self.BMI
        test_array[6] = self.DiabetesPedigreeFunction
        test_array[7] = self.Age

        test_array

        print('Test Array :', test_array)
        predicted_diabetes = np.around(self.model.predict([test_array]))
        #print('Medical Insurance charges are : RS.',predicted_charges)
        return predicted_diabetes
if __name__ == '__main__':

    Pregnancies = 5
    Glucose = 145
    BloodPressure = 74
    SkinThickness = 30
    Insulin = 0
    BMI = 31
    DiabetesPedigreeFunction = 0.65
    Age = 48
    med_ins = Diabetes_pediction(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,
       BMI,DiabetesPedigreeFunction,Age)
    med_ins.get_predicted_diabetis()