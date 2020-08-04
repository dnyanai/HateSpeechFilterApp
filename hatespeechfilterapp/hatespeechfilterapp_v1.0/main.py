## Google translate API
import googletrans
from googletrans import Translator

## Import flask
from flask import Flask,render_template,request

## Python libraries
import pandas as pd
import re

## Geting the sql data from other file
import connect_getdata


app = Flask(__name__)
app.secret_key = "9890872061"

@app.route('/')
def index():
	return render_template("index.html")


@app.route("/results", methods=["POST"])
def detect():

	## Creating an empty string to collect the changes to the input text
	usrtxt = ''
	new_usrtxt = ''
	#badWord = []
	#badPhrase = []

 	## We will mask the bad words so creating a mask string
	badWordMask = '*@#$%@#$%^~@%^~@#$@#$%^~'

	if request.method == 'POST':
		comment = request.form['comment']
		usrtxt = comment

	data_words,data_phrases = connect_getdata.connect_return_data()
	data = {"Word":data_words,"Phrase":data_phrases}

	df = pd.DataFrame(data)
	df.Word = df.Word.str.lower()
	df.Phrase = df.Phrase.str.lower()

	## For every item in the Word column in the dataframe column word
	for word in df.Word.values:

        ## Here we are using regex to search for the word in the usertext and ignore the case of the input
        ## Regex requires a string or pattern thus we are typ casting to string in case anything is not in string
		wordReplace = re.search(str(word),usrtxt,re.I)

        ## re.search ouputs a match Object for matched result and None for a no-match, thus finding out
        ## and replacing the matched word with the badWorkMask which will be on that word's length
		if wordReplace!=None:
			new_usrtxt = usrtxt.replace(wordReplace.group(0),badWordMask[:len(wordReplace.group(0))])
			#badWord.append(wordReplace.group(0))

    #### Similarly checking for phrases from phrases columns
	for phrase in df.Phrase:
            ## If we do not have any bad (single)words in the user input then do a phrase search on usrtxt
            ## else continue to do a bad phrase check on the modified input in which the bad words are already filtered
		if new_usrtxt!='':
			phrase = re.search(str(phrase),new_usrtxt,re.I)
		else:
			new_usrtxt = usrtxt
			phrase = re.search(str(phrase),new_usrtxt,re.I)
            ## re.search ouputs a match Object for matched result and None for a no-match, thus finding out
            ## and replacing the matched phrase with the badWorkMask which will be on that phrase's length
		if phrase!=None:
			new_usrtxt =  new_usrtxt.replace(phrase.group(0),badWordMask[:len(phrase.group(0))])
			#badPhrase.append(phrase.group(0))

	return render_template('results.html',detected=new_usrtxt,comment=usrtxt)



@app.route('/translate',methods=["POST"])
def enTrans():

	## Creating an empty string to collect the changes to the input text
	usrtxt = ''
	new_usrtxt = ''
	badWord = []
	badPhrase = []

	## We will mask the bad words so creating a mask string
	badWordMask = '*@#$%@#$%^~@%^~@#$@#$%^~'

	if request.method == 'POST':
		comment = request.form['comment']
		usrtxt = comment

	data_words,data_phrases = connect_getdata.connect_return_data()
	data = {"Word":data_words,"Phrase":data_phrases}

	df = pd.DataFrame(data)
	df.Word = df.Word.str.lower()
	df.Phrase = df.Phrase.str.lower()

	## For every item in the Word column in the dataframe column word
	for word in df.Word.values:

	## Here we are using regex to search for the word in the usertext and ignore the case of the input
	## Regex requires a string or pattern thus we are typ casting to string in case anything is not in string
		wordReplace = re.search(str(word),usrtxt,re.I)
	## re.search ouputs a match Object for matched result and None for a no-match, thus finding out
	## and replacing the matched word with the badWorkMask which will be on that word's length
		if wordReplace!=None:
			new_usrtxt = usrtxt.replace(wordReplace.group(0),badWordMask[:len(wordReplace.group(0))])
			badWord.append(wordReplace.group(0))

	#### Similarly checking for phrases from phrases columns
	for phrase in df.Phrase:
		## If we do not have any bad (single)words in the user input then do a phrase search on usrtxt
		## else continue to do a bad phrase check on the modified input in which the bad words are already filtered
		if new_usrtxt!='':
			phrase = re.search(str(phrase),new_usrtxt,re.I)
		else:
			new_usrtxt = usrtxt
			phrase = re.search(str(phrase),new_usrtxt,re.I)
		## re.search ouputs a match Object for matched result and None for a no-match, thus finding out
		## and replacing the matched phrase with the badWorkMask which will be on that phrase's length
		if phrase!=None:
			new_usrtxt =  new_usrtxt.replace(phrase.group(0),badWordMask[:len(phrase.group(0))])
			badPhrase.append(phrase.group(0))


	## Getting the Translator from Googletrans library
	translator= Translator()

	## Creating empty lists to store badwords and badphrases translated to english
	badWrdEng = []
	badPhrseEng = []

	## Get the english translation of the user input data
	usrTxtEng = translator.translate(usrtxt).text

	## If there is a or many badwords in the given text append its english translation to the badWrdEng list
	if badWord!=[]:
		for each in badWord:
			badWrdEng.append(translator.translate(each).text)
	else:
		pass


	## If there is a or many badphrases in the given text append its english translation to the badPhrseEng list
	if badPhrase!=[]:
		for each in badPhrase:
			badPhrseEng.append(translator.translate(each).text)
	else:
		pass

	return render_template('translate.html',inText=usrtxt,badWord=badWord,badPhrase=badPhrase,\
				BWEng=badWrdEng,BPEng=badPhrseEng,\
				usrTxtEng=usrTxtEng,verifiedText=new_usrtxt)


