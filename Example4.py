import time
from imp import reload
import  Example3
print("program enter sleep mode ")
time.sleep(15)
reload(Example3)
import  Example3
print("i am last   file ")