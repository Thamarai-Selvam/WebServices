from flask import Flask, request, url_for, render_template
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
import uuid, csv, datetime, shutil
from tempfile import NamedTemporaryFile
from random import *  

app = Flask(__name__)
app.config.from_pyfile('config.cfg')

mail = Mail(app)

s = URLSafeTimedSerializer('Thisisasecret!')

tempData = {}
allUserData = {}
crollNum = ''
cbPassKey = '' 
cnPassKey = ''
# Mail Config-----
mail = Mail(app)  

app.config["MAIL_SERVER"]='smtp.gmail.com'  
app.config["MAIL_PORT"] = 465      
app.config["MAIL_USERNAME"] = 'meliodastheman106@gmail.com'  
app.config['MAIL_PASSWORD'] = 'meliodas1063000'  
app.config['MAIL_USE_TLS'] = False  
app.config['MAIL_USE_SSL'] = True  

mail = Mail(app)  
timedOTP = 1
#end Mail Config-----

@app.route('/register', methods=['GET', 'POST'])
def index():
    global tempData, allUserData
    if request.method == 'GET':
        # return '<form action="/" method="POST"><input name="email"><input type="submit"></form>'
        return render_template("index.html") 
    else:
        email = request.form['email']
        userName = request.form['userName']
        phNum = request.form['phNum']
        rollNum = request.form['rollNum']
        passKey = request.form['passKey']
        tempData = { 
                    'userName' : userName,
                    'phNum' : phNum,
                    'rollNum' : rollNum,
                    'eMail' : email,
                    'passKey' : passKey
                    }
        print(tempData)
        token = s.dumps(email, salt='email-confirm')

        msg = Message('Confirm Email', sender='meliodastheman106@gmail.com', recipients=[email])
        link = url_for('confirm_email', token=token, _external=True)
        msg.body = 'Your link is {}'.format(link)
        mail.send(msg)

        return '<h1>The email you entered is {}. The token is {}</h1>'.format(email, token)

@app.route('/confirm_email/<token>')
def confirm_email(token):
    try:
        email = s.loads(token, salt='email-confirm', max_age=3600)
    except SignatureExpired:
        return '<h1>The token is expired!</h1>'
    
    userdata = dict(tempData)
    print(userdata)
    rollNum = userdata["rollNum"]
    userName = userdata["userName"]
    phNum = userdata["phNum"]
    eMail = userdata["eMail"]
    passKey = userdata["passKey"]
    regOn = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    uID = str(uuid.uuid4())

    if len(rollNum) < 2 and len(userName) < 3 and len(phNum) < 9 and len(eMail) < 10 :
        return "Please submit valid data."
    else:
        for userRow in allUserData:
            print(f"postRoll {rollNum} | userRoll {userRow['rollNum']}")
            if(int(rollNum) == int(userRow['rollNum'])):
                return '<h1>User Already Registered !</h1>'

        with open('data.csv', mode='a') as csv_file:
            data = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            data.writerow([uID, rollNum, userName, phNum, eMail, regOn, passKey])
        return '<h1>Registered Successfully !</h1>'

@app.route('/', methods=['GET', 'POST'])
def cLogin():
    if request.method == 'POST':
        bRollNum = request.form['rollNum']
        bPassKey = request.form['passKey']
        print(allUserData)
        for userRow in allUserData:
            print(userRow)
            print(f"postRoll {bRollNum} | userRoll {userRow['rollNum']}")
            if(int(bRollNum) == int(userRow['rollNum'])):
                if(bPassKey == userRow['passKey']):
                    return render_template("dash.html", userData = userRow) 
    else:
        return render_template('login.html')

@app.route('/changePass', methods=['GET', 'POST'])
def passChange():
    if request.method == 'POST':
        bRollNum = request.form['rollNum']
        bPassKey = request.form['passKey']
        nPassKey = request.form['npassKey']
        for userRow in allUserData:
            print(userRow)
            print(f"postRoll {bRollNum} | userRoll {userRow['rollNum']}")
            if(int(bRollNum) == int(userRow['rollNum'])):
                if(bPassKey == userRow['passKey']):
                    print('updating....')
                    cacheUserData(bRollNum, bPassKey, nPassKey)
                    return otpCheckForPassUpdate(False, userRow['eMail'])
                else:
                    return '<h1>Incorrect Current Password !</h1>'
    else:
        infoMsg = ''
        return render_template('passchange.html', infoMsg = infoMsg)


@app.route('/validate',methods=["POST"])   
def validate():  
    user_otp = request.form['userOtp']  
    print(f"timedOTP {timedOTP} | userOTP {user_otp}")
    if(timedOTP == int(user_otp)):  
        print('Otp Verified...')
        return updatePassKey() 
    return "<h3>failure, OTP does not match</h3>" 



def cacheUserData(rollNum, bPassKey, nPassKey):
    global crollNum,cbPassKey, cnPassKey
    crollNum, cbPassKey, cnPassKey = rollNum, bPassKey, nPassKey

def otpCheckForPassUpdate(isProtoComplete=False, eMail=''):
    global timedOTP
    email = eMail
    timedOTP = randint(000000,999999) 
    msg = Message('OTP',sender = 'meliodastheman106@gmail.com', recipients = [email])  
    msg.body = str(timedOTP)  
    mail.send(msg)  
    print('Mail Sent....')
    return render_template('confirm.html') 

def updatePassKey():
    if(updateCSV('rollNum', crollNum, 'passKey',cbPassKey, cnPassKey)):
        return  '<h1>Password Updated Successfully !</h1>'
    return '<h1>Password Updation Failed !</h1>'

  
    
def fileLoader():
    global allUserData
    with open('data.csv') as csv_file:
            data = csv.reader(csv_file, delimiter=',')
            first_line = True
            allUserData = []
            for row in data:
                if not first_line:
                    print(row)
                    allUserData.append({ 
                        'rollNum' : row[1],
                        'userName' : row[2],
                        'phNum' : row[3],
                        'eMail' : row[4],
                        'passKey' : row[6]
                    })
                else:
                    first_line = False


def updateCSV(colToIdentify, rowVal, colToUpdate, colVal, valToUpdate):
    global allUserData
    print(colToIdentify, rowVal, colToUpdate, colVal, valToUpdate)
    tempfile = NamedTemporaryFile(mode='w', delete=False)
    with open('data.csv','r', newline='', encoding='utf-8') as csv_file, tempfile:
            reader = csv.reader(csv_file, delimiter=',')
            writer =  csv.writer(tempfile, delimiter=',',lineterminator='\n')
            first_line = True
            isUpdated = False
            allUserData = []
            for row in reader:
                if not first_line:
                    print(row)
                    if(row[1] == rowVal):
                        if(row[6] == colVal):
                            row[6] = valToUpdate
                            nRow = { 
                                'id'    : row[0],
                                'rollNum' : row[1],
                                'userName' : row[2],
                                'phNum' : row[3],
                                'eMail' : row[4],
                                'passKey' : row[6]
                            }
                            allUserData.append({ 
                                'rollNum' : row[1],
                                'userName' : row[2],
                                'phNum' : row[3],
                                'eMail' : row[4],
                                'passKey' : row[6]
                            })
                            writer.writerow(nRow)
                            print(nRow)
                            isUpdated = True
                            print('-----DONE-----')
                    writer.writerow(row)

                else:
                    first_line = False


    
    if(isUpdated):
        shutil.move(tempfile.name, 'data.csv')
        fileLoader()
        return True
if __name__ == '__main__':
    fileLoader()
    app.run(debug=True)     