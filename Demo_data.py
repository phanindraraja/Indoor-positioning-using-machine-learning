import csv
import numpy as np

def data_sample():
    import serial 
    serial = serial.Serial("COM1", 115200)

    with open("data_unfiltered.txt", "w") as f:
        i=1
        while i<=200:
            for v in range(1,22):
                data = serial.read()
                if v==21:
                    f.write("\n")
                elif v==17:
                    pass 
                else:
                    f.write(str(data))    
            i+=1
    with open("data_unfiltered.txt", "r") as f:
        with open("data_filtered.txt", "w") as f1:
            for s in range(200):
                data1=f.readline()
                f1.write(data1[11:15]+","+data1[16:19]+"\n")
    
    with open('data_filtered.txt', 'r') as f1:
        stripped_data = (line.strip() for line in f1)
        grouped = [line.split(',') for line in stripped_data]
        with open('data_filtered.csv', 'w') as f2:
            writer = csv.writer(f2)
            writer.writerow(['Slave', 'RSSI'])
            writer.writerows(grouped)
    
    with open('data_filtered.csv', 'r') as f2:
        reader = csv.reader(f2)
        v=1
        x=1
        y=1
        z=1
        fb1=open('data_filtered_b1.csv', 'w')
        fb2=open('data_filtered_b2.csv', 'w')
        fb3=open('data_filtered_b3.csv', 'w')
        fb4=open('data_filtered_b4.csv', 'w')
        for row in reader:
            for field in row:
                if field=="69DF":
                    writer = csv.writer(fb4)
                    if v==1:
                        writer.writerow(["Slave","RSSI"])
                        v+=1
                    writer.writerow(row)
                elif field=="41F3":
                    writer = csv.writer(fb2)
                    if x==1:
                        writer.writerow(["Slave","RSSI"])
                        x+=1
                    writer.writerow(row)
                elif field=="6CDD":
                    writer = csv.writer(fb1)
                    if y==1:
                        writer.writerow(["Slave","RSSI"])
                        y+=1
                    writer.writerow(row)
                elif field=="459F":
                    writer = csv.writer(fb3)
                    if z==1:
                        writer.writerow(["Slave","RSSI"])
                        z+=1
                    writer.writerow(row)
        fb1.close()
        fb2.close()
        fb3.close()
        fb4.close()
    
    v=[]
    w=[]
    with open('data_filtered_b1.csv', 'r') as fb1:
        reader=csv.reader(fb1)
        for row in reader:
            if row[1]!="RSSI":
                v.append(row[1])
    z=len(v)%5
    y=len(v)-z
    a=int(y/5)
    i=0
    for r in range(a):
        s=0
        for x in range(5):
            s+=int(v[i])
            i+=1
        avg=(s/5)
        w.append(str(avg))
#    with open('data_filtered_b1_avg.csv', 'w', newline='') as fb1a:
#        writer=csv.writer(fb1a)
#        writer.writerow(["Slave","RSSI"])
#        for t in w:
#            writer.writerow(["6CDD",t])
    B1_rand = w

    q=[]
    e=[]
    with open('data_filtered_b2.csv', 'r') as fb2:
        reader=csv.reader(fb2)
        for row in reader:
            if row[1]!="RSSI":
                q.append(row[1])
    z=len(q)%5
    y=len(q)-z
    a=int(y/5)
    i=0
    for r in range(a):
        s=0
        for x in range(5):
            s+=int(q[i])
            i+=1
        avg=(s/5)
        e.append(str(avg))
#    with open('data_filtered_b2_avg.csv', 'w', newline='') as fb2a:
#        writer=csv.writer(fb2a)
#        writer.writerow(["Slave","RSSI"])
#        for t in e:
#            writer.writerow(["41F3",t])
    B2_rand = e

    o=[]
    p=[]
    with open('data_filtered_b3.csv', 'r') as fb3:
        reader=csv.reader(fb3)
        for row in reader:
            if row[1]!="RSSI":
                o.append(row[1])
    z=len(o)%5
    y=len(o)-z
    a=int(y/5)
    i=0
    for r in range(a):
        s=0
        for x in range(5):
            s+=int(o[i])
            i+=1
        avg=(s/5)
        p.append(str(avg))
#    with open('data_filtered_b3_avg.csv', 'w', newline='') as fb3a:
#        writer=csv.writer(fb3a)
#        writer.writerow(["Slave","RSSI"])
#        for t in p:
#            writer.writerow(["459F",t])
    B3_rand = p
    g=[]
    h=[]
    with open('data_filtered_b4.csv', 'r') as fb4:
        reader=csv.reader(fb4)
        for row in reader:
            if row[1]!="RSSI":
                g.append(row[1])
    z=len(g)%5
    y=len(g)-z
    a=int(y/5)
    i=0
    for r in range(a):
        s=0
        for x in range(5):
            s+=int(g[i])
            i+=1
        avg=(s/5)
        h.append(str(avg))
#    with open('data_filtered_b4_avg.csv', 'w', newline='') as fb4a:
#        writer=csv.writer(fb4a)
#        writer.writerow(["Slave","RSSI"])
#        for t in h:
#            writer.writerow(["69DF",t])
    B4_rand = h
    return np.array(B1_rand), np.array(B2_rand), np.array(B3_rand), np.array(B4_rand)

#A, B, C, D = data_sample()
#print A.shape
#print B.shape
#print C.shape
#print D.shape

