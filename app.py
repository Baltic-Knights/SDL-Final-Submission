from flask import *

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')



@app.route('/covid_map')
def covid():
    return render_template('covid_map.html')



@app.route('/predict', methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        #f = request.files.get('file')
        f = request.files['file']
        fname=f.filename
        fname = fname.split(".")
        name=fname[0]

        return render_template('index.html', pred1="Condition of given X-ray Scan : {} ".format(name))
        #return render_template('index.html', pred1="Success")



if __name__ == "__main__":
    app.run(debug = True)
