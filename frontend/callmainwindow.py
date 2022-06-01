 #-*- coding:utf-8 -*-
from ast import Global
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from mainwindow import *
from create_accountwindow import *
from login_window import *
from count import *
from rank_window import *
from PyQt5.QtWidgets import  QMessageBox
from PyQt5.QtCore import Qt
import requests
import json
import cv2
import mediapipe as mp
import time
import random
import math
from playsound import playsound
#import keyboard

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

ip = "140.116.154.65:56543"
Time = 10     #game time
Time_interval = 2

class loginWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(loginWindow, self).__init__()
		self.ui = Ui_loginWindow()
		self.ui.setupUi(self)

		self.ui.pushButton.clicked.connect(self.creat_account)
		self.ui.pushButton_2.clicked.connect(self.login)
		self.ui.pushButton_3.clicked.connect(self.delete)
	
	

	def keyPressEvent(self, event):
		if event.key() == Qt.Key_Return:
			self.login()

	def login(self):
		account = self.ui.lineEdit.text()
		password = self.ui.lineEdit_2.text()
		res = requests.get('http://' + ip + '/api/login?account=' + account+'&passWord='+ password )
        
		dic = json.loads(res.text)
		print(dic['status'])
		if (dic['status']==0):
			self.ui.lineEdit.clear()
			self.ui.lineEdit_2.clear()
			global nickname
			nickname = dic['nickname']
			global UID
			UID = dic['uid']
			window.hide()
			mainwindow.set_text(nickname)
			mainwindow.show()
		elif (dic['status']==1):
			msg = QMessageBox()
			msg.setWindowTitle("錯誤提示")
			msg.setText("帳號不存在")
			msg.exec_()
		else:
			msg = QMessageBox()
			msg.setWindowTitle("錯誤提示")
			msg.setText("密碼錯誤")
			msg.exec_()

	def creat_account(self):
		window.hide()
		accountWindow.show()
		

	def delete(self):          
		self.ui.lineEdit.clear()
		self.ui.lineEdit_2.clear()





class create_accountWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(create_accountWindow, self).__init__()
		self.ui = Ui_create_accountWindow()
		self.ui.setupUi(self)
		self.ui.pushButton.clicked.connect(self.confirm)
		self.ui.pushButton_2.clicked.connect(self.delete)
		self.ui.pushButton_3.clicked.connect(self.clear)

	def clear(self):          
		self.ui.lineEdit.clear()
		self.ui.lineEdit_2.clear()
		self.ui.lineEdit_3.clear()
		self.ui.lineEdit_4.clear()

	def confirm(self):          
		account   = self.ui.lineEdit.text()
		password1 = self.ui.lineEdit_2.text()
		password2 = self.ui.lineEdit_3.text()
		nickname  = self.ui.lineEdit_4.text()
		
		if(password1 != password2):
		    msg = QMessageBox()
		    msg.setWindowTitle("錯誤提示")
		    msg.setText("重新確認密碼")
		    msg.exec_()
		else:
			res = requests.get('http://' + ip + '/api/register?account=' + account+'&passWord='+ password1 +'&nickname='+ nickname)

			dic = json.loads(res.text)
			
			print(dic['status'])
			if(dic['status'] == 0): #success
				msg = QMessageBox()
				msg.setWindowTitle("註冊成功")
				msg.setText("歡迎！")
				msg.exec_()
				self.clear()
				self.close()
				window.show()
			else:
				msg = QMessageBox()
				msg.setWindowTitle("錯誤提示")
				msg.setText("帳號已存在")
				msg.exec_()
			
	def delete(self):
		self.clear()
		self.close()
		window.show()


class MainWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.pushButton.clicked.connect(self.game)
		self.ui.pushButton_2.clicked.connect(self.advgame)
		#self.ui.pushButton_3.clicked.connect(self.user_info)
		self.ui.pushButton_4.clicked.connect(self.rank)
		self.ui.pushButton_5.clicked.connect(self.logout)


		
	def game(self):
		#self.close()
		# For static images:
		countwindow.show()
		global score
		score = 0
		IMAGE_FILES = []
		BG_COLOR = (192, 192, 192) # gray
		with mp_pose.Pose(
		static_image_mode=True,
		model_complexity=2,
		enable_segmentation=True,
		min_detection_confidence=0.5) as pose:
			for idx, file in enumerate(IMAGE_FILES):
				image = cv2.imread(file)
				image_height, image_width, _ = image.shape
				# Convert the BGR image to RGB before processing.
				results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

				if not results.pose_landmarks:
				  continue
				print(
				f'Nose coordinates: ('
				f'{results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x * image_width}, '
				f'{results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y * image_height})'
				)

				annotated_image = image.copy()
				# Draw segmentation on the image.
				# To improve segmentation around boundaries, consider applying a joint
				# bilateral filter to "results.segmentation_mask" with "image".
				condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.1
				bg_image = np.zeros(image.shape, dtype=np.uint8)
				bg_image[:] = BG_COLOR
				annotated_image = np.where(condition, annotated_image, bg_image)
				# Draw pose landmarks on the image.
				mp_drawing.draw_landmarks(
				annotated_image,
				results.pose_landmarks,
				mp_pose.POSE_CONNECTIONS,
				landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
				cv2.imwrite('/tmp/annotated_image' + str(idx) + '.png', annotated_image)
				# Plot pose world landmarks.
				mp_drawing.plot_landmarks(
				results.pose_world_landmarks, mp_pose.POSE_CONNECTIONS)

		# For webcam input:
		cap = cv2.VideoCapture(0)
		with mp_pose.Pose(
			min_detection_confidence=0.5,
			min_tracking_confidence=0.5) as pose:

			time_start = time.time()
			
			
			Changed = 0
			Correct = 0
			X = 0
			Y = 0
			while cap.isOpened():
				success, image = cap.read()
				if not success:
				  print("Ignoring empty camera frame.")
				  # If loading a video, use 'break' instead of 'continue'.
				  continue

				# To improve performance, optionally mark the image as not writeable to
				# pass by reference.
				image.flags.writeable = False
				image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
				results = pose.process(image)
				# print(results)
				# print(results.pose_landmarks)
				# print('-------------------')S
				# print(results.pose_landmarks)
				#if results:
				
				#for i in results.pose_landmarks.landmark:
				#	print(i)
				print('--------------')
				# Draw the pose annotation on the image.
				image.flags.writeable = True
				image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
				mp_drawing.draw_landmarks(
				image,
				results.pose_landmarks,
				mp_pose.POSE_CONNECTIONS,
				landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
				# Flip the image horizontally for a selfie-view display.
			
				time_end = time.time()
				
				
				# Center coordinates 
				Width,Height,c=image.shape
				#print(Width, Height)
				#print(a,b,c)
				if  (int(time_end - time_start) % Time_interval == 0  and Changed == 0) or Correct == 1:
					X = random.randint(0,Height)
					Y = random.randint(0,Width)
					center_coordinates = (X,Y) 
					Changed = 1
					Correct = 0
				elif int(time_end - time_start) % Time_interval == Time_interval/2:	
				    Changed = 0
				        
				# Radius of circle 
				radius = 5
				   
				# Blue color in BGR 
				color = (255, 0, 0) 
				   
				# Line thickness of 2 px 
				thickness = 10
				   
				# Draw a circle with blue line borders of thickness of 2 px 
				image = cv2.circle(image, (X,Y), radius, color, thickness) 
				
				# 15 17 19 21 lefthand
				# 16 18 20 22
				if not results.pose_landmarks:
					continue
				for id, coor in enumerate(results.pose_landmarks.landmark):
					if ( id ==19 or id ==20 ) and coor.visibility > 0.5:
						if abs(X-coor.x*Height) < 40 and abs(Y-coor.y*Width)< 40 :
							print(id, coor.x, coor.y, coor.visibility,X,Y)
							score = score + 1
							Correct = 1
							playsound('./correct.mp3', block=False)
							
							for i in range (0, 5000) :
								image = cv2.circle(image, (X,Y), radius, (0,255,0), thickness) 
				
				
				cv2.imshow('MediaPipe Pose', cv2.flip(image, 1))			
				countwindow.labelupdate(Time-int(time_end - time_start),score)
                
				if  cv2.waitKey(5) & 0xFF == 27 or int(time_end - time_start) == Time: #time setting
					cv2.destroyWindow('MediaPipe Pose')
					break
		cap.release()
		requests.get('http://' + ip + '/api/saveGame?uid=' + str(UID) +'&score='+ str(score) + '&mode='+ 'normal')
		
		
    
	def advgame(self):
		countwindow.show()

		IMAGE_FILES = []
		BG_COLOR = (192, 192, 192) # gray
		with mp_pose.Pose(
		static_image_mode=True,
		model_complexity=2,
		enable_segmentation=True,
		min_detection_confidence=0.5) as pose:
			for idx, file in enumerate(IMAGE_FILES):
				image = cv2.imread(file)
				image_height, image_width, _ = image.shape
				# Convert the BGR image to RGB before processing.
				results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

				if not results.pose_landmarks:
					continue
				print(
				f'Nose coordinates: ('
				f'{results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x * image_width}, '
				f'{results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y * image_height})'
				)

				annotated_image = image.copy()
				# Draw segmentation on the image.
				# To improve segmentation around boundaries, consider applying a joint
				# bilateral filter to "results.segmentation_mask" with "image".
				condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.1
				bg_image = np.zeros(image.shape, dtype=np.uint8)
				bg_image[:] = BG_COLOR
				annotated_image = np.where(condition, annotated_image, bg_image)
				# Draw pose landmarks on the image.
				mp_drawing.draw_landmarks(
				annotated_image,
				results.pose_landmarks,
				mp_pose.POSE_CONNECTIONS,
				landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
				cv2.imwrite('/tmp/annotated_image' + str(idx) + '.png', annotated_image)
				# Plot pose world landmarks.
				mp_drawing.plot_landmarks(
				results.pose_world_landmarks, mp_pose.POSE_CONNECTIONS)

		# For webcam input:
		cap = cv2.VideoCapture(0)
		with mp_pose.Pose(
			min_detection_confidence=0.5,
			min_tracking_confidence=0.5) as pose:

			time_start = time.time()
			score = 0
			
			Changed = 0
			Correct = 0
			Changed2 = 0
			Correct2 = 0
			X = 0
			Y = 0
			X2 = 0
			Y2 = 0
			while cap.isOpened():
				success, image = cap.read()
				if not success:
					print("Ignoring empty camera frame.")
				# If loading a video, use 'break' instead of 'continue'.
					continue

				# To improve performance, optionally mark the image as not writeable to
				# pass by reference.
				image.flags.writeable = False
				image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
				results = pose.process(image)
				# print(results)
				# print(results.pose_landmarks)
				# print('-------------------')S
				# print(results.pose_landmarks)
				#if results:
				
				#for i in results.pose_landmarks.landmark:
				#	print(i)
				print('--------------')
				# Draw the pose annotation on the image.
				image.flags.writeable = True
				image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
				mp_drawing.draw_landmarks(
				image,
				results.pose_landmarks,
				mp_pose.POSE_CONNECTIONS,
				landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
				# Flip the image horizontally for a selfie-view display.
			
				time_end = time.time()
				
				
				# Center coordinates 
				Width,Height,c=image.shape
				#print(Width, Height)
				#print(a,b,c)
				if  (int(time_end - time_start) % Time_interval == 0  and Changed == 0) or Correct == 1:
					X = random.randint(0,Height)
					Y = random.randint(0,Width)
					#X2 = random.randint(0,Height)
					#Y2 = random.randint(0,Width)
					#center_coordinates = (X,Y) 
					Changed = 1
					Correct = 0
				elif int(time_end - time_start) % Time_interval == Time_interval/2:	
					Changed = 0
						
				# Radius of circle 
				radius = 5
				
				# Blue color in BGR 
				color = (255, 0, 0) 
				
				# Line thickness of 2 px 
				thickness = 10
				
				# Draw a circle with blue line borders of thickness of 2 px 
				image = cv2.circle(image, (X,Y), radius, color, thickness) 
				# 15 17 19 21 lefthand
				# 16 18 20 22
				if not results.pose_landmarks:
					continue
				for id, coor in enumerate(results.pose_landmarks.landmark):
					if ( id ==19 or id ==20 ) and coor.visibility > 0.5:
						if  (abs(X-coor.x*Height) < 40 and abs(Y-coor.y*Width)< 40)  :                                                         
							print(id, coor.x, coor.y, coor.visibility,X,Y)
							score = score + 1
							Correct = 1
							playsound('./correct.mp3', block=False)
							for i in range (0, 5000) :
								image = cv2.circle(image, (X,Y), radius, (0,255,0), thickness) 
				
				## second  point 
				if  (int(time_end - time_start) % Time_interval == 0  and Changed2 == 0) or Correct2 == 1:
					X2 = random.randint(0,Height)
					Y2 = random.randint(0,Width)
					#X2 = random.randint(0,Height)
					#Y2 = random.randint(0,Width)
					#center_coordinates = (X,Y) 
					Changed2 = 1
					Correct2 = 0
				elif int(time_end - time_start) % Time_interval == Time_interval/2:	
					Changed2 = 0
						
				# Radius of circle 
				radius = 5
				
				# Blue color in BGR 
				color = (255, 0, 0) 
				
				# Line thickness of 2 px 
				thickness = 10
				
				# Draw a circle with blue line borders of thickness of 2 px 
				image = cv2.circle(image, (X2,Y2), radius, color, thickness) 
				# 15 17 19 21 lefthand
				# 16 18 20 22
				if not results.pose_landmarks:
					continue
				for id, coor in enumerate(results.pose_landmarks.landmark):
					if ( id ==19 or id ==20 ) and coor.visibility > 0.5:
						if  (abs(X2-coor.x*Height) < 40 and abs(Y2-coor.y*Width)< 40)  :                                                         
							print(id, coor.x, coor.y, coor.visibility,X2,Y2)
							score = score + 1
							Correct2 = 1
							playsound('./correct.mp3', block=False)
							for i in range (0, 5000) :
								image = cv2.circle(image, (X2,Y2), radius, (0,255,0), thickness) 
				
				cv2.imshow('MediaPipe Pose', cv2.flip(image, 1))			
				countwindow.labelupdate(Time-int(time_end - time_start),score)
				
				if  cv2.waitKey(5) & 0xFF == 27 or int(time_end - time_start) == Time: #time setting
					cv2.destroyWindow('MediaPipe Pose')
					break
		cap.release()

	#def user_info(self):
		

	def rank(self):
		res=requests.get('http://' + ip + '/api/scoreboard?mode=' + 'normal' )
		dic = json.loads(res.text)
		print(dic)
		record = ['null' for i in range(5)]
		for i in range(len(dic)) :
			#record[i] = str(dic[i]['uid']) + str(dic[i]['gameId']) + dic[i]['date'] + str(dic[i]['score'])
			tmp = str(dic[i]['date']).spilt('GMT')	
			record[i] = str(dic[i]['score']) + '   ' + tmp[0]
		rankwindow.set_text(record[0],record[1],record[2],record[3],record[4])
		
		rankwindow.show()

	def logout(self):
		flag = QtWidgets.QMessageBox.question(self, "登出","是否要登出")
		if flag == QtWidgets.QMessageBox.Yes:
		    
		    self.close()
		    window.show()
	def set_text(self,nickname):		    
	    self.ui.label.setText("Hi,"+str(nickname))

class countWindow(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		super(countWindow, self).__init__()
		self.ui = Ui_countWindow()
		self.ui.setupUi(self)
		self.ui.pushButton.clicked.connect(self.confirm)

	def labelupdate(self,Time,Score):
		self.ui.label_3.setText(str(Time))
		self.ui.label_4.setText(str(Score))	

	def confirm(self):
		self.close()


class rankWindow(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		super(rankWindow, self).__init__()
		self.ui = Ui_rankWindow()
		self.ui.setupUi(self)
		
	def set_text(self, str1, str2, str3, str4, str5):		    
			self.ui.label_6.setText(str1)
			self.ui.label_7.setText(str2)
			self.ui.label_8.setText(str3)
			self.ui.label_9.setText(str4)
			self.ui.label_10.setText(str5)


		 
if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = loginWindow()
	mainwindow = MainWindow()
	accountWindow = create_accountWindow()
	countwindow = countWindow()
	rankwindow = rankWindow()
	window.show()
	sys.exit(app.exec_())
	
