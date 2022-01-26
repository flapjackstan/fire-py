import pyrebase

config = {}


firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
    
cloud_path = 'images/test-1.jpg'
path_local = 'data/images/2020-08-03_184156.jpg-0.jpg'

# local to cloud     
#storage.child(cloud_path).put(path_local)

# cloud to local
storage.child(cloud_path).download('output/images/test-1.jpg')