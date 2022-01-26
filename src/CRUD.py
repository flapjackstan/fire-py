from firebase import firebase

class db:

    def __init__(self,username,url):
        self.username = username
        
        #(url,authentification details)
        self.fb = firebase.FirebaseApplication(url, None)
        
    def user(self):
        print(self.user)
        
    def create_table(self,table,df):
        df = df.applymap(str)
        
        for i in range(df.shape[0]):
            data = df.iloc[i]
            data = data.to_dict()
            result = self.fb.post(self.username+table,data, {'print':'pretty'})
            print(result)
        
    def create_record(self,table,data):
    
        result = self.fb.post(self.username+table,data)
        print(result)

    def read(self,table,query):
        result = self.fb.get(self.username+table,query)
        return result
    
    def update(self,table,uid,attribute,change):
        result = self.fb.put(self.username+table+'/'+uid,attribute,change)
        print(result)
        
    def delete(self,table,uid):
        result = self.fb.delete(self.username+table,'/'+uid)
        print(uid + 'has been deleted')
    
    
