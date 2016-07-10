# ##############################################################################
# 							*** SETUP / INSTALLATION ***
# ##############################################################################
# STABLE FILES : https://github.com/MyRobotLab/aiml/tree/master/bots/ [ RACHEL AIML + PYTHON ]
# UPDATED DEV FILES : https://github.com/MyRobotLab/pyrobotlab/tree/master/home/moz4r [ RACHEL AIML + PYTHON ]
# -----------------------------------
# - Inmoov-Life Version 1.3 By Moz4r
# - Credit :
# - Rachel the humano�de
# - Wikidatafetcher By Beetlejuice
# - Grog / Kwatters / and All MRL team
# - HairyGael
# - heisenberg333 for help to construct french AIML brain
# -----------------------------------
# !!! INSTALL : !!!
# !!! PLEASE copy all aiml files to : develop\ProgramAB\bots\rachel\aiml !!!
# !!! AND https://github.com/MyRobotLab/aiml/tree/master/bots/BOTS-FRENCH/Rachel/TXT to the root of MRL
# !!! + https://github.com/MyRobotLab/aiml/tree/master/bots/BOTS-ENGLISH/Rachel/TXT
#
# 
# I use realTime voice syncronisation not mouthcontrol : https://github.com/MyRobotLab/pyrobotlab/blob/master/home/moz4r/mouthcontrol_hardware.ino
#
# ------>
#
#Your language / votre langue( FR/EN )
lang="FR"
# To fetch weather etc [ adresse du serveur fetcher meteo etc ...]
BotURL="http://myai.cloud/bot1.php"
units="metric" # or : imperial
# ##
#
#IF YOU DIDNT HAVE MOTORS set inmoov=0 / Si vous n'avez pas de servo : inmoov=0
IsInmoov=0
leftPort = "COM3"
rightPort = "COM4"

#Eyeleads / paupieres
IhaveEyelids=0
PaupiereServoPin = 27

# Ligh if you have / led RGB with pins
IhaveLights = 0

ROUGE=29
VERT=28
BLEU=30


# ###
# 
# ##############################################################################
#  						*** END SETUP ***
# ##############################################################################






import urllib2
from java.lang import String
import random
import threading
import io
import itertools
import random
import time
import textwrap
import codecs
import socket
import os
import shutil



oridir=os.getcwd().replace("\\", "/")
try:
	shutil.rmtree(oridir+'/ProgramAB/bots/rachel/aimlif')
except: 
	pass


gesturesPath = os.getcwd().replace("develop", "").replace("\\", "/")+"gestures"
BotURL=BotURL+"?lang="+lang+"&FixPhpCache="+str(time.time())


#some voice emotions
laugh = [" #LAUGH01# ", " #LAUGH02# ", " #LAUGH03# ", " ", " "]
troat = [" #THROAT01# ", " #THROAT02# ", " #THROAT03# ", " ", " ", " "]



image=Runtime.createAndStart("ImageDisplay", "ImageDisplay")
sleep(1)
Runtime.createAndStart("chatBot", "ProgramAB")
wdf=Runtime.createAndStart("wdf", "WikiDataFetcher")

i01 = Runtime.createAndStart("i01", "InMoov")
i01.setMute(1)
i01.startEar()
i01.startMouth()

mouth = i01.mouth
ear = i01.ear

webgui = Runtime.create("WebGui","WebGui")
webgui.autoStartBrowser(True)
webgui.startService()
#webgui.startBrowser("http://localhost:8888/#/service/i01.ear")
webgui.start()

