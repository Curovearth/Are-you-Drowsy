from pkg_resources import to_filename
from scipy.spatial import distance
from imutils import face_utils
import imutils
import dlib
import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
import urllib
import urllib.request
#------------- For Twilio ----------------
import os
from twilio.rest import Client
import playsound
path="alarm.wav"


############################## CREDENTIALS ################################

'''
The credentials are stored in a separate .txt file in the same folder 
Make sure you never share your credentials with someone else

Format for credentials have been given in credentials.txt file
'''

f=open('credentials1.txt','r')
credential=[]
for x in f.readlines():
    credential.append(x)

SID = credential[0]  
token  = credential[1]

account_sid = os.environ.get(SID[:-2])	#TWILIO ACCOUNT SID
auth_token = os.environ.get(token)	#TWILIO_AUTH_TOKEN

client = Client(account_sid, auth_token)

############################## CREDENTIALS SECURED ################################



def eye_aspect_ratio(eye):
	A = distance.euclidean(eye[1], eye[5])
	B = distance.euclidean(eye[2], eye[4])
	C = distance.euclidean(eye[0], eye[3])
	ear = (A + B) / (2.0 * C)
	return ear
	
thresh = 0.25
frame_check = 20
detect = dlib.get_frontal_face_detector()
predict = dlib.shape_predictor("models/shape_predictor_68_face_landmarks.dat")# Dat file is the crux of the code

(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["right_eye"]
cap=cv2.VideoCapture(0)
flag=0
list=[]
drowsy_count=0
total_drowsy=0
blink=0


while True:
	ret, frame=cap.read()
	frame = imutils.resize(frame, width=450)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	subjects = detect(gray, 0)
	for subject in subjects:
		shape = predict(gray, subject)
		shape = face_utils.shape_to_np(shape)#converting to NumPy Array
		leftEye = shape[lStart:lEnd]
		rightEye = shape[rStart:rEnd]
		leftEAR = eye_aspect_ratio(leftEye)
		rightEAR = eye_aspect_ratio(rightEye)
		ear = (leftEAR + rightEAR) / 2.0
		leftEyeHull = cv2.convexHull(leftEye)
		rightEyeHull = cv2.convexHull(rightEye)
		cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
		cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

		#print(shape)

		if ear < thresh:
			
			flag += 1
			# data=urllib.request.urlopen("https://api.thingspeak.com/update?api_key=3UYE569ESMGON9H3&field1="+flag)
			#print (flag)
			list.append(int(flag))
			
			if flag >= frame_check:

				#--------Sound ADDED-----------------

				playsound.playsound(path)

				#--------ADDED-----------------
				
				#---------------------------- Twilio API configuration to send an sms to emergency number ----------------------------
				'''
				Body: The content of the message that will be displayed to your emergency contact number.
				client.api.account.create(<some_code>): a virtual number will be assigned to you when you make your twilio free account where the arguments
					- to: number of emergency contact which should be verified from twilio
					- from_: your own twilio virtual phone number
				'''

				body="You have been selected as an emergency number by Swarup. Swarup is currently feeling drowsiness. Please contact him asap so that he can travel safely."

				# uncomment the below line once the verification of twilio is done
				# client.api.account.messages.create(to="emergency number",from_="+19403267422",body=body)

				# ----------------------------- Working on frame to display a visual alert to the uer. --------------------------------

				# cv2.putText(frame, "****************ALERT!****************", (10, 30),
				# 		cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
				cv2.putText(frame, "****************ALERT!****************", (10,325),
						cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
				print ("Drowsiness detected")
				total_drowsy += 1
				drowsy_count += 1
				cv2.imwrite('Drowsy-Clicks/drowsy%d.jpg' % drowsy_count,frame)		#extracts that particular frame
				
		else:
			flag = 0
			drowsy_count=0
		######################### Drowsy COUNTER ########################

		cv2.putText(frame,f'Drowsy Count: {total_drowsy}',(60,40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv2.LINE_AA)

		######################### Drowsy  COUNTER ########################


	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break
cv2.destroyAllWindows()
cap.release() 
# print(list)
y=np.array(list)
x=np.arange(len(list))

print('total drowsy count:',total_drowsy)

# Matplotlib Plot
plt.title("Values of Drowsiness")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.plot(x,y,color="red")
plt.show()

