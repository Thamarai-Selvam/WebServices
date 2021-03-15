from flask import Flask, request, Response, render_template, send_file,Markup
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from hurry.filesize import size
from Huffman_Coding.app import compress_file, decompress_file
from Run_Length_Coding.app import encode, decode
from LZW_Coding.app import compress, deCompress
app = Flask(__name__)
sFileSize = fFileSize = 0

def huffman(idata):
    global sFileSize, fFileSize
    if idata :
        filename = secure_filename(idata.filename)
        print(filename)
    sFileSize, fFileSize = compress_file(idata, str(idata.filename+'.cmp'))
    # return str(sFileSize), str(fFileSize)
    return send_file(str(idata.filename+'.cmp'), as_attachment=True)
    # return "Success"

def dchuffman(idata):
    global sFileSize, fFileSize
    if idata :
        filename = secure_filename(idata.filename)
        print(filename[0:-4])
    fFileSize,sfFileSize = decompress_file(idata, str(idata.filename[0:-4]))
    # return str(sFileSize), str(fFileSize)
    return send_file(str(idata.filename[0:-4]), as_attachment=True)
    # return "Success"

def runLength(idata):

    return encode(idata)

def lZW(idata):

    global sFileSize, fFileSize
    if idata :
        filename = secure_filename(idata.filename)
        print(filename)
    sFileSize, fFileSize = compress(idata, str(idata.filename+'.cmp'))
    # return str(sFileSize), str(fFileSize)
    return send_file(str(idata.filename+'.cmp'), as_attachment=True)
    
def dcrunLength(idata):

    return decode(idata)

def dclZW(idata):

    global sFileSize, fFileSize
    if idata :
        filename = secure_filename(idata.filename)
        print(filename[0:-4])
    fFileSize,sfFileSize = deCompress(idata, str(idata.filename[0:-4]))
    # return str(sFileSize), str(fFileSize)
    return send_file(str(idata.filename[0:-4]), as_attachment=True)

@app.route('/downFile', methods=['GET', 'POST'])
def downloadFile():
   
    filename = request.form['itextVal'] + '.cmp'
    print(filename)
    return send_file(filename, as_attachment=True)
    

@app.route('/dcdownFile', methods=['GET', 'POST'])
def dcdownloadFile():
   
    filename = request.form['itextVal'] 
    print(filename)
    return send_file(filename, as_attachment=True)


@app.route('/compress', methods=['GET', 'POST'])
def getHandler():
    global sFileSize, fFileSize
    sFileSize = fFileSize = 0
    print(request.form)
    opChoice = int(request.form['opChoice'])
    opCmpChoice = int(request.form['opCmpChoice'])
    idata = request.form['itext']
    tFile = request.files['ifile']
    print(request.files)
    if tFile :
        print('file is there-> ', tFile)
        idata = request.files['ifile']
    print(idata)
    if (opCmpChoice == 0):
        if(opChoice == 0):
            huffman(idata)
            form = Markup('<form class="response_form" id="response_form" action="/downFile" method=post enctype=multipart/form-data>\
                <label for="ofile">UnCompressed File Size '+str(size(sFileSize))+'</label></br>\
                <label for="cfile">Compressed File Size '+str(size(fFileSize))+'</label></br>\
                <input type="hidden" id="itextVal" name="itextVal" value=""></br>\
                <input type="submit" id="dbtn" name="dbtn" value="Download File"></br>\
            </form>')
        elif(opChoice == 1):
            cText = runLength(idata)
            form = Markup('<form class="response_form" id="response_form" action="/dcdownFile" method=post enctype=multipart/form-data>\
                <label for="ofile">UnCompressed Text '+str(idata)+'</label></br>\
                <label for="cfile">Compressed Text '+str(cText)+'</label></br>\
                <input type="hidden" id="itextVal" name="itextVal" value=""></br>\
            </form>')
        else:
            lZW(idata)
            form = Markup('<form class="response_form" id="response_form" action="/downFile" method=post enctype=multipart/form-data>\
                <label for="ofile">UnCompressed File Size '+str(size(sFileSize))+'</label></br>\
                <label for="cfile">Compressed File Size '+str(size(fFileSize))+'</label></br>\
                <input type="hidden" id="itextVal" name="itextVal" value=""></br>\
                <input type="submit" id="dbtn" name="dbtn" value="Download File"></br>\
            </form>')
        

        # iresult = switcher.get(opChoice,('Invalid data supplied', 500))
        # print(iresult)
       
        return render_template('index.html',resp_form=form)
    else:
        if(opChoice == 0):
            dchuffman(idata)
            form = Markup('<form class="response_form" id="response_form" action="/dcdownFile" method=post enctype=multipart/form-data>\
                <label for="ofile">UnCompressed File Size '+str(size(sFileSize))+'</label></br>\
                <label for="cfile">Compressed File Size '+str(size(fFileSize))+'</label></br>\
                <input type="hidden" id="itextVal" name="itextVal" value=""></br>\
                <input type="submit" id="dbtn" name="dbtn" value="Download File"></br>\
            </form>')
        elif(opChoice == 1):
            dcText = dcrunLength(idata)
            form = Markup('<form class="response_form" id="response_form" action="/dcdownFile" method=post enctype=multipart/form-data>\
                <label for="ofile">UnCompressed Text '+str(idata)+'</label></br>\
                <label for="cfile">Compressed Text '+str(dcText)+'</label></br>\
                <input type="hidden" id="itextVal" name="itextVal" value=""></br>\
            </form>')
        else:
            dclZW(idata)
            form = Markup('<form class="response_form" id="response_form" action="/dcdownFile" method=post enctype=multipart/form-data>\
                <label for="ofile">UnCompressed File Size '+str(size(sFileSize))+'</label></br>\
                <label for="cfile">Compressed File Size '+str(size(fFileSize))+'</label></br>\
                <input type="hidden" id="itextVal" name="itextVal" value=""></br>\
                <input type="submit" id="dbtn" name="dbtn" value="Download File"></br>\
            </form>')
        # switcher = { 
        #     0: dchuffman(idata), 
        #     1: dcrunLength(idata),  
        #     2: dclZW(idata), 
        # }     
        # iresult = switcher.get(opChoice,('Invalid data supplied', 500))
        
        return render_template('index.html',resp_form=form)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>Page not found.</p>", 404


@app.route('/', methods=['GET','POST'])
def home():
  return render_template('index.html')
if __name__ == '__main__':
  app.run(debug=True)