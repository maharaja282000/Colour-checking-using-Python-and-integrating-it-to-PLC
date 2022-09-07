import cv2
import pyautogui as p
lastclipcount=0
import time
import snap7
from snap7.util import *
from snap7.types import *
client=snap7.client.Client()
client.connect("10.74.12.142",0,1,102)
print(bool(client.get_connected))
#cv2.rectangle(frame, (cx - 220, 10), (cx + 200, 120), (255, 255, 255), -1)
print("                            Rane ZF - Trichy                        ")
print("                 LEADWIRE CLIP COLOUR DETECTION & DISTANCE CHECKING      ")
print("-----------------------------------------------------------------------------------------------")
print("\nList of models available:")
print("               Model 1 : Manual BN7-R")
print("               Model 2 : Power BN7-R")
modelselector=int(input("\nScan the QR-code for Model Selection"))
if(modelselector==1):
    print("Setting up camera for Model 1 : Manual BN7-R")
elif(modelselector==2):
    print("Setting up camera for Model 2 : Power BN7-R")
string="0"
count=0  #partcount
li1=100
li2=100
li3=100
li4=100
tli=100
cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape
    print(p.position())
    if(modelselector==1):
        px1= 184
        py1= 304
        px2= 461
        py2= 304
        px3= 845
        py3= 304
        px4= 993
        py4= 304
        clip4 = "C&D"
        clip3 = "C&D"
        clip2 = "C&D"
        clip1 = "C&D"
        cv2.circle(frame, (px1, py1), 5, (0, 0, 255), 3)
        cv2.circle(frame, (px2, py2), 5, (0, 0, 255), 3)
        cv2.circle(frame, (px3, py3), 5, (0, 0, 255), 3)
        cv2.circle(frame, (px4, py4), 5, (0, 0, 255), 3)
        cv2.rectangle(frame, (983, 654), (1255, 558), (255, 255, 255), -1)
        cv2.rectangle(frame, (18,613), (267,465), (0, 0, 0), -1)
        cv2.putText(frame,"4", (994, 289), 2, 1,(0,0,0), 1)
        cv2.putText(frame,"3", (845, 289), 2, 1,(0,0,0), 1)
        cv2.putText(frame,"2", (462, 289), 2, 1,(0,0,0), 1)
        cv2.putText(frame,"1", (182, 289), 2, 1,(0,0,0), 1)
        pixel_c1 = hsv_frame[py1, px1]
        pixel_c2 = hsv_frame[py2, px2]
        pixel_c3 = hsv_frame[py3, px3]
        pixel_c4 = hsv_frame[py4, px4]

        #hues
        hue_value1 = pixel_c1[0]
        hue_value2 = pixel_c2[0]
        hue_value3 = pixel_c3[0]
        hue_value4 = pixel_c4[0]

        #saturations
        sat_value1=pixel_c1[1]
        sat_value2=pixel_c2[1]
        sat_value3=pixel_c3[1]
        sat_value4=pixel_c4[1]

        #vibrance
        vib_value1=pixel_c1[2]
        vib_value2=pixel_c2[2]
        vib_value3=pixel_c3[2]
        vib_value4=pixel_c4[2]
    
        if (hue_value1>=95 and hue_value1<=110):
            if(vib_value1>=140 and vib_value1<=150):
                lastclipcount=lastclipcount+1
                if(lastclipcount>=1):
                    li1=1
                    bv1=li1.to_bytes(2,"big")
                    client.db_write(62,2,bv1)
                if(li1==1):
                    clip1="C&D"
                    cv2.circle(frame, (px1, py1), 5, (0,255,0), 3)
                    
        else:
            clip1="C&D"
       
        
        if(hue_value2>=93 and hue_value2<=110):
            if(vib_value2>=130 and vib_value2<=140):
                li2=1
                bv2=li2.to_bytes(2,"big")
                client.db_write(62,4,bv2)
            if(li2==1):
                clip2="C&D"
                cv2.circle(frame, (px2, py2), 5, (0,255,0), 3)
        else:
            clip2="C&D"
       
        
        if(hue_value3>=93 and hue_value3<=110):
            if(vib_value3>=130 and vib_value3<=140):
                li3=1
                bv3=li3.to_bytes(2,"big")
                client.db_write(62,6,bv3)
            if(li3==1):
                clip3="C&D"
                cv2.circle(frame, (px3, py3), 5, (0,255,0), 3)
        else:
            clip3="C&D"
        
                    
    
        if(vib_value4>=12 and vib_value4<=20):
            if (hue_value4>110 and hue_value4<=130):
                li4=1
                bv4=li4.to_bytes(2,"big")
                client.db_write(62,8,bv4)
            if(li4==1):
                clip4="C&D"
                cv2.circle(frame, (px4, py4), 5, (0,255,0), 3)
        else:
            clip4="C&D"
            
        if(li1==1):
            cv2.putText(frame,"Clip 1 : "+clip1, (37,478+20), 2, 1,(0,255,0), 2)
        elif(li1==0):
            cv2.putText(frame,"Clip 1 : "+clip1, (37,478+20), 2, 1,(0,0,255), 2)
        else:
            cv2.putText(frame,"Clip 1 : "+clip1, (37,478+20), 2, 1,(0,255,255), 2)
        if(li2==1):  
            cv2.putText(frame,"Clip 2 : "+clip2, (37,478+30+20), 2, 1,(0,255,0), 2)
        elif(li2==0):
            cv2.putText(frame,"Clip 2 : "+clip2, (37,478+30+20), 2, 1,(0,0,255), 2)
        else:
            cv2.putText(frame,"Clip 2 : "+clip2, (37,478+30+20), 2, 1,(0,255,255), 2) 
        if(li3==1):
            cv2.putText(frame,"Clip 3 : "+clip3, (37,478+60+20), 2, 1,(0,255,0), 2)
        elif(li3==0):
            cv2.putText(frame,"Clip 3 : "+clip3, (37,478+60+20), 2, 1,(0,0,255), 2)
        else:
            cv2.putText(frame,"Clip 3 : "+clip3, (37,478+60+20), 2, 1,(0,255,255), 2)
        if(li4==1):
            cv2.putText(frame,"Clip 4 : "+clip4, (37,478+90+20), 2, 1,(0,255,0), 2)
        elif(li4==0):
            cv2.putText(frame,"Clip 4 : "+clip4, (37,478+90+20), 2, 1,(0,0,255), 2)
        else:
             cv2.putText(frame,"Clip 4 : "+clip4, (37,478+90+20), 2, 1,(0,255,255), 2)
        
        if(li4==1 and li2==1 and li3==1 and li1==1):        
            cv2.circle(frame, (px1, py1), 5, (0,0,255), 3)
            cv2.circle(frame, (px2, py2), 5, (0,0,255), 3)
            cv2.circle(frame, (px3, py3), 5, (0,0,255), 3)
            cv2.circle(frame, (px4, py4), 5, (0,0,255), 3)
            tli=1
            li1=100
            bv1=li1.to_bytes(2,"big")
            client.db_write(62,2,bv1)
            li2=100
            bv2=li2.to_bytes(2,"big")
            client.db_write(62,4,bv2)
            li3=100
            bv3=li3.to_bytes(2,"big")
            client.db_write(62,6,bv3)
            li4=100
            bv4=li4.to_bytes(2,"big")
            client.db_write(62,8,bv4)
            #for i in range(0,3000):
            cv2.putText(frame,"Colour : OK ", (997, 584), 2, 1,(0,255,0), 3)
            cv2.putText(frame,"Distance : OK ", (997, 614), 2, 1,(0,255,0), 3)
            time.sleep(3)
            count=count+1
            bv0=count.to_bytes(2,"big")
            client.db_write(62,0,bv0)
            string=str(count)
        #cv2.putText(frame,"Colour : OK ", (997, 584), 2, 1,(0,255,0), 3)
        #cv2.putText(frame,"Distance : OK ", (997, 614), 2, 1,(0,255,0), 3)
        #cv2.rectangle(frame, (63,54), (751, 37), (255, 255, 255), -1)
        cv2.rectangle(frame, (182,58), (901,38+20), (255, 255, 255), -1)
        cv2.putText(frame," Lead wire Clip colour & Distance Checking", (80+100, 35+10), 2,1,(255,0,255), 1)
        cv2.rectangle(frame, (47, 124), (573, 81), (255, 255, 255), -1)
        cv2.putText(frame,"Model Selected : Manual BN7-R", (40+6, 80+35), 2,1,(226,43,138), 2)
        cv2.rectangle(frame, (58,223), (273, 185), (255, 255, 255), -1)
        cv2.putText(frame,"OK-Part : "+string, (53+6, 180+35), 2, 1,(255,0,0), 2)
        
        cv2.imshow("lead wire clip colour", frame)
        key = cv2.waitKey(1)

    elif(modelselector==2):
        px1= 559
        py1= 304
        px2= 861
        py2= 304
        px3= 1010
        py3= 304
        cv2.circle(frame, (px1, py1), 5, (0, 0, 255), 3)
        cv2.circle(frame, (px2, py2), 5, (0, 0, 255), 3)
        cv2.circle(frame, (px3, py3), 5, (0, 0, 255), 3)
        cv2.rectangle(frame, (983, 654), (1255, 558), (255, 255, 255), -1)
        #cv2.putText(frame,"Colour : NOK ", (997, 584), 2, 1,(0,0,255), 3)
        #cv2.putText(frame,"Distance : NOK ", (997, 614), 2, 1,(0,0,255), 3)
        pixel_c1 = hsv_frame[py1, px1]
        pixel_c2 = hsv_frame[py2, px2]
        pixel_c3 = hsv_frame[py3, px3]
        
        hue_value1 = pixel_c1[0]
        hue_value2 = pixel_c2[0]
        hue_value3 = pixel_c3[0]

        sat_value1=pixel_c1[1]
        sat_value2=pixel_c2[1]
        sat_value3=pixel_c3[1]
        
        #vibrance
        vib_value1=pixel_c1[2]
        vib_value2=pixel_c2[2]
        vib_value3=pixel_c3[2]
    
        if (hue_value1>=95 and hue_value1<=110):
            if(vib_value1>=140 and vib_value1<=150):
                lastclipcount=lastclipcount+1
                if(lastclipcount>=1):
                    li1=1
                    if(li1==1):
                        cv2.circle(frame, (px1, py1), 5, (0,255,0), 3)                                                  
        
        if(hue_value2>=93 and hue_value2<=110):
            if(vib_value2>=130 and vib_value2<=140):
                li2=1
                if(li2==1):
                    cv2.circle(frame, (px2, py2), 5, (0,255,0), 3)                                                  
    
        if(vib_value3>=12 and vib_value3<=20):
            if (hue_value3>110 and hue_value3<=130):
                li3=1
                if(li3==1):
                    cv2.circle(frame, (px3, py3), 5, (0,255,0), 3)
        
        
        if(li3==1 and li2==1 and li1==1):        
            cv2.circle(frame, (px1, py1), 5, (0,0,255), 3)
            cv2.circle(frame, (px2, py2), 5, (0,0,255), 3)
            cv2.circle(frame, (px3, py3), 5, (0,0,255), 3)
            tli=1
            li1=0
            li2=0
            li3=0
            li4=0
            cv2.waitKey(4000)
            cv2.putText(frame,"Colour : OK ", (997, 584), 2, 1,(0,255,0), 3)
            cv2.putText(frame,"Distance : OK ", (997, 614), 2, 1,(0,255,0), 3)
            cv2.waitKey(4000)
            #time.sleep(3)
            count=count+1
            string=str(count)
        #cv2.rectangle(frame, (63,54), (751, 37), (0, 0, 255), -1)
        cv2.putText(frame,"Lead wire clip colour & Distance checking", (80+50, 35), 2,1,(255,0,255,), 1)
        cv2.rectangle(frame, (47, 124), (573, 81), (255, 255, 255), -1)
        cv2.putText(frame,"Model selected : Power BN7-R ", (40+6, 80+35), 2, 1,(226,43,138), 2)
        cv2.rectangle(frame, (58,223), (273, 185), (255, 255, 255), -1)
        cv2.putText(frame,"OK-part : "+string, (53+6, 180+35), 2, 1,(255,0,0), 2)
        cv2.imshow("lead wire clip colour", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break

cap.release()
cv2.destroyAllWindows()
