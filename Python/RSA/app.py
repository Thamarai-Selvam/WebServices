from flask import Flask, request
import math, random 

app = Flask(__name__)
#common error handler
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>Page not found.</p>", 404
  

def prime_check(a):
    if(a==2):
        return True
    elif((a<2) or ((a%2)==0)):
        return False
    elif(a>2):
        for i in range(2,a):
            if not(a%i):
                return False
    return True

#GCD
'''CALCULATION OF GCD FOR 'e' CALCULATION.'''
def egcd(e,r):
    while(r!=0):
        e,r=r,e%r
    return e

#Euclid's Algorithm
def eugcd(e,r):
    for i in range(1,r):
        while(e!=0):
            a,b=r//e,r%e
            if(b!=0):
                print("%d = %d*(%d) + %d"%(r,a,e,b))
            r=e
            e=b

#Extended Euclidean Algorithm
def eea(a,b):
    if(a%b==0):
        return(b,0,1)
    else:
        gcd,s,t = eea(b,a%b)
        s = s-((a//b) * t)
        print("%d = %d*(%d) + (%d)*(%d)"%(gcd,a,t,s,b))
        return(gcd,t,s)

#Multiplicative Inverse
def mult_inv(e,r):
    gcd,s,_=eea(e,r)
    if(gcd!=1):
        return None
    else:
        if(s<0):
            print("s=%d. Since %d is less than 0, s = s(modr), i.e., s=%d."%(s,s,s%r))
        elif(s>0):
            print("s=%d."%(s))
        return s%r

def encrypt(pub_key,n_text):
    e,n=pub_key
    x=[]
    m=0
    for i in n_text:
        if(i.isupper()):
            m = ord(i)-65
            c=(m**e)%n
            x.append(c)
        elif(i.islower()):               
            m= ord(i)-97
            c=(m**e)%n
            x.append(c)
        elif(i.isspace()):
            spc=400
            x.append(400)
    return x
    
    
def decrypt(priv_key,c_text):
    d,n=priv_key
    txt=c_text.split(', ')
    x=''
    m=0
    for i in txt:
        if(i=='400'):
            x+=' '
        else:
            m=(int(i)**d)%n
            m+=65
            c=chr(m)
            x+=c
    return x
    
def md5(message, opChoice):
    
    primes = [i for i in range(0,999) if prime_check(i)]
    p = random.choice(primes)
    q = random.choice(primes)
    print(p,q)
    p = 7
    q = 17

        
    check_p = prime_check(p)
    check_q = prime_check(q)
    while(((check_p==False)or(check_q==False))):
        p = int(input("Enter a prime number for p: "))
        q = int(input("Enter a prime number for q: "))
        check_p = prime_check(p)
        check_q = prime_check(q)

    #RSA Modulus
    '''CALCULATION OF RSA MODULUS 'n'.'''
    n = p * q
    print("RSA Modulus(n) is:",n)

    #Eulers Toitent
    '''CALCULATION OF EULERS TOITENT 'r'.'''
    r= (p-1)*(q-1)
    print("Eulers Toitent(r) is:",r)
        
    #e Value Calculation
    '''FINDS THE HIGHEST POSSIBLE VALUE OF 'e' BETWEEN 1 and 1000 THAT MAKES (e,r) COPRIME.'''
    for i in range(1,1000):
        if(egcd(i,r)==1):
            e=i
    print("The value of e is:",e)

    #d, Private and Public Keys
    print("EUCLID'S ALGORITHM:")
    eugcd(e,r)
    print("END OF THE STEPS USED TO ACHIEVE EUCLID'S ALGORITHM.")
    print("EUCLID'S EXTENDED ALGORITHM:")
    d = mult_inv(e,r)
    print("END OF THE STEPS USED TO ACHIEVE THE VALUE OF 'd'.")
    print("The value of d is:",d)
    public = (e,n)
    private = (d,n)
    print("Private Key is:",private)
    print("Public Key is:",public)
    if(opChoice == 0):
        result = encrypt(public,message)
    else:
        result = decrypt(private, message)
  
    return str(result)
#---------------Tranpose--------------------
@app.route('/rsa', methods=['GET'])
def otpGen():
  
    message = request.args['message']
    opChoice = int(request.args['opChoice'])

    value = enc_msg=md5(message, opChoice)
    return {'message' : message, 'value' : value}
    # return home(message, value)

@app.route('/', methods=['GET','POST'])
def home(message='HELLO THERE !', value=""):
  return '''<!DOCTYPE html>
<html>
<head>
<title>RSA</title>
<style>
body {
  background-color: #4db8ff;
  text-align: center;
  color: white;
  font-family: Arial, Helvetica, sans-serif;
}
span {
	color : white;
    font-style: oblique;
}
.info {
	background-color : #0099ff;
    padding : 20px;
    margin: -10px -10px 0 -10px;
}
.api_proc {
	background-color: #6600cc;
    padding:7px;
    border-radius:20px;
}
.workarea {
text-align : left;
padding : 50px;
}

input[type=text] {
  width: 80%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
  
}
input[type=submit] {
  width: 40%;
  background-color:   #00b359;
  color: white;
  padding: 10px 20px;
  margin: 8px 0;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size:17px;
}

input[type=submit]:hover {
  background-color: #00994d;
}
.response_form {
	padding-top:50px;
}
</style>

</head>
<body>
<div class="info">
<h1>RSA</h1>
<p>Returns the encrypted/decrypted message </p>
<p class="api_proc">API Call Format : <span>http://localhost:5000/rsa?message=heythere&opChoice=0</span></p>
</div>
<div class="workarea">

<form action="/rsa">
  <label for="message">RSA Length</label><br>
   <center> <select name="opChoice" id="opChoice" >
                <option id="enc" value="0" selected='true'>Encrypt</option>
                <option id="dec" value="1">Decrypt</option>
            </select>
    </center>
    </br>
  <label for="message">Message to Encrypt</label><br>
  <input type="text" id="message" name="message" value="'''+message+'''"><br>
  <input type="submit" value="Submit">
</form>
<form class="response_form">
  <label for="response">Checksum</label><br>
  <input type="text" id="response" name="response" value="'''+value+'''"><br>
</form>
</div>

</body>
</html>

'''

if __name__ == '__main__':
  app.run(debug=True)
