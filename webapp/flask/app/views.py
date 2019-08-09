from app import app
from flask import render_template,request
from app import db_api #database api

@app.route("/")
def index():
    return render_template("view/startup.html")

@app.route('/db',methods = ['POST', 'GET'])
def mydb():
    mobj = db_api.MyMongo() #creating db api object
    # mobj.myclient = pymongo.MongoClient()
    if request.method == 'POST':
        print(request.form)
        ijson = {}
        ijson['fname'] = request.form['fname']
        ijson['lname'] = request.form['lname']
        print(ijson)
        print("hio")
        return mobj.inset_to_collection(ijson)
    else:
        return mobj.get_all_documents()
    # mobj.myclient.close()
