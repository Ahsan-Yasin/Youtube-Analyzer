from flask import Flask, render_template
from model import UseUrl , getSentiments , inference  

app=Flask(__name__)  
@app.route('/',methods=['GET','POST'])  
def index():
   
    return render_template("index.html") 

if __name__ == '__main__':
    app.run(debug=True) 