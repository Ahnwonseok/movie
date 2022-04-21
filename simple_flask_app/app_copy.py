from flask import Flask, render_template, request
import pandas as pd
import pickle

with open("model.pkl","rb") as fr:
   boosting = pickle.load(fr)
with open("encoder.pkl","rb") as fr:
   encoder = pickle.load(fr)

app = Flask(__name__)

@app.route('/')
def student():
   return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      print(result)
      result=result.to_dict(flat=False)


   student_card = pd.DataFrame({'감독':result['감독'],
                              '제작사':result['제작사'],
                              '수입사':result['수입사'],
                              '배급사':result['배급사'],
                              '개봉일':[int(result['개봉일'][0])],
                              '국적':result['국적'],
                              '스크린수':[int(result['스크린수'][0])],
                              '장르':result['장르'],
                              '등급':result['등급']})
                            
   X_tests_encoded = encoder.transform(student_card)  

   result2=boosting.predict(X_tests_encoded)      
                
   return render_template("default.html",result = str(result2[0]))

if __name__ == '__main__':
   app.run(debug = True)
