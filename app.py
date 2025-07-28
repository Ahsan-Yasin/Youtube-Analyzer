from flask import Flask, render_template,request
from model import UseUrl , getSentiments , inference  


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    positive=0 
    negative=0  
    if request.method == 'POST':
        user_input = request.form['userInput']
        print("Your input:")
        print(user_input)
        if user_input.startswith("https://"):
            #here is to be implemented the url funcitonality  
            UseUrl(user_input) #this will created the database  
            total,positive,negative=getSentiments() #this will return the positive and negative % 
            print(total)
            print(positive)
            print(negative) 
            
        else: 
            #here i will implement the inference funtionality 
            print("This is not a url ")
    return render_template("index.html",positive=positive,negative=negative)


if __name__ == '__main__':
    app.run(debug=True) 