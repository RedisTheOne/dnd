from flask import Flask, jsonify, send_file, request, render_template
from flask_pymongo import MongoClient
from api.apiFunctions import getMonthlySleepDeclarations, getMonthlyNutritions, findUser, signIn, signUp, createNutrition, createSleepDeclaration, deleteNutrition, editSleepHours, updateUserInfo

app = Flask(__name__)

#DATABASE
client = MongoClient('mongodb+srv://redus:redis06122002!@cluster0-xwsm9.mongodb.net/dnd?retryWrites=true&w=majority')
db = client['dnd']

#MODELS
User = db['users']
Nutirtion = db['nutritions']
SleepDeclaration = db['sleepDeclarations']

#FRONT END STUFF
@app.route('/nasafont')
def nasaFontMethod():
    return send_file('./font/nasalization-rg.woff')

@app.route('/homebackground')
def homeBackgroundMethod():
    return send_file('./images/background.png')

@app.route('/homemidground')
def homeMidgroundMethod():
    return send_file('./images/midground.png')

@app.route('/homeforeground')
def homeForegroundMethod():
    return send_file('./images/foreground.png')

# VIEWS
#HOME
@app.route('/', methods=['GET'])
def indexViews():
    return render_template('frontpage.html')

#SIGN IN
@app.route('/signin', methods=['GET'])
def signInViews():
    return render_template('signin.html')

#SIGN IN
@app.route('/signup', methods=['GET'])
def signUpViews():
    return render_template('signup.html')


#SEND AVATAR IMAGES
@app.route('/images/send', methods=['GET'])
def sendImage():
    try:
        return send_file('./uploadedImages/' + request.args.get('image'))
    except:
        return send_file('./uploadedImages/not_found.jpg')

#USER ROUTES
@app.route('/api/users', methods=['GET'])
def indexMethod():
    return findUser(User, Nutirtion, SleepDeclaration)

@app.route('/api/users/update', methods=['POST'])
def updateMethod():
    return updateUserInfo(User)

@app.route('/api/signin', methods=['POST'])
def signInMethod():
    return signIn(User)

@app.route('/api/signup', methods=['POST'])
def signUpMethod():
    return signUp(User)

#NUTRITIONS ROUTES
@app.route('/api/add/nutrition', methods=['POST'])
def addNutritionMethod():
    return createNutrition(Nutirtion)

@app.route('/api/delete/nutrition', methods=['POST'])
def deleteNutritionMethod():
    return deleteNutrition(Nutirtion)

@app.route('/api/nutritions/monthly', methods=['GET'])
def getMonthlyNutritionsMethods():
    return getMonthlyNutritions(Nutirtion)

#SLEEP DECLARATIONS ROUTES
@app.route('/api/add/sleepdeclaration', methods=['POST'])
def addSleepMethod():
    return createSleepDeclaration(SleepDeclaration)

@app.route('/api/edit/sleep', methods=['POST'])
def editSleepHoursMethod():
    return editSleepHours(SleepDeclaration)

@app.route('/api/sleepdeclarations/monthly', methods=['GET'])
def getMonthlySleepDeclarationsMethod():
    return getMonthlySleepDeclarations(SleepDeclaration)