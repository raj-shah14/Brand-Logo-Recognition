import cv2
import numpy as np 
from matplotlib import pyplot as plt
import glob




def des_match(des_l,des_q):
	bf=cv2.BFMatcher(cv2.NORM_L2,crossCheck=True)
	matches=bf.match(des_l,des_q)
	matches = sorted(matches,key=lambda x:x.distance)
	return matches

def check_match(matches,threshold,txt):	
	count=0
	if (matches[0].distance< threshold):
		for i in range (0,len(matches)):
			if (int(matches[i].distance) <=threshold):
				count+=1
				#print matches[i].distance
		#print txt				
		return count
	else:
		print str(txt)+" not found"	

'''
cap=cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS,30)
while (1):
	ret,frame = cap.read()
	cv2.imshow('Query Image',frame)
	if (cv2.waitKey(112)==ord('p')):
		query=frame
		cap.release()
		break
'''

#Ideal Logo
coke=cv2.imread('/home/raj/Downloads/CVproject/IdealLogos/C.jpg')
fanta=cv2.imread('/home/raj/Downloads/CVproject/IdealLogos/F.jpg')
star=cv2.imread('/home/raj/Downloads/CVproject/IdealLogos/S.jpg')
sprite=cv2.imread('/home/raj/Downloads/CVproject/IdealLogos/SP.jpg')
redbull=cv2.imread('/home/raj/Downloads/CVproject/IdealLogos/R.jpg')
pepsi=cv2.imread('/home/raj/Downloads/CVproject/IdealLogos/P.jpg')
heineken=cv2.imread('/home/raj/Downloads/CVproject/IdealLogos/H.jpg')

test_set=glob.glob('/home/raj/Downloads/CVproject/testset/*.jpg')
print len(test_set)

for j in range(0,len(test_set)):
#Query Image
	query=cv2.imread(test_set[j])

	
	C=cv2.cvtColor(coke,cv2.COLOR_BGR2GRAY)
	F=cv2.cvtColor(fanta,cv2.COLOR_BGR2GRAY)
	S=cv2.cvtColor(star,cv2.COLOR_BGR2GRAY)
	SP=cv2.cvtColor(sprite,cv2.COLOR_BGR2GRAY)
	R=cv2.cvtColor(redbull,cv2.COLOR_BGR2GRAY)
	P=cv2.cvtColor(pepsi,cv2.COLOR_BGR2GRAY)
	H=cv2.cvtColor(heineken,cv2.COLOR_BGR2GRAY)


	#Query
	gquery=cv2.cvtColor(query,cv2.COLOR_BGR2GRAY)


	#SIFT Implementation
	sift=cv2.xfeatures2d.SIFT_create()

	#Keypoint and Descriptor for Logos
	kpc,desc = sift.detectAndCompute(C,None)
	kpf,desf = sift.detectAndCompute(F,None)
	kps,dess = sift.detectAndCompute(S,None)
	kpsp,dessp = sift.detectAndCompute(SP,None)
	kpr,desr = sift.detectAndCompute(R,None)
	kpp,desp = sift.detectAndCompute(P,None)
	kph,desh = sift.detectAndCompute(H,None)

	# keypoint and Descriptor for Query
	kpq,desq = sift.detectAndCompute(gquery,None)

	#print temp1
	#img=cv2.drawKeypoints(img,kp4,img)
	#gray4=cv2.drawKeypoints(gray4,kp4,gray4)
	#cv2.imshow("DEs",gray4)

	des_count=[]
	threshold=200
	matches=des_match(desc,desq)
	count=check_match(matches,threshold,txt="Coke")
	des_count.append((count,"Coke"))

	matches=des_match(desf,desq)
	count=check_match(matches,threshold,txt="Fanta")
	des_count.append((count,"Fanta"))

	matches=des_match(dess,desq)
	count=check_match(matches,threshold,txt="Starbucks")
	des_count.append((count,"Starbucks"))

	matches=des_match(dessp,desq)
	count=check_match(matches,threshold,txt="Sprite")
	des_count.append((count,"Sprite"))

	matches=des_match(desr,desq)
	count=check_match(matches,threshold,txt="Redbull")
	des_count.append((count,"Redbull"))

	matches=des_match(desp,desq)
	count=check_match(matches,threshold,txt="Pepsi")
	des_count.append((count,"Pepsi"))

	matches=des_match(desh,desq)
	count=check_match(matches,threshold,txt="Heineken")
	des_count.append((count,"Heineken"))

	print des_count
	x,i=max(des_count)
	print x,i
	
	cv2.putText(query,i,(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
	
	cv2.imshow("Query",query)
	cv2.imwrite('/home/raj/Downloads/CVproject/result/'+str(j)+'.jpg',query)

	cv2.waitKey(0)
	cv2.destroyAllWindows()
	
