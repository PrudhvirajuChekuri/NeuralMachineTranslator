import os
import shutil
import warnings
warnings.filterwarnings('ignore')
from flask import send_file
from getmail import send_mail
from utils import encode_input_str
from flask_restful import Api, Resource
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, jsonify
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer


tokenizer = 'mt5_tokenizer'
model_path = 'fine_tuned_full'
langs = ["en", "te", "hi"]
LANG_TOKEN_MAPPING = {'en': '<en>', 'te': '<te>','hi': '<hi>'}

tokenizer = AutoTokenizer.from_pretrained(tokenizer)
model = AutoModelForSeq2SeqLM.from_pretrained(model_path)

app = Flask(__name__)
app.config['DEBUG'] = True
api = Api(app)

class TranslateText(Resource):
    def post(self):

        data = request.json
        text = data['text']
        dest_lang = data['dest_lang']

        input_ids = encode_input_str(
            text = text,
            target_lang = dest_lang,
            tokenizer = tokenizer,
            seq_len = model.config.max_length,
            lang_token_map = LANG_TOKEN_MAPPING)
        input_ids = input_ids.unsqueeze(0)

        output_tokens = model.generate(input_ids, num_beams=10, num_return_sequences=2)

        output_text = tokenizer.decode(output_tokens[0], skip_special_tokens=True)

        return {'translated_text': output_text}

api.add_resource(TranslateText, "/translate")

def MakeZipgen(filepath):
    shutil.make_archive('./gendata', 'zip', filepath)

@app.route('/deletegen')
def deletegen():
    if "gendata.zip" in os.listdir("./"):
        os.remove("gendata.zip")
    return ("nothing")

@app.route('/')
def home():
	return render_template("home.html")

@app.route('/translate')
def translate():
    return render_template('translate.html')

@app.route('/translate_text', methods=['POST'])
def translate_text():
    input_lang = request.form['input_lang']
    output_lang = request.form['output_lang']
    input_text = request.form['input_text']
    
    if (input_lang not in langs) or (output_lang not in langs):
        return jsonify({'output_text': "Invalid lang code"})

    input_ids = encode_input_str(
            text = input_text,
            target_lang = output_lang,
            tokenizer = tokenizer,
            seq_len = model.config.max_length,
            lang_token_map = LANG_TOKEN_MAPPING)
    input_ids = input_ids.unsqueeze(0)

    output_tokens = model.generate(input_ids, num_beams=10, num_return_sequences=2)

    output_text = tokenizer.decode(output_tokens[0], skip_special_tokens=True)
    return jsonify({'output_text': output_text})

@app.route('/getdata')
def getdata():
    return render_template('inputfordata.html')

@app.route('/gen', methods=['GET', 'POST'])
def gen():
    dirs = ["gen", "gen/input", "gen/output"]

    if dirs[0] in os.listdir("./"):
        shutil.rmtree("gen")

    for dir in dirs:
        os.mkdir(dir)

    UPLOAD_FOLDER = './gen/input'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    if(request.method == 'POST'):
        for file in request.files.getlist('file'):
            if file:
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                path = "gen/input/" + str(filename)
                
                with open(path, mode = 'r') as f:
                    data = f.read()

                input_lang, output_lang = data[:2], data[3:5]
                data = data.split('\n')[1:]

                
                output_text = ""
                for sen in data:

                    input_ids = encode_input_str(
                                text = sen,
                                target_lang = output_lang,
                                tokenizer = tokenizer,
                                seq_len = model.config.max_length,
                                lang_token_map = LANG_TOKEN_MAPPING)
                    input_ids = input_ids.unsqueeze(0)

                    output_tokens = model.generate(input_ids, num_beams=10, num_return_sequences=2)

                    output_text += tokenizer.decode(output_tokens[0], skip_special_tokens=True) + '\n'
                
                filepath = f"gen/output/{str(filename[:-4])}_{output_lang}.txt"
                with open(filepath, 'w', encoding = "utf-8") as f:
                        f.write(output_text)

        MakeZipgen('./gen')
    
    path='gendata.zip'
    shutil.rmtree("gen")
    return send_file(path,as_attachment=True)

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/sentsafe',methods=['GET', 'POST'])
def send_sentsafe():
    if request.method == 'POST':
        email = request.form['email']
        comments = request.form['comments']
        name=request.form['name']
        comments=email+"  \n "+"Name:"+name+"  \n "+"Feedback:"+comments
        send_mail(email,comments)
    return render_template('sentfeed.html')

if __name__=="__main__":
    app.run(debug=True)