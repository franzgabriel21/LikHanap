from django.contrib import admin
from.models import Post
from.models import VerifiedPost
from.models import Portfolio
from .models import Bid
from .models import Apply
from .models import Accept
from .models import Employ
from.models import Feedback

admin.site.register(VerifiedPost)
admin.site.register(Post)
admin.site.register(Portfolio)
admin.site.register(Bid)
admin.site.register(Apply)
admin.site.register(Accept)
admin.site.register(Employ)
admin.site.register(Feedback)
admin.site.site_header = 'LikHanap Admin'