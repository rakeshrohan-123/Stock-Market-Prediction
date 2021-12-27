#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, render_template, request
import numpy as np
from keras.models import load_model

app = Flask(__name__)
model1 = load_model('my_model.h5')

@app.route('/')
def home():
    return render_template("stock.html")

@app.route('/predict', methods=['POST'])
def results():
    stk1 = request.form['stk1']
    stk2= request.form['stk2']
    stk3= request.form['stk3']
    sk1=float(stk1)
    sk2=float(stk2)
    sk3=float(stk3)
    k= model1.predict(np.array([[[sk1],[sk2],[sk3]]]))
    pred=k[0][0]
    print(pred)
    0
    
    
    
    return render_template("stock.html", result = pred)


if __name__ == '__main__':
    app.run()