if IsInmoov==1:

	
	right = Runtime.start("i01.right", "Arduino")
	right.setBoard("mega2560")
	right.publishState()
	right.connect(rightPort)
	sleep(1)
	if IhaveLights==1:

		right.pinMode(ROUGE, Arduino.OUTPUT)
		right.pinMode(VERT, Arduino.OUTPUT)
		right.pinMode(BLEU, Arduino.OUTPUT)
		

		right.digitalWrite(ROUGE,1)
		right.digitalWrite(VERT,0)
		right.digitalWrite(BLEU,1)
	left = Runtime.start("i01.left", "Arduino")
	left.setBoard("mega2560")
	left.publishState()
	left.connect(leftPort)
	sleep(1)
	
	i01.startRightArm(rightPort)
	i01.startRightHand(rightPort,"atmega2560")
	i01.startLeftHand(leftPort,"atmega2560")
	i01.startHead(leftPort,"atmega2560")
	i01.startLeftArm(leftPort)
	torso = i01.startTorso(leftPort)
	i01.setHeadSpeed(0.5, 0.5)
	i01.head.neck.setMinMax(0,180)
	i01.head.rothead.setMinMax(0,180)
	i01.moveHead(80,86,40,78,76)
	i01.setHeadSpeed(1, 1)
	i01.head.eyeX.setMinMax(0,180)
	i01.head.eyeY.setMinMax(0,180)
	i01.head.eyeX.setRest(90)
	i01.head.eyeY.setRest(90)
	i01.head.eyeY.rest()
	i01.head.eyeX.rest()
	i01.startEyesTracking(leftPort)
	i01.startHeadTracking(leftPort)
	
	i01.eyesTracking.pid.setPID("eyeX",20.0,5.0,0.1)
	i01.eyesTracking.pid.setPID("eyeY",20.0,5.0,0.1)
	i01.headTracking.pid.setPID("rothead",12.0,5.0,0.1)
	i01.headTracking.pid.setPID("neck",12.0,5.0,0.1)
		
	
	
	
	

Runtime.createAndStart("htmlFilter", "HtmlFilter")


	


if lang=="FR":
   voiceType="MargauxSad"
   WikiFile="prop.txt"
   ear.setLanguage("fr-FR")
   wdf.setLanguage("fr")
   wdf.setWebSite("frwiki")
else:
   voiceType="Ryan"
   WikiFile="propEN.txt"
   wdf.setLanguage("en")
   wdf.setWebSite("enwiki")


sleep(2)
mouth.setVoice(voiceType)
mouth.setLanguage(lang)
ear.startListening()



def SaveMemory(question,reponse,silent,justPredicates):
	chatBot.savePredicates()
	if justPredicates==0:
		ServerResponse="0"
		RetourServer=Parse("http://www.myai.cloud/shared_memory.php?action=update&question="+urllib2.quote(question)+"&reponse="+urllib2.quote(reponse.replace("'", " ")))
		print "http://www.myai.cloud/shared_memory.php?action=update&question="+urllib2.quote(question)+"&reponse="+urllib2.quote(reponse.replace("'", " "))
		if silent<>1:
			chatBot.getResponse("SAVEMEMORY")


chatBot.startSession("ProgramAB", "default", "rachel")
#ear.addTextListener(chatBot)
chatBot.addTextListener(htmlFilter)
htmlFilter.addListener("publishText", python.name, "talk") 

if IhaveEyelids==1:
	execfile('../RACHEL_INC_paupieres_eyeleads.py')
execfile('../RACHEL_INC_vie_aleatoire-standby_life.py')


#on bloque le micro quand le robot parle

def onEndSpeaking(text):
	ear.startListening()
	global TimeNoSpeak
	VieAleatoire.startClock()
	TimeNoSpeak="OFF"
	sleep(0.1)
	Light(0,0,0)
	ear.startListening()

def onStartSpeaking(text):
	ear.stopListening()
	global TimeNoSpeak
	TimeNoSpeak="OFF"
	VieAleatoire.stopClock()
	Light(0,0,0)
	
#ear.addTextListener(chatBot)	
def onText(text):
	print text.replace("'", " ")
	chatBot.getResponse(text.replace("'", " "))
	
python.subscribe(ear.getName(),"publishText")

	
	
#on bloque le micro quand le robot parle
		
python.subscribe(mouth.getName(),"publishStartSpeaking")
python.subscribe(mouth.getName(),"publishEndSpeaking")



i01.setMute(0)
		
def talk(data):
	sleep(1)
	#VieAleatoire.stopClock()
	
	if data!="":
		mouth.speak(unicode(data,'utf-8'))


		
def Parse(utfdata):
	#Light(1,1,0)
	utfdata = urllib2.urlopen(utfdata).read()
	utfdata = utfdata.replace("&#039;", "'").replace("http://fr.answers.yahoo.com/question/ind...", "")
	try:
		utfdata = utfdata.decode( "utf8" ).replace(" : ", random.choice(troat))
	except: 
		pass
	print utfdata
	#Light(1,1,1)
	return utfdata;

def MoveHead():
	if IsInmoov==1:
		#i01.attach()
		i01.setHeadSpeed(0.5, 0.5)
		i01.moveHead(20,120,40,78,76)
		time.sleep(2)
		i01.moveHead(150,30,40,78,76)
		time.sleep(2)
		i01.moveHead(80,90,40,78,76)
		#i01.detach()
		
