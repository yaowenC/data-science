import sys
import ssl
import urllib.request
import matplotlib.pyplot as plt

context = ssl._create_unverified_context()
file = urllib.request.urlopen('https://ceiba.ntu.edu.tw/course/481ea4/hw1_data.csv', context=context)
dataori = file.read()
data = dataori.decode().split('\n')
for i in range(len(sys.argv)): 
    if i > 0:
        if sys.argv[i][1]== 'E': 
            m=[]
            f=[]
            total=[]
            xnames=[]
            pie_size=[]
            name = data[1][0:15]
            for row in data[2:7]:
                split_list = row.split(',')
                xnames.append(split_list[0])
                m.append(float(split_list[2]))
                f.append(float(split_list[4]))
                result = (float(split_list[1])*float(split_list[2])+float(split_list[3])*float(split_list[4]))/(float(split_list[1])+float(split_list[3]))
                total.append(round(result,1))
                pie = (float(split_list[1])*float(split_list[2])+float(split_list[3])*float(split_list[4]))/100
                pie_size.append(pie)
        elif sys.argv[i][1]== 'A': 
            m=[]
            f=[]
            total=[]
            xnames=[]
            pie_size=[]
            name = data[7][0:22]
            for row in data[8:11]:
                split_list = row.split(',')
                xnames.append(split_list[0])
                m.append(float(split_list[2]))
                f.append(float(split_list[4]))
                result = (float(split_list[1])*float(split_list[2])+float(split_list[3])*float(split_list[4]))/(float(split_list[1])+float(split_list[3]))
                total.append(round(result,1))
                pie = (float(split_list[1])*float(split_list[2])+float(split_list[3])*float(split_list[4]))/100
                pie_size.append(pie)
        elif sys.argv[i][1]== 'W': 
            m=[]
            f=[]
            total=[]
            xnames=[]
            pie_size=[]
            name = data[11][0:19]
            for row in data[12:15]:
                split_list = row.split(',')
                xnames.append(split_list[0])
                m.append(float(split_list[2]))
                f.append(float(split_list[4]))
                result = (float(split_list[1])*float(split_list[2])+float(split_list[3])*float(split_list[4]))/(float(split_list[1])+float(split_list[3]))
                total.append(round(result,1)) 
                pie = (float(split_list[1])*float(split_list[2])+float(split_list[3])*float(split_list[4]))/100
                pie_size.append(pie)
        if sys.argv[i][2]== 'l' and (sys.argv[i][1]== 'A' or sys.argv[i][1]== 'W') :
            fig = plt.figure()
            ax = fig.add_subplot(111) 
            x = range(3)
            plt.xticks(x, xnames)  
            plt.plot(x,m,color='red',label='Male',marker='x')
            plt.plot(x,f,color='green',label='Female',marker='o')
            plt.plot(x,total,color='blue',label='Total',marker='*')
            plt.legend(loc = 'upper right')
            plt.title('Smoking percentage vs '+ str(name))
            plt.xlabel(str(name))
            plt.ylabel("Smoking Percentage (%)")
            for i,j in zip(x,m):
                ax.annotate('%s' %j,xy=(i,j), textcoords='data')
            for i,j in zip(x,f):
                ax.annotate('%s' %j,xy=(i,j), textcoords='data')
            for i,j in zip(x,total):
                ax.annotate('%s' %j,xy=(i,j), textcoords='data')
            plt.show()
        elif sys.argv[i][2]== 'l':
            fig = plt.figure()
            ax = fig.add_subplot(111) 
            x = range(5)
            plt.xticks(x, xnames)  
            plt.plot(x,m,color='red',label='Male',marker='x')
            plt.plot(x,f,color='green',label='Female',marker='o')
            plt.plot(x,total,color='blue',label='Total',marker='*')
            plt.legend(loc = 'upper right')
            plt.title('Smoking percentage vs '+ str(name))
            plt.xlabel(str(name))
            plt.ylabel("Smoking Percentage (%)")
            for i,j in zip(x,m):
                ax.annotate('%s' %j,xy=(i,j), textcoords='data')
            for i,j in zip(x,f):
                ax.annotate('%s' %j,xy=(i,j), textcoords='data')
            for i,j in zip(x,total):
                ax.annotate('%s' %j,xy=(i,j), textcoords='data')
            plt.show()  
        elif sys.argv[i][2]== 'b' and (sys.argv[i][1]== 'A' or sys.argv[i][1]== 'W') :
            fig = plt.figure()
            ax = fig.add_subplot(111) 
            x = range(3)  
            bar_width = 0.25
            rects1 = ax.bar([float(s)-bar_width for s in x], m,bar_width,color='r',label='Male')
            rects2 = ax.bar([float(s) for s in x], f,bar_width,color='g',label='Female')
            rects3 = ax.bar([float(s)+bar_width for s in x], total,bar_width,color='b',label='Total')
            plt.xticks(x, xnames)
            plt.title('Smoking percentage vs '+ str(name))
            plt.xlabel(str(name))
            plt.ylabel("Smoking Percentage (%)")
            for i,j in zip(rects1,m):
                height = i.get_height()
                ax.text(i.get_x() + i.get_width()/2, height + 0.5, j, ha='center', va='bottom')
            for i,j in zip(rects2,f):
                height = i.get_height()
                ax.text(i.get_x() + i.get_width()/2, height + 0.5, j, ha='center', va='bottom')
            for i,j in zip(rects3,total):
                height = i.get_height()
                ax.text(i.get_x() + i.get_width()/2, height + 0.5, j, ha='center', va='bottom')
            plt.legend(loc='upper right')
            plt.show()  
        elif sys.argv[i][2]== 'b':
            fig = plt.figure()
            ax = fig.add_subplot(111) 
            x = range(5)  
            bar_width = 0.25
            rects1 = ax.bar([float(s)-bar_width for s in x], m,bar_width,color='r',label='Male')
            rects2 = ax.bar([float(s) for s in x], f,bar_width,color='g',label='Female')
            rects3 = ax.bar([float(s)+bar_width for s in x], total,bar_width,color='b',label='Total')
            plt.xticks(x, xnames)
            plt.title('Smoking percentage vs '+ str(name))
            plt.xlabel(str(name))
            plt.ylabel("Smoking Percentage (%)")
            for i,j in zip(rects1,m):
                height = i.get_height()
                ax.text(i.get_x() + i.get_width()/2, height + 0.5, j, ha='center', va='bottom')
            for i,j in zip(rects2,f):
                height = i.get_height()
                ax.text(i.get_x() + i.get_width()/2, height + 0.5, j, ha='center', va='bottom')
            for i,j in zip(rects3,total):
                height = i.get_height()
                ax.text(i.get_x() + i.get_width()/2, height + 0.5, j, ha='center', va='bottom')
            plt.legend(loc='upper right')
            plt.show()  
        elif sys.argv[i][2]== 'p' and (sys.argv[i][1]== 'A' or sys.argv[i][1]== 'W') : 
            colors = ['gold', 'yellowgreen', 'lightcoral']
            plt.title('Proportion of different '+ str(name) + ' in smoking population')
            plt.pie(pie_size, labels=xnames, colors=colors, autopct='%1.1f%%', startangle=30)
            plt.axis('equal')
            plt.tight_layout()
            plt.show() 
        elif sys.argv[i][2]== 'p':
            colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red']  
            plt.title('Proportion of different '+ str(name) + ' in smoking population')
            plt.pie(pie_size, labels=xnames, colors=colors, autopct='%1.1f%%', startangle=30)
            plt.axis('equal')
            plt.tight_layout()
            plt.show()   
file.close()