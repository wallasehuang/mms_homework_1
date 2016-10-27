
# coding: utf-8

# In[11]:

#multimedia
from PIL import Image
# In[15]:
#Q1
img_q1 = Image.open('Penguins.jpg')
width,height = img_q1.size
pixel = img_q1.load()

for i in xrange(width):
    for j in xrange(height):
        R,G,B = pixel[i,j]
        if i <= width/3:
            pixel[i,j]=(3*R,G,B)
        elif i > width/3 and i<= (width/3)*2:
            pixel[i,j]=(R,3*G,B)
        else:
            pixel[i,j]=(R,G,B*3)

img_q1.save('Q1.jpg')


# In[22]:

#Q2
img_q2 = Image.open('Penguins.jpg').convert('CMYK')
width,height = img_q2.size
piexl = img_q2.load()

#print img_q2.mode

for i in xrange(width):
    for j in xrange(height):
        C,M,Y,K = piexl[i,j]
        if i <= width/4:
            piexl[i,j]=(C*3,M,Y,K)
        elif i>width/4 and i<=(width/4)*2:
            piexl[i,j]=(C,M*3,Y,K)
        elif i>(width/4)*2 and i<=(width/4)*3:
            piexl[i,j]=(C,M,Y*3,K)
        else:
            piexl[i,j]=(C,M,Y,K*3)

img_q2.save('Q2.jpg')


# In[24]:

#Q3
img_q3 = Image.open('Penguins.jpg')
width,height = img_q3.size
piexl = img_q3.load()

for i in xrange(width):
    for j in xrange(height):
        R,G,B = piexl[i,j]
        piexl[i,j] = (255-R,255-G,255-B)

img_q3.save('Q3.jpg')


# In[36]:

#Q4
img_q4 = Image.open('Penguins.jpg')
width,height = img_q4.size
piexl = img_q4.load()

for i in xrange(width):
    for j in xrange(height):
            piexl[i,j] = piexl[i/8*8,j/8*8]

img_q4.save('Q4.jpg')


# In[42]:

#Q5-1
img_q5_1 = Image.open('Penguins.jpg')
width,height = img_q5_1.size
piexl = img_q5_1.load()

for i in xrange(width):
    for j in xrange(height):
        R,G,B=piexl[i,j]
        avgRGB=(R+G+B)/3
        piexl[i,j]=(avgRGB,avgRGB,avgRGB)


img_q5_1.save('Q5-1.jpg')


# In[43]:

#Q5-2
img_q5_2 = Image.open('Penguins.jpg')
width,height = img_q5_2.size
piexl = img_q5_2.load()

for i in xrange(width):
    for j in xrange(height):
        R,G,B=piexl[i,j]
        grayRGB=int(0.299*R+0.587*G+0.114*B)
        piexl[i,j]=(grayRGB,grayRGB,grayRGB)


img_q5_2.save('Q5-2.jpg')


# In[44]:

#Q6-1
img_q6_1 = Image.open('Penguins.jpg')
width,height = img_q6_1.size
piexl = img_q6_1.load()

for i in xrange(width):
    for j in xrange(height):
        R,G,B=piexl[i,j]
        avgRGB=(R+G+B)/3
        threshold = 180
        if avgRGB > threshold:
            piexl[i,j]=(255,255,255)
        else:
            piexl[i,j]=(0,0,0)

img_q6_1.save('Q6-1.jpg')


# In[45]:

#Q6-2
img_q6_2 = Image.open('Penguins.jpg')
width,height = img_q6_2.size
piexl = img_q6_2.load()

for i in xrange(width):
    for j in xrange(height):
        R,G,B=piexl[i,j]
        avgRGB=(R+G+B)/3
        threshold = 64
        if avgRGB > threshold:
            piexl[i,j]=(255,255,255)
        else:
            piexl[i,j]=(0,0,0)

img_q6_2.save('Q6-2.jpg')


# In[46]:

