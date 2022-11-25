from settings import DATABASE
from mongoengine import connect

class Connection:
    '''
    This is used to create and close clients to databases available
    '''

    def __enter__(self, *args, **kwargs):
        '''
        This method creates clients
        '''

        # Mongo Client
        self.mongo_client = connect(
            db=DATABASE.MONGO.DB,
            port=int(DATABASE.MONGO.PORT),
            username=DATABASE.MONGO.USERNAME,
            host=DATABASE.MONGO.HOST,
            password=DATABASE.MONGO.PASSWORD
        )

    def __exit__(self, *args, **kwargs):
        '''
        This method closes clients
        '''
        # self.mongo_client.close() # Mongo Client
        pass

def connect_to_db(func):
    '''
    This is a decorator used to connect api functions or methods connect to dbs
    '''
    def inner(*args, **kwargs):
        with Connection():
            func(*args, **kwargs)
    return inner
