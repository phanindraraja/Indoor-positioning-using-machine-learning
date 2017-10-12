import os
import csv
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from math import exp
import bluetooth
from PyOBEX.client import Client

B1=np.ones((16,1050))
B2=np.ones((16,1050))
B3=np.ones((16,1050))
B4=np.ones((16,1050))

def test_regression():
    global B1
    global B2
    global B3
    global B4
    b1=[]
    b2=[]
    b3=[]
    b4=[]
    rootDir = r'C:\Users\Phanindra\Desktop\Data req\New folder\16datapts'
    for dirName, subdirList, fileList in os.walk(rootDir):
        #print('Found directory: %s' % dirName)
        #print(subdirList)
        #print(fileList)
        #for subname in subdirList:
            #print('\t%s' % subname)
            #for fname in fileList:
                #print('\t\t%s' % fname)
        if len(fileList)>0:
            #print(fileList)
            i=1
            for fname in fileList:
            #print(dirName+'\\'+fname)
                if (fname[15]=='1'):
                    x=np.genfromtxt(dirName+'\\'+fname, unpack=True, skip_header=1,delimiter=',')[1,:]
                    x=x.tolist()
                    b1.append(x)
                    i+=1
                if (fname[15]=='2'):
                    y=np.genfromtxt(dirName+'\\'+fname, unpack=True, skip_header=1,delimiter=',')[1,:]
                    y=y.tolist()
                    b2.append(y)
                    i+=1
                if (fname[15]=='3'):
                    z=np.genfromtxt(dirName+'\\'+fname, unpack=True, skip_header=1,delimiter=',')[1,:]
                    z=z.tolist()
                    b3.append(z)
                    i+=1
                if (fname[15]=='4'):
                    v=np.genfromtxt(dirName+'\\'+fname, unpack=True, skip_header=1,delimiter=',')[1,:]
                    v=v.tolist()
                    b4.append(v)
                    i+=1
                
    j=0
    for i in range(16):
        v=b1[j]+b1[j+1]+b1[j+2]+b1[j+3]
        j=j+4
        for k in range(len(v)):
            B1[i][k]=v[k]
    j=0
    for i in range(16):
        v=b2[j]+b2[j+1]+b2[j+2]+b2[j+3]
        j=j+4
        for k in range(len(v)):
            B2[i][k]=v[k]
    j=0
    for i in range(16):
        v=b3[j]+b3[j+1]+b3[j+2]+b3[j+3]
        j=j+4
        for k in range(len(v)):
            B3[i][k]=v[k]
    j=0
    for i in range(16):
        v=b4[j]+b4[j+1]+b4[j+2]+b4[j+3]
        j=j+4
        for k in range(len(v)):
            B4[i][k]=v[k]
    B1=B1[:,:950]
    B2=B2[:,:950]
    B3=B3[:,:950]
    B4=B4[:,:950]

    B1_avg=np.ones((16,190))
    B2_avg=np.ones((16,190))
    B3_avg=np.ones((16,190))
    B4_avg=np.ones((16,190))

    for i in range(16):
        k=0
        for j in range(190):
            B1_avg[i][j]=(B1[i][k]+B1[i][k+1]+B1[i][k+2]+B1[i][k+3]+B1[i][k+4])/(5.0)
            k+=5

    for i in range(16):
        k=0
        for j in range(190):
            B2_avg[i][j]=(B2[i][k]+B2[i][k+1]+B2[i][k+2]+B2[i][k+3]+B2[i][k+4])/(5.0)
            k+=5

    for i in range(16):
        k=0
        for j in range(190):
            B3_avg[i][j]=(B3[i][k]+B3[i][k+1]+B3[i][k+2]+B3[i][k+3]+B3[i][k+4])/(5.0)
            k+=5

    for i in range(16):
        k=0
        for j in range(190):
            B4_avg[i][j]=(B4[i][k]+B4[i][k+1]+B4[i][k+2]+B4[i][k+3]+B4[i][k+4])/(5.0)
            k+=5

    with open('data.csv','w') as f:
        writer=csv.writer(f)
        writer.writerow(["position","beacon1","beacon2","beacon3","beacon4"])
        for i in range(16):
            for x,y,z,v in zip(B1_avg[i][:],B2_avg[i][:],B3_avg[i][:],B4_avg[i][:]):
                writer.writerow([str(i+1),str(x),str(y),str(z),str(v)])

    df = pd.read_csv("data.csv")
    train_cols = df.columns[1:]
    out_cols = df.columns[0]
    v=np.array(df[train_cols])
    s=np.array(df[out_cols])
    s1 = [[i] for i in s]
    s2=np.array(s1)
    model = LogisticRegression(multi_class='multinomial',solver ='newton-cg',max_iter=1000)
    model = model.fit(v,s2.ravel())
    return model 

def formulae(r1,r2,r3,r4):
    #op_e.clear()
    del op_e[:]
    #op.clear()
    del op[:]
    for i in range(16):
        b=(y[i][0]*r1)+(y[i][1]*r2)+(y[i][2]*r3)+(y[i][3]*r4)+z[i]
        op_e.append(b)
    for i in range(16):
        l=((exp(op_e[i]))/(1+(exp(op_e[i]))))
        op.append(l)
  
print "Starting to regress"
# model = test_regression()

print "Finished Regression"
from Demo_data import data_sample
#np.savetxt('coef.csv', np.array(model.coef_), delimiter=',')
#np.savetxt('intercep.csv', np.array(model.intercept_), delimiter=',')

print "Loading parameters"
y=np.loadtxt('coef.csv', delimiter =',')
z=np.loadtxt('intercep.csv', delimiter =',')
print "Loaded"
while True:
    x = input("Enter to start")
    B1_rand, B2_rand, B3_rand, B4_rand = data_sample()
    op_e=[]
    op=[]
    a=[0 for i in range(16)]
    for j in range(min([B1_rand.shape[0], B2_rand.shape[0], B3_rand.shape[0], B4_rand.shape[0] ])):
        formulae(float(B1_rand[j]),float(B2_rand[j]),float(B3_rand[j]),float(B4_rand[j]))
        b=op.index(max(op))
        a[b]+=1
        count=(a.index(max(a)))+1
        
    address = '40:83:DE:A4:18:20'
    svc = bluetooth.find_service(address=address, uuid='1105')
    
    first_match = svc[0]
    port = first_match["port"]
    name = first_match["name"]
    host = first_match["host"]
    print("Connecting to \"%s\" on %s" % (name, host))
    client = Client(host, port)
    client.connect() 
    client.put("test.txt", str(count))
    client.disconnect()