def Light(ROUGE_V,VERT_V,BLEU_V):
	if IhaveLights==1 and IsInmoov==1:
		right.digitalWrite(ROUGE,ROUGE_V)
		right.digitalWrite(VERT,VERT_V)
		right.digitalWrite(BLEU,BLEU_V)


	
def askWiki(query): # retourne la description du sujet (query)
	#Light(1,0,0)
	query = unicode(query,'utf-8')# on force le format de police UTF-8 pour prendre en charge les accents
	if query[1]== "\'" : # Si le sujet contient un apostrophe , on efface tout ce qui est avant ! ( "l'�t�" -> "�t�")
		query2 = query[2:len(query)]
		query = query2
	print query # petit affichage de contr�le dans la console python ..
	word = wdf.cutStart(query) # on enl�ve le derminant ("le chat" -> "chat")
	start = wdf.grabStart(query) # on garde que le d�terminant ( je ne sais plus pourquoi j'ai eu besoin de �a, mais la fonction existe ...)
	wikiAnswer = wdf.getDescription(word) # r�cup�re la description su wikidata
	answer = ( query + " est " + wikiAnswer)
	if (wikiAnswer == "Not Found !") or (unicode(wikiAnswer[-9:],'utf-8') == u"Wikim�dia") : # Si le document n'ai pas trouv� , on r�ponds "je ne sais pas"
		answer=(question(query))
		sleep(1);
		chatBot.getResponse(answer)
	else:
		talk(answer)
	#Light(1,1,1)
	


def getProperty(query, what): # retourne la valeur contenue dans la propri�t� demand�e (what)
	#Light(1,0,0)
	query = unicode(query,'utf-8')
	what = unicode(what,'utf-8')
	if query[1]== "\'" :
		query2 = query[2:len(query)]
		query = query2
	if what[1]== "\'" :
		what2 = what[2:len(what)]
		what = what2
		print "what = " + what + " - what2 = " + what2
	ID = "error"
	# le fichier propri�t�.txt contient les conversions propri�t� -> ID . wikidata n'utilise pas des mots mais des codes (monnaie -> P38)	f = codecs.open(unicode('os.getcwd().replace("develop", "").replace("\", "/") + "/propri�t�s_ID.txt','r',"utf-8") #
	f = codecs.open(os.getcwd().replace("develop", "").replace("\\", "/")+WikiFile,'r','utf-8') #os.getcwd().replace("develop", "").replace("\\", "/") set you propertiesID.txt path
	
	for line in f:
    		line_textes=line.split(":")
    		if line_textes[0]== what:
	    		ID= line_textes[1]
	f.close()
	#print "query = " + query + " - what = " + what + " - ID = " + ID
	wikiAnswer= wdf.getData(query,ID) # r�cup�re la valeur de la propri�t� si elle existe dans le document
	answer = ( what +" de " + query + " est " + wikiAnswer)
	
	if wikiAnswer == "Not Found !":
		answer=(question(query+" "+what))
		sleep(1);
		chatBot.getResponse(answer)
	else:
		talk(answer)
	#Light(1,1,1)
	return answer
	
def getDate(query, ID):# Cette fonction permet d'afficher une date personnalis�e (mardi, le 10 juin, 1975, 12h38 .....)
	answer = ( wdf.getTime(query,ID,"day") +" " +wdf.getTime(query,ID,"month") + " " + wdf.getTime(query,ID,"year"))
	print " La date est : " + answer
	chatBot.getResponse("say Le " + answer)
	
def FindImage(image):
	try:
		image = image.decode( "utf8" )
	except: 
		pass
	mouth.speak(image)
	#PLEASE USE REAL LANGUAGE PARAMETER :
	#lang=XX ( FR/EN/RU/IT etc...)
	#A FAKE LANGUAGE WORKS BUT DATABASE WILL BROKE
	a = Parse(BotURL+"&type=pic&pic="+urllib2.quote(image).replace(" ", "%20"))
	
	DisplayPic(a)
	print BotURL+"&type=pic&pic="+urllib2.quote(image).replace(" ", "%20")
	#Light(1,1,1)
			
def Joke():
	MoveHead()
	a = Parse(BotURL+"&type=joke&genre="+JokeType).replace(" : ", random.choice(troat))
	mouth.speakBlocking(a+' '+random.choice(laugh))
	
