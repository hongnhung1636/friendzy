from django.db import models
import ast
import datetime
# Create your models here.


class ListField(models.TextField):
    __metaclass__ = models.SubfieldBase
    description = "Stores a python list"
    
    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)
    
    def to_python(self, value):
        if not value:
            value = []
        if isinstance(value, list):
            return value
        return ast.literal_eval(value)
    
    def get_prep_value(self, value):
        if value is None:
            return value
        return unicode(value)
    
    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)




class User(models.Model):
    facebook_id = models.CharField(max_length=200)
    friends = ListField()
    status = models.CharField(max_length=200)
    status_time = models.DateTimeField('date published')
    
    def login(self, userid, facebook_friends):
        try:
            myuser = User.objects.get(facebook_id=userid)
        except User.DoesNotExist:
            myuser = User()
            myuser.save()
        #user exists
        myuser.friends = facebook_friends
        return myuser.get_friend_statuses()
    
    def get_friend_statuses(self):
        statuses = []
        for friend in self.friends:
            try:
                myuser = User.objects.get(facebook_id=userid)
                statuses += [myuser.facebook_id, myuser.get_status()]
            except User.DoesNotExist:
                #do nothing
                print("user " + str(self.facebook_id) + " needs to relogin to update friendlist")
        return filter(lambda x: x[1] != None, statuses)
    
    def set_status(self, userid, status, time):
        self.status = status
        status_time = self.parse_date(time)
        try:
            myuser = User.objects.get(facebook_id=userid)
            # return matching statuses
            statuses = myuser.get_friend_statuses()
            out = []
            for fid, fstatus in statuses:
                if self.matches(status, fstatus):
                    out.append([status, fstatus])
            return out
        except User.DoesNotExist:
            #do nothing
            print("user " + str(userid) + " not found - status not set")
    
    def get_status(self):
        """
        returns status if valid, else returns None
        """
        now = datetime.datetime.now()
        statustime = self.status_time
        if now-statustime < datetime.timedelta(minutes=-1):
            return self.status
        return None
    
    @staticmethod
    def matches(string1, string2):
        """
        returns if string1 matches with string2
        more complex matching algorithm yet to come
        """
        return string1 == string2
    
    @staticmethod
    def parse_date(time):
        return time
    
    




