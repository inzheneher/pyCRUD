import psycopg2


class Connection:

    def __init__(self, conf):
        self.conf = conf
        try:
            self.connection = psycopg2.connect(user=self.conf.get('user'),
                                               password=self.conf.get('password'),
                                               host=self.conf.get('host'),
                                               port=self.conf.get('port'),
                                               database=self.conf.get('database'))
        except (Exception, psycopg2.Error) as error:
            print("Failed create connection to db", error)

    def get_connection(self):
        return self.connection
