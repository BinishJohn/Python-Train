#Write Data Into A File 
from datetime import datetime
file_object = open('write.txt','w')
file_object.write("Hello How Are You")
file_object.write(str(datetime.now()))
file_object.close()
