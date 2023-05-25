# 🚗 Are you Drowsy? 💤

<p>
  In fiscal year 2019, the road transport passengers amounted to around <a href="https://www.statista.com/statistics/667456/road-transport-passengers-india/
">22.6 trillion passengers per kilometer accross India.</a>
  The fact that this number is so huge where we can’t rely on other driving passenger for our safety leads us to at least contribute to develop a system which can be used in the mobile vehicles to monitor the drivers at each and every moment.

This project is a drowsiness detection system. It uses a camera to monitor the EAR (eye aspect ratio) of the driver. After it reaches a certain value, an alarm is played to wake the driver and make him focus on the road. If you are travelling in a group, this could be a good time switching drivers.
</p>

<p align=center>
  <samp>"<a href="https://www.thehindu.com/news/national/kerala/sleep-deprived-drivers-responsible-for-40-of-road-accidents-say-transport-officials/
">40% of the on road accidents</a> occur due to <em>Sleep deprivation</em>"</samp>
</p>

<p>
  The following project is an implementation of <a href="https://github.com/akshaybahadur21/Drowsiness_Detection">@akshaybahadur21: Drowsiness Detection System</a>, with additional improvements to give users more detailed information. Below I have mentioned the changes,
  
- [X] Graphical Output 
- [X] Drowsy Count displayed on the screen
- [X] Twilio API integration to send 'sms' to emergency contact number
- [ ] Displaying real time data over thingspeak 
   
</p>
<hr>

| To know about Algorithm and Code Dependencies | I highly recommend you to visit <a href="https://github.com/akshaybahadur21/Drowsiness_Detection">@akshaybahadur21: Drowsiness Detection System</a>  |
| --- | --- |

## Results 💯

<p align=center>
  <img src="https://github.com/Curovearth/Are-you-Drowsy/blob/main/img/working%20GIF.gif" width=729 /><br>
  To view, <a href="https://github.com/Curovearth/Are-you-Drowsy/blob/main/img/working.mov">video file</a>
</p>

| <p>Whenever the screen displays "Drowsiness Detected", SMS is sent to the verified<br> emergency contact number using Twilio API.<br> <a href="https://www.twilio.com/">TWILIO</a> <br><img src="https://twilio-cms-prod.s3.amazonaws.com/images/sms-email.width-600.format-jpeg.jpegquality-85.jpg" width=300 /></p> | <img src="https://github.com/Curovearth/Are-you-Drowsy/blob/main/img/sms.png" /> |
| --- | --- |
| Below, these were the frames which were captured at the time of drowsiness | Not a really "good acting" from my end |
| <img src="https://github.com/Curovearth/Are-you-Drowsy/blob/main/Drowsy-Clicks/drowsy1.jpg" width=400 /> | <img src="https://github.com/Curovearth/Are-you-Drowsy/blob/main/Drowsy-Clicks/drowsy2.jpg" width=400 /> |


## Execution 🔧

- You need to run the **main_drowsy.py** for execution 
```python
C:\Users\iwill\Desktop\github\11-Are you Drowsy\Are-you-Drowsy> python main_drowsy.py
```

- The frames captured via execution of the project will update automatically via this line and will be saved in the Drowsy-Clicks folder
```python
cv2.imwrite('Drowsy-Clicks/drowsy%d.jpg' % drowsy_count,frame)		#extracts that particular frame
```

- For Twilio API to work uncomment the below line which is commented out by default
- For Twilio Documentation, <a href="https://www.twilio.com/docs/messaging">see</a>
```python
client.api.account.messages.create(to="emergency_number",from_="+19403267422",body=body)
```

## Contribution 🤝
This project has a room for lots of improvement which can be done together to add new features or displaying the data in a more beautiful manner.
I hope you can connect with me via my <a href="https://discord.com/channels/718336604887973939">Discord</a>

<br>
I hope you like the project<br>
~ Swarup Tripathy ⏳
