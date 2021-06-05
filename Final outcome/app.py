from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
import os
import pickle
import numpy as np


# from flask_pymongo import PyMongo
# import scrape_mars

app = Flask(__name__)
picfolder=os.path.join('static','images')

app.config['UPLOAD_FOLDER']= picfolder

# # Use flask_pymongo to set up mongo connection
# mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


# # Or set inline
# # mongo = PyMongo(app, uri="mongodb://localhost:27017/phone_app")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/index.html")
def model():
    pic1= os.path.join(app.config['UPLOAD_FOLDER'],'features.png')
    pic2= os.path.join(app.config['UPLOAD_FOLDER'],'heatmap.png')
    pic3= os.path.join(app.config['UPLOAD_FOLDER'],'tree.png')
    pic4= os.path.join(app.config['UPLOAD_FOLDER'],'loanzz.jpeg')
    pic5= os.path.join(app.config['UPLOAD_FOLDER'],'apply.png')
    pic6= os.path.join(app.config['UPLOAD_FOLDER'],'uborrow.png')
    


    return render_template('index.html', usr_image= pic1, usr_img= pic2, usr_inge=pic3, imag= pic4, imag1= pic5, imag2= pic6)


@app.route("/graphs.html")
def graphs():
    pica= os.path.join(app.config['UPLOAD_FOLDER'],'Credit_History_graph.png')
    picb= os.path.join(app.config['UPLOAD_FOLDER'],'Dependents_graph.png')
    picc= os.path.join(app.config['UPLOAD_FOLDER'],'Education_graph.png')
    picd= os.path.join(app.config['UPLOAD_FOLDER'],'SelfEmployed_graph.png')


    return render_template('graphs.html', viz= pica, viz1= picb, viz2=picc, viz3= picd)

@app.route("/trymodel.html")
def trymodel():
    
    
    return render_template('trymodel.html')   

@app.route("/predict", methods=['POST'])
def predict():
    filename = 'finalized_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))

    # load the model from disk
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = loaded_model.predict(final_features)
    output = prediction[0]

    return render_template("trymodel.html", prediction_text='Your predicted answer is {}'.format(output))
    


if __name__ == "__main__":
    app.run(debug=True)