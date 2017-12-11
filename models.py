from google.appengine.api import users
from google.appengine.ext import ndb

class UserAlbums(ndb.Model):
    user = ndb.UserProperty(auto_current_user_add=True)
    photo = ndb.BlobProperty() #album = ndb.BlobProperty()
    
def get_useralbums(user_id=None):
	if not user_id:
		user = users.get_current_user()
		if not user:
			return None
		user_id = user.user_id()
	key = ndb.Key(‘UserAlbums’,user_id)
	useralbums = key.get()
	if not useralbums:
		useralbums = UserAlbums(id=user_id)
	return useralbums
