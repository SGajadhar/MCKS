# blue prints are imported 
# explicitly instead of using *
from .user import user_views
from .index import index_views
from .auth import auth_views
# from .testing import testing_views
#from .routine import routine_views
from .login import login_views




views = [user_views, index_views, auth_views,login_views] 
# blueprints must be added to this list