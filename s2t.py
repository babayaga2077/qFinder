import re
import sys
import os
import speech_recognition as sr

def speech2text(file):
	AUDIO_FILE = file
	r = sr.Recognizer()
	try:
		with sr.AudioFile(AUDIO_FILE) as source:
		        audio = r.record(source)
	except ValueError:
		return ["Audio file could not be read as PCM WAV, AIFF/AIFF-C, or Native FLAC; check if file is corrupted or in another format",0]
	finally:
		os.remove(AUDIO_FILE)
	try:

		msg=r.recognize_google(audio)
		#Adding intelligence to recognize symbols and some words based on phrases
		output = re.sub(r'open single quote|open single court|open single quota|open single cool|single quote',"'",msg.lower())
		output = re.sub(r'open parenthesis',"(",output)
		output = re.sub(r'dash',"-",output)
		output = re.sub(r'- -',"-- -",output)
		output = re.sub(r'email',"@",output)
		output = re.sub(r'close parenthesis',")",output)
		output = re.sub(r'hyphen',"-",output)
		output = re.sub(r'pound sign',"#",output)
		output = re.sub(r'dot|dog|period',".",output)
		output = re.sub(r'dollar sign',"$",output)
		output = re.sub(r'caret',"^",output)
		output = re.sub(r'space'," ",output)
		output = re.sub(r'your surname|your username|you surname|surname|use her name',"username",output)
		output = re.sub(r'open double quote','"',output)
		output = re.sub(r'semicolon',";",output)
		output = re.sub(r'joined|join',"union",output)
		output = re.sub(r'comment python',"#",output)
		output = re.sub(r'comment database|common database',"-- -",output)
		output = re.sub(r'comment php',"//",output)
		output = re.sub(r'equals',"=",output)
		output = re.sub(r'hall',"all",output)
		output = re.sub(r'three',"3",output)
		output = re.sub(r'underscore|on your score',"_",output)
		output = re.sub(r'won|wan|one',"1",output)
		output = re.sub(r'two|to',"2",output)
		output = re.sub(r'aur',"or",output)
		output = re.sub(r'asterisk|asterix|hester it|all',"*",output)
		output = re.sub(r'are',"or",output)
		output = re.sub(r'comma|comment',",",output)
		output = re.sub(r'can catch|can cut|con can',"concat",output)
		output = re.sub(r'idea|design',"schema",output)
		output = re.sub(r'''(?:(?<=\') | (?=\'))''','',output)
		output = re.sub(r'(?:(?<=\_) | (?=\_))','',output)
		output = re.sub(r'(?:(?<=\.) | (?=\.))','',output)
		output = re.sub(r'(?:(?<=\,) | (?=\,))','',output)
		output = re.sub(r'(?:(?<=\") | (?=\"))','',output)
		output = re.sub(r'(?:(?<=\() | (?=\())','',output)
		output = re.sub(r'(?:(?<=\)) | (?=\)))','',output)
		if output=="":
			return ["AI Speech Recognition could not understand audio :(",0]
		return [output,1]



	except sr.UnknownValueError:
	        return ["AI Speech Recognition could not understand audio :(",0]
	except sr.RequestError as e:
	        return ["Could not request results from AI Speech Recognition service; {0}".format(e),0]
