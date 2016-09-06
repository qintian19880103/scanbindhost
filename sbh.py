import urllib,urllib2,time,sys,threading,time

class timer(threading.Thread): #The timer class is derived from the class threading.Thread  
    def __init__(self, host, ip):  
        threading.Thread.__init__(self)  
        self.host = host  
        self.ip = ip  
        self.thread_stop = False  
   
    def run(self): #Overwrite run() method, put what you want the thread do here  
        curl(self.host,self.ip)
    def stop(self):  
        self.thread_stop = True  
         


def curl(host,ip):
    url = 'https://'+ip+'/'
    print url
    request = urllib2.Request(url)
    request.add_header('User-Agent', 'baidu')
    request.add_header('HOST', host)
    request.add_header('X-Forwarded-For', '8.8.8.8')
    start_time = time.time()
    try:
        response = urllib2.urlopen(request,timeout=10)
    except:
        #print 'debug error'
        return False
    #print response.read()    
    #print host +' bind ip : ' + ip
    if response.read().find('baidu.com') >= 0:
        file_name = open("c:\\windows\\temp\\1.txt", mode='ab+')
        #file_name = open("/tmp/succeed", mode='ab+')
        file_name.write(host +' bind ip : ' + ip +'\r\n')
        file_name.close()        
    sys.exit(0)



def start(host,ip):
    new_ip = ".".join(ip.split('.')[:2])
    ip = new_ip
    default_threads = 50
    for i in range(0,255):
        new_ip += '.' + str(i)
        for x in range(0,256,default_threads):
            for z in range(1,default_threads+1): 
                if z + x > 255:
                    break
                timer(host, new_ip + '.' + str(x+z)).start()
            x += default_threads
        new_ip = ip



if __name__ == '__main__':
    start('www.baidu.com','220.181.112.224')
    
    
    
