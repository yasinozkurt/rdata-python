
from random import randint
import datetime
import json

import copy
from faker import Faker



 

class RandomData:


    def __init__(self):

        self.id=0
       

    def rand_prod(self):
              
        fake=Faker() # Faker modülü birçok random data elde etmeye yarıyor

        self.id+=1

        self.name,self.lastname=fake.first_name(),fake.last_name()

        self.address=fake.address()

        self.birthday=datetime.date(randint(1950,2021),randint(1,12),randint(1,28))

        self.latitude=(18,16)

        self.longtitude=(18,16)


    

with open('text.txt','w') as f:

    data_list=[]

    current_rd=RandomData()

    for i in range(1000):
        
        current_rd.rand_prod()

        copy_dict=copy.deepcopy(current_rd.__dict__) #__dict__ metodu referans dödürdüğünden listeye bağımsız veri eklemek için deepcopy gerekiyor

        data_list.append(copy_dict)
    


    f.write(json.dumps(data_list,indent=4,default=str)) #json serializable olmayan attribute'lar stringe çeviriliyor ve dump ediliyor 
   
   
    

