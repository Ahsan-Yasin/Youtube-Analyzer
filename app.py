from flask import Flask, render_template, request, session
from model import UseUrl, getSentiments, inference

app = Flask(__name__)
app.secret_key = '1122'  
 
@app.route('/', methods=['GET', 'POST'])
def index(): 
    answer='Your link analysis will appear after you enter the link'
    if request.method == 'POST':
        user_input = request.form['userInput']
        print("Your input:")
        print(user_input)

        if user_input.startswith("https://"):
            # Process YouTube URL
            UseUrl(user_input)
            total, positive, negative = getSentiments()
            print(total, positive, negative)

            session['positive'] = positive
            session['negative'] = negative
        else:
            # Just run inference; don't touch session values
            print("This is not a URL")
            answer= inference(user_input)

    # Read values from session if they exist, else default to 0
    positive = session.get('positive', 0)
    negative = session.get('negative', 0) 

    return render_template("index.html", positive=positive, negative=negative,answer=answer)

if __name__ == '__main__':
    app.run(debug=True)
