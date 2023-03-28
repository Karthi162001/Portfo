from flask import Flask, render_template, request , redirect, url_for
from datetime import datetime
import csv
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
app = Flask(__name__)

print(__name__)
print(app)
@app.route("/index.html")
def my_home():
    return render_template("index.html")

@app.route("/<string:page_name>")    
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open("database.txt",mode ='a') as database:
        name = data["name"]
        email = data["email"]
        message = data["message"]
        file = database.write(f"\n{dt_string} - name :{name}, email: {email}, message : {message}" )

def write_to_csv(data):
    with open("database.csv",mode ='a') as database2:
        name = data["name"]
        email = data["email"]
        message = data["message"]
        csv_writter = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writter.writerow([name,email,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        #write_to_file(data)
        write_to_csv(data)        
        return redirect('/thankyou.html')
    else:
        return "Something went wrong"

