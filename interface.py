from utils import Diabetes_pediction
from flask import Flask, jsonify, render_template, request
import config

app = Flask(__name__)

##################################################################################
 ################################# Base API #####################################
##################################################################################

@app.route('/')
def Perdiction_model():
    print('Welcome to Diabetes Prediction Model')
    return render_template('index.html')

##################################################################################
 ################################# Model API #####################################
##################################################################################

@app.route('/predicted_diabetes',methods = ['POST','GET'])
def Get_Diabetes_Prediction():
    if request.method == 'POST':
        print('We are using POST Method')
        data = request.form
        Pregnancies = data['Pregnancies']
        Glucose = data['Glucose']
        BloodPressure = data['BloodPressure']
        SkinThickness = data['SkinThickness']
        Insulin = data['Insulin']
        BMI = data['BMI']
        DiabetesPedigreeFunction = data['DiabetesPedigreeFunction']
        Age = data['Age']
        print(f'Pregnancies >> {Pregnancies}, Glucose >> {Glucose}, BloodPressure >> {BloodPressure}, SkinThickness >> {SkinThickness}, Insulin >> {Insulin}, BMI >> {BMI},DiabetesPedigreeFunction >> {DiabetesPedigreeFunction},Age >> {Age} ')
        med_ins = Diabetes_pediction(Pregnancies,Glucose, BloodPressure, SkinThickness,Insulin, BMI,DiabetesPedigreeFunction,Age)
        charges = med_ins.get_predicted_diabetis()
        #return render_template('result.html', prediction=my_prediction)
        return render_template('result.html', charges=charges)

    else:
        print('We are in GET Method')
        

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = config.PORT_NUMBER, debug= True)