def No(data):
	if IsInmoov==999:
		#i01.attach()
		i01.setHeadSpeed(1, 1)
		i01.moveHead(80,90,0,80,40)
		sleep(2)
		i01.moveHead(80,90,180,80,40)
		sleep(1)
		i01.moveHead(80,90,90,80,40)
		sleep(0.5)
	#Light(0,1,1)
	if IsInmoov==1:
		i01.moveHead(81,50,90,78,40)
		sleep(0.5)
		i01.moveHead(79,120,90,78,40)
	chatBot.getResponse("IDONTUNDERSTAND")
	if IsInmoov==1:
		i01.moveHead(80,50,90,78,40)
		sleep(0.5)
		i01.moveHead(83,120,90,78,40)
	sleep(0.5)
	Light(1,1,1)
	if IsInmoov==1:
		i01.moveHead(80,90,90,78,40)
	if IsInmoov==1:
		i01.head.jaw.rest()
		#i01.detach()
	
def Yes(data):
	i01.attach()
	i01.moveHead(80,90,90,180,40)
	sleep(1)
	#Light(1,0,1)
	i01.setHeadSpeed(1, 1)
	i01.moveHead(120,88,90,78,40)
	sleep(0.4)
	i01.moveHead(40,92,90,78,40)
	sleep(0.4)
	mouth.speakBlocking(data.decode( "utf8" ))
	sleep(0.4)
	i01.moveHead(120,87,90,78,40)
	sleep(0.4)
	i01.moveHead(40,91,90,78,40)
	sleep(0.4)
	i01.moveHead(120,87,90,78,40)
	sleep(0.3)
	#Light(1,1,1)
	i01.moveHead(80,90,90,78,40)
	mouth.speakBlocking(random.choice(troat))
	i01.head.jaw.rest()
	i01.detach()
	

	
def ClearMemory():
	chatBot.setPredicate("default","topic","")
	chatBot.setPredicate("default","QUESTION_WhoOrWhat","")
	chatBot.setPredicate("default","QUESTION_sujet","")
	chatBot.setPredicate("default","QUESTION_action","")
	

		
def QueryMemory(question,retour):
	RetourServer=Parse("http://www.myai.cloud/shared_memory.php?action=select&question="+urllib2.quote(question))
	
	if RetourServer!="" and RetourServer!="0":
		chatBot.getResponse("SAY " + RetourServer)
	else:
		chatBot.getResponse(retour)
	
		
def Meteo(data):
	a = Parse(BotURL+"&type=meteo&units="+units+"&city="+urllib2.quote(data).replace(" ", "%20"))
	print BotURL+"&type=meteo&units="+units+"&city="+urllib2.quote(data).replace(" ", "%20")
	mouth.speakBlocking(a)
	MoveHead()

def question(data):
	chatBot.getResponse("FINDTHEWEB")
	a = Parse(BotURL+"&type=question&question="+urllib2.quote(data).replace(" ", "%20"))
	print BotURL+"&type=question&question="+urllib2.quote(data).replace(" ", "%20")
	if a[0]=="0":
		return("IDONTUNDERSTAND")
	elif a[0:299]<>"":
		#return(a[0:299])
		return("IDONTUNDERSTAND")
	else:
		return("IDONTUNDERSTAND")
#if IsInmoov==1:
	#i01.detach()
#Light(1,1,1)


def DisplayPic(pic):
	r=0
	try:
		r=image.displayFullScreen(pic,1)
	except: 
		chatBot.getResponse("PICTUREPROBLEM")
		pass
	time.sleep(0.1)
	try:
		r=image.displayFullScreen(pic,1)
	except:
		pass
	time.sleep(2)
	image.exitFS()
	image.closeAll()


def rest():
	if IsInmoov==1:
		i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
		i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
		i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
		i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
		i01.setHeadSpeed(1.0, 1.0)
		i01.setTorsoSpeed(1.0, 1.0, 1.0)
		i01.moveHead(80,86,82,78,76)
		i01.moveArm("left",5,90,0,10)
		i01.moveArm("right",5,90,0,12)
		i01.moveHand("left",2,2,2,2,2,90)
		i01.moveHand("right",2,2,2,2,2,90)
		i01.moveTorso(80,90,80)
		i01.detach()
  
def trackHumans():
	#i01.headTracking.findFace()
	#i01.opencv.SetDisplayFilter
	i01.headTracking.faceDetect()
	#i01.eyesTracking.faceDetect()
	


	
ClearMemory()

#print gesturesPath
chatBot.getResponse("WAKE_UP")

rest()
if IsInmoov==1:
	i01.head.attach()
	trackHumans()