#Q6-3
img_q6_3 = Image.open('Penguins.jpg')
width,height = img_q6_3.size
piexl = img_q6_3.load()

for i in xrange(width):
    for j in xrange(height):
        R,G,B=piexl[i,j]
        avgRGB=(R+G+B)/3
        threshold = 20
        if avgRGB > threshold:
            piexl[i,j]=(255,255,255)
        else:
            piexl[i,j]=(0,0,0)

img_q6_3.save('Q6-3.jpg')


# In[47]:

#Q7-1 RGB->RBG
img_q7_1 = Image.open('Penguins.jpg')
width,height = img_q7_1.size
piexl = img_q7_1.load()

for i in xrange(width):
    for j in xrange(height):
        R,G,B=piexl[i,j]
        piexl[i,j]=(R,B,G)

img_q7_1.save('Q7-1.jpg')


# In[48]:

#Q7-2 RGB->GRB
img_q7_2 = Image.open('Penguins.jpg')
width,height = img_q7_2.size
piexl = img_q7_2.load()

for i in xrange(width):
    for j in xrange(height):
        R,G,B=piexl[i,j]
        piexl[i,j]=(G,R,B)

img_q7_2.save('Q7-2.jpg')


# In[49]:

#Q7-3 RGB->GBR
img_q7_3 = Image.open('Penguins.jpg')
width,height = img_q7_3.size
piexl = img_q7_3.load()

for i in xrange(width):
    for j in xrange(height):
        R,G,B=piexl[i,j]
        piexl[i,j]=(G,B,R)

img_q7_3.save('Q7-3.jpg')


# In[50]:

#Q7-4 RGB->BRG
img_q7_4 = Image.open('Penguins.jpg')
width,height = img_q7_4.size
piexl = img_q7_4.load()

for i in xrange(width):
    for j in xrange(height):
        R,G,B=piexl[i,j]
        piexl[i,j]=(B,R,G)

img_q7_4.save('Q7-4.jpg')


# In[51]:

#Q7-5 RGB->BGR
img_q7_5 = Image.open('Penguins.jpg')
width,height = img_q7_5.size
piexl = img_q7_5.load()

for i in xrange(width):
    for j in xrange(height):
        R,G,B=piexl[i,j]
        piexl[i,j]=(B,G,R)

img_q7_5.save('Q7-5.jpg')


# In[52]:

#Q8
img_q8 = Image.open('Penguins.jpg')
width,height = img_q8.size
piexl = img_q8.load()

for i in xrange(width):
    for j in xrange(height):
        R,G,B=piexl[i,j]
        similarColor = ((R-255)**2+(G-190)**2+(B-25)**2)**0.5
        if similarColor<100.0:
            piexl[i,j]=(R,int(G*0.6),B)

img_q8.save('Q8.jpg')


# In[56]:

#Q9
img_q9 = Image.open('Penguins.jpg')
width,height = img_q9.size
piexl = img_q9.load()

for i in xrange(width-1):
    for j in xrange(height-1):
        R,G,B=piexl[i,j]
        right_R,right_G,right_B=piexl[i+1,j]
        down_R,down_G,down_B=piexl[i,j+1]

        avgRGB = (R+G+B)/3
        avgRightRGB = (right_R+right_G+right_B)/3
        avgDownRGB = (down_R+down_G+down_B)/3

        if ((avgRGB-avgRightRGB)**2)**0.5 >10.0 and ((avgRGB-avgDownRGB)**2)**0.5 >10.0:
            piexl[i,j]=(0,0,0)
        else:
            piexl[i,j]=(255,255,255)
img_q9.save('Q9.jpg')


# In[60]:

#Q10
img_q10 = Image.open('Penguins_noise.jpg')
width,height = img_q10.size
piexl = img_q10.load()

for i in xrange(1,width-1):
    for j in xrange(1,height-1):
        R,G,B=piexl[i,j]
        lt_R,lt_G,lt_B=piexl[i-1,j-1]
        t_R,t_G,t_B=piexl[i,j-1]
        rt_R,rt_G,rt_B=piexl[i+1,j-1]
        r_R,r_G,r_B=piexl[i-1,j]
        l_R,l_G,l_B=piexl[i+1,j]
        ld_R,ld_G,ld_B=piexl[i-1,j+1]
        d_R,d_G,d_B=piexl[i,j+1]
        rd_R,rd_G,rd_B=piexl[i+1,j+1]

        avgRGB=(R+G+B)/3
        avgltRGB=(lt_R+lt_G+lt_B)/3
        avgtRGB=(t_R+t_G+t_B)/3
        avgrtRGB=(rt_R+rt_G+rt_B)/3
        avgrRGB=(r_R+r_G+r_B)/3
        avglRGB=(l_R+l_G+l_B)/3
        avgldRGB=(ld_R+ld_G+ld_B)/3
        avgdRGB=(d_R+d_G+d_B)/3
        avgrdRGB=(rd_R+rd_G+rd_B)/3

        colorList =[(avgRGB,piexl[i,j]),(avgltRGB,piexl[i-1,j-1]),(avgtRGB,piexl[i,j-1]),(avgrtRGB,piexl[i+1,j-1]),(avgrRGB,piexl[i-1,j]),(avglRGB,piexl[i+1,j]),(avgldRGB,piexl[i-1,j+1]),(avgdRGB,piexl[i,j+1]),(avgrdRGB,piexl[i+1,j+1])]
        sortList = sorted(colorList,key = lambda x : x[0])

        avg,rgb = sortList[4]

        piexl[i,j]=rgb
img_q10.save('Q10.jpg')


# In[61]:

#Q11-1 right to left
img_q11_1 = Image.open('Penguins.jpg')
width,height = img_q11_1.size
piexl = img_q11_1.load()

for i in xrange(width):
    for j in xrange(height):
        if i>width/2:
            piexl[i,j]=piexl[width-i,j]
img_q11_1.save('Q11-1.jpg')


# In[65]:

#Q11-2 left to right
img_q11_2 = Image.open('Penguins.jpg')
width,height = img_q11_2.size
piexl = img_q11_2.load()

for i in xrange(width/2):
    for j in xrange(height):
        piexl[i,j]=piexl[width-i-1,j]
img_q11_2.save('Q11-2.jpg')


# In[67]:

#Q11-3 top to down
img_q11_3 = Image.open('Penguins.jpg')
width,height = img_q11_3.size
box = (0,0,width,height/2)

img_region = img_q11_3.crop(box)
img_flip = img_region.transpose(Image.FLIP_TOP_BOTTOM)

img_q11_3.paste(img_flip,(0,height/2,width,height))
img_q11_3.save('Q11-3.jpg')


# In[68]:

#Q11-4 down to top
img_q11_4 = Image.open('Penguins.jpg')
width,height = img_q11_4.size
box = (0,height/2,width,height)

img_region = img_q11_4.crop(box)
img_flip = img_region.transpose(Image.FLIP_TOP_BOTTOM)

img_q11_4.paste(img_flip,(0,0,width,height/2))
img_q11_4.save('Q11-4.jpg')


# In[98]:

#Q12
img_elsa = Image.open('Elsa.jpg')
img_background = Image.open('Chrysanthemum.jpg')
width,height = img_elsa.size
img_background = img_background.resize((width,height))

piexl_elsa = img_elsa.load()
piexl_background = img_background.load()

base_R,base_G,base_B = piexl_elsa[0,0]


for i in xrange(width):
    for j in xrange(height):
        R,G,B = piexl_elsa[i,j]

        similarColor = ((R-base_R)**2+(G-base_G)**2+(B-base_B)**2)**0.5

        if similarColor<23.0:
            piexl_elsa[i,j] = piexl_background[i,j]
img_elsa.save('Q12.jpg')
