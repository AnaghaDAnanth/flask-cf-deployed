import os
from flask import Flask, render_template, request
import nltk
# from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer
import joblib
import re
app = Flask(__name__)

def configure_routes(app):

    @app.route('/')
    def hello():
        return render_template('index.html')

    @app.route('/hello/<name>')
    def hello_name(name):
        # Load current count
        f = open("count.txt", "r")
        count = int(f.read())
        f.close()
        # Increment the count
        count += 1
        # Overwrite the count
        f = open("count.txt", "w")
        f.write(str(count))
        f.close()

        return render_template('hello.html', name=name, count=count)

    @app.route('/sentimentAnalysis', methods=['GET', 'POST'])
    def trying():
        if request.method=="POST":
                print("POST")
                name  = request.form["name"]
                review = request.form["review"]
                #name = request.values.get.POST["name"]
                #review = request.values.get.POST["review"]      
                print(name)
                op = predict_result(review)
                #op =0
                
                return render_template('home.html',name=name ,review=review ,op=op ,h=1)
        else:
                #return render(req,'home.html',{'h':h,'reviews':reviews ,'ops':ops ,'reviews':reviews} )
                
                # logger.info("page hit")
                return render_template('home.html',h=0)
            #return render_template('home.html')

    def predict_result(text):
        nltk.download('stopwords')
        from nltk.corpus import stopwords
        stopwrds = stopwords.words('english')

        to_be_removed =['not' ,'no' ,'nor' ,"wasn't" ,"wouldn't","weren't","doesn't" ,"didn't" ,"haven't" ]
        for w in to_be_removed:
                stopwrds.remove(w)
        ps2 = PorterStemmer()
        new_review = re.sub('[^a-zA-Z]' ," " ,text)
        new_review = new_review.lower()
        new_review = new_review.split()
        new_review = [ps2.stem(x) for x in new_review if not x in set(stopwrds)]
        new_review = " ".join(new_review)
        #print(new_review)
        new_corpus =[new_review]


        cvmodel = joblib.load('MyModel/cv_model')

        corpus2 =cvmodel.transform(new_corpus).toarray()
        svmModel = joblib.load('MyModel/svm_model')
        if svmModel.predict(corpus2)==0:
            print('negtive')
            return 0

        else:
            print('positive')
            return 1
