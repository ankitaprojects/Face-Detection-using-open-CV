#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install opencv-python --user


# In[4]:


import cv2


# In[6]:


face_cascade = cv2.CascadeClassifier(r'C:\Users\ankit\Desktop\frontalface_default.xml')


# In[9]:


cap = cv2.VideoCapture(r'C:\Users\ankit\Desktop\Technical round\ef3e_elem_r&c1&2_short film.mp4')


# In[ ]:


while True:
    # Read the frame
    _, img = cap.read()


# In[ ]:


# Convert to grayscale
   gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# In[ ]:


# Detect the faces
   faces = face_cascade.detectMultiScale(gray, 1.1, 4)


# In[ ]:


# Draw the rectangle around each face
   for (x, y, w, h) in faces:
       cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)


# In[ ]:


# Display
    cv2.imshow('img', img)


# In[ ]:


# Stop if escape key is pressed
   k = cv2.waitKey(30) & 0xff
   if k==27:
       break


# In[ ]:


# Release the VideoCapture object
cap.release()

