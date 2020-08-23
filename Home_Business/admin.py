from django.contrib import admin
from.models import Post
from.models import Portfolio
from .models import Bid
from .models import Apply
from .models import Accept
from .models import Employ
from.models import Feedback
from.models import LikhanapFeedback
from .models import LogoContract
from .models import LogoCertificate
from .models import WebCertificate
from .models import ALogoContract
from .models import WebContract
from .models import AWebContract
from .models import GraphicContract
from .models import AGraphicContract


admin.site.register(Post)
admin.site.register(Portfolio)
admin.site.register(Bid)
admin.site.register(Apply)
admin.site.register(Accept)
admin.site.register(Employ)
admin.site.register(Feedback)
admin.site.register(LikhanapFeedback)
admin.site.register(LogoContract)
admin.site.register(LogoCertificate)
admin.site.register(WebCertificate)
admin.site.register(ALogoContract)
admin.site.register(AWebContract)
admin.site.register(WebContract)
admin.site.register(GraphicContract)
admin.site.register(AGraphicContract)

admin.site.site_header = 'LikHanap Admin'