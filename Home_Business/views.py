from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Post
from .models import Portfolio
from .models import Bid
from .models import LogoContract
from .models import LogoCertificate
from .models import WebCertificate
from .models import ALogoContract
from .models import WebContract
from .models import AWebContract
from .models import GraphicContract
from .models import AGraphicContract
from .models import Apply
from .models import Accept
from .models import Employ
from .models import Feedback
from .models import LikhanapFeedback
from .models import Report
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.contrib import messages
from itertools import chain
from operator import attrgetter
User = get_user_model()




class PostListView(ListView):
    model = Post    
    template_name = 'Home_Business/home.html'   #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = [ '-dateposted']
    paginate_by = 5

    def get_queryset(self):
        
        request = self.request
        query = request.GET.get('q', '')
        posts_results= Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query) |
            Q(author__username__icontains=query) | Q(city__icontains=query) | Q(street__icontains=query) | Q(category__icontains=query))
        posts_count=Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query) |
            Q(author__username__icontains=query) | Q(city__icontains=query) | Q(street__icontains=query) | Q(category__icontains=query)).count()  
        try:
            if posts_count < 1:
                messages.warning(request, f'We did not found anything, try searching again.')
                return Post.objects.all()
        except:
            messages.warning(request, f'We did not found anything, try searching again.')
             
        else:
            return posts_results 

class ProjectListView(ListView):
    model = Post    
    template_name = 'Home_Business/project.html'   #<app>/<model>_<viewtype>.html
    context_object_name = 'projects'
    ordering = [ '-dateposted']
    paginate_by = 5

    def get_queryset(self):
        
        request = self.request
        query = request.GET.get('q', '')
        posts_results= Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query) |
            Q(author__username__icontains=query) | Q(city__icontains=query) | Q(street__icontains=query) | Q(category__icontains=query))
        posts_count=Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query) |
            Q(author__username__icontains=query) | Q(city__icontains=query) | Q(street__icontains=query) | Q(category__icontains=query)).count()  
        try:
            if posts_count < 1:
                messages.warning(request, f'We did not found anything, try searching again.')
                return Post.objects.all()
        except:
            messages.warning(request, f'We did not found anything, try searching again.')
             
        else:
            return posts_results
        
    

class LogoArtistListView(ListView):
    model = Portfolio    
    template_name = 'Home_Business/logoartist.html'   #<app>/<model>_<viewtype>.html
    context_object_name = 'logoartist'
    ordering = [ '-dateposted']
   
    

class LogoProjectListView(ListView):
    #model = Post    
    template_name = 'Home_Business/logoproject.html'   #<app>/<model>_<viewtype>.html
    context_object_name = 'logoproject'
    ordering = [ '-dateposted']
    def get_queryset(self):
        qs1 = Post.objects.filter(Q(category__icontains='LOGO')) #your first qs
        #you can add as many qs as you want
        queryset = sorted(chain(qs1),key=attrgetter('dateposted'),)
        return queryset

    
class BannerAdsArtistListView(ListView):
    model = Portfolio    
    template_name = 'Home_Business/banneradsartist.html'   #<app>/<model>_<viewtype>.html
    context_object_name = 'banneradsartist'
    ordering = [ '-dateposted']

class BannerAdsProjectListView(ListView):
    #model = Post    
    template_name = 'Home_Business/banneradsproject.html'   #<app>/<model>_<viewtype>.html
    context_object_name = 'banneradsproject'
    ordering = [ '-dateposted']
    def get_queryset(self):
        qs1 = Post.objects.filter(Q(category__icontains='BANNER ADS')) #your first qs
        #you can add as many qs as you want
        queryset = sorted(chain(qs1),key=attrgetter('dateposted'),)
        return queryset
class SignageArtistListView(ListView):
    model = Portfolio    
    template_name = 'Home_Business/signageartist.html'   #<app>/<model>_<viewtype>.html
    context_object_name = 'signageartist'
    ordering = [ '-dateposted']
 

class SignageProjectListView(ListView):
    #model = Post    
    template_name = 'Home_Business/signageproject.html'   #<app>/<model>_<viewtype>.html
    context_object_name = 'signageproject'
    ordering = [ '-dateposted']
    def get_queryset(self):
        qs1 = Post.objects.filter(Q(category__icontains='SIGNAGE')) #your first qs
        #you can add as many qs as you want
        queryset = sorted(chain(qs1),key=attrgetter('dateposted'),)
        return queryset

class WebDesignsArtistListView(ListView):
    model = Portfolio    
    template_name = 'Home_Business/webdesignsartist.html'   #<app>/<model>_<viewtype>.html
    context_object_name = 'webdesignsartist'
    ordering = [ '-dateposted']

class WebDesignsProjectListView(ListView):
    #model = Post    
    template_name = 'Home_Business/webdesignsproject.html'   #<app>/<model>_<viewtype>.html
    context_object_name = 'webdesignsproject'
    ordering = [ '-dateposted']
    def get_queryset(self):
        qs1 = Post.objects.filter(Q(category__icontains='WEB DESIGNS')) #your first qs
        #you can add as many qs as you want
        queryset = sorted(chain(qs1),key=attrgetter('dateposted'),)
        return queryset

class UserPostListView(ListView):
    model = Post    
    template_name = 'Home_Business/user_posts.html'   #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
     
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-dateposted')

class UserPostDetailView(DetailView, UpdateView):
    model = Post 
    fields = ['status']

class PostDetailView(DetailView):
    model = Post   

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
       
    fields = ['title', 'content', 'category', 'theme', 'rate', 'city', 'street', 'verified']

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post    
    fields = ['title', 'content', 'category', 'theme', 'city', 'street']   
    
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post   
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PortfolioListView(ListView):
    model = Portfolio    
    template_name = 'Home_Business/home.html'   #<app>/<model>_<viewtype>.html
    context_object_name = 'portfolios'
    ordering = [ '-dateposted']
    paginate_by = 5

    
    def get_queryset(self):
        
        request = self.request
        query = request.GET.get('q', '')
        Portfolio_results= Portfolio.objects.filter(Q(Expertise__icontains=query) | Q(Background__icontains=query) |
             Q(author__username__icontains=query) | Q(city__icontains=query) | Q(street__icontains=query) | Q(category__icontains=query))
        Portfolio_count=Portfolio.objects.filter(Q(Expertise__icontains=query) | Q(Background__icontains=query) |
             Q(author__username__icontains=query) | Q(city__icontains=query) | Q(street__icontains=query) | Q(category__icontains=query)).count()  
        try:
            if Portfolio_count < 1:
                messages.warning(request, f'We did not found anything, try searching again.')
                return Portfolio.objects.all()
        except:
            messages.warning(request, f'We did not found anything, try searching again.')
             
        else:
            return Portfolio_results
        

class PortfolioDetailView(DetailView):
    model = Portfolio   
class PortfolioCreateView(LoginRequiredMixin, CreateView):
   
    model = Portfolio   
    fields = ['Expertise', 'Background', 'category', 'theme', 'rate', 'image1', 'description1', 'image2', 'description2', 'image3', 'description3', 'city', 'street']
    
    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)

class PortfolioUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    
    model = Portfolio  
    fields = ['Expertise', 'Background', 'category', 'theme', 'rate', 'image1','image2','image3', 'city', 'street']   
    
    
    def test_func(self):
        portfolios = self.get_object()
        if self.request.user == portfolios.author:
            return True
        return False
class PortfolioDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Portfolio   
    success_url = '/'
    def test_func(self):
        portfolios = self.get_object()
        if self.request.user == portfolios.author:
            return True
        return False

class BidCreateView(LoginRequiredMixin, CreateView):
    model = Bid    
    fields = ['title', 'content','image', 'category', 'theme', 'rate', 'artist_username', 'city', 'street' ]

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)

class LogoContractCreateView(LoginRequiredMixin, CreateView):
    model = LogoContract    
    fields = ['businessname', 'ownername', 'address', 'image' ]

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)

class ALogoContractCreateView(LoginRequiredMixin, CreateView):
    model = ALogoContract    
    fields = ['artistname', 'address', 'image' ]

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)


class LogoContractDetailView(DetailView):
    model = LogoContract 

class LogoContractUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = LogoContract    
    fields = ['businessname', 'ownername', 'address', 'image' ]
    
    def test_func(self):
        apply = self.get_object()
        if self.request.user == apply.author:
            return True
        return False
class ALogoContractDetailView(DetailView):
    model = ALogoContract 


class ALogoContractUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ALogoContract    
    fields = ['artistname', 'address', 'image' ]
    
    def test_func(self):
        apply = self.get_object()
        if self.request.user == apply.author:
            return True
        return False

class LogoContractDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = LogoContract   
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False 

class ALogoContractDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ALogoContract   
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False 

class WebContractCreateView(LoginRequiredMixin, CreateView):
    model = WebContract    
    fields = ['businessname', 'ownername', 'address', 'image' ]

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)

class WebContractDetailView(DetailView):
    model = WebContract 

class WebContractUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = WebContract    
    fields = ['businessname', 'ownername', 'address', 'image' ]
    
    def test_func(self):
        apply = self.get_object()
        if self.request.user == apply.author:
            return True
        return False

class WebContractDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = WebContract   
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False 

class AWebContractCreateView(LoginRequiredMixin, CreateView):
    model = AWebContract    
    fields = ['artistname', 'address', 'image' ]

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)

class AWebContractDetailView(DetailView):
    model = AWebContract 

class AWebContractUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = AWebContract    
    fields = ['artistname', 'address', 'image' ]
    
    def test_func(self):
        apply = self.get_object()
        if self.request.user == apply.author:
            return True
        return False

class AWebContractDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = AWebContract   
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False 

class GraphicContractCreateView(LoginRequiredMixin, CreateView):
    model = GraphicContract    
    fields = ['businessname', 'ownername', 'address', 'image' ]

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)

class GraphicContractDetailView(DetailView):
    model = GraphicContract 

class GraphicContractUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = GraphicContract    
    fields = ['businessname', 'ownername', 'address', 'image' ]
    
    def test_func(self):
        apply = self.get_object()
        if self.request.user == apply.author:
            return True
        return False

class GraphicContractDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = GraphicContract   
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False 

class AGraphicContractCreateView(LoginRequiredMixin, CreateView):
    model = AGraphicContract    
    fields = ['artistname', 'address', 'image' ]
    
    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)

class AGraphicContractDetailView(DetailView):
    model = AGraphicContract 

class AGraphicContractUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = AGraphicContract    
    fields = ['artistname', 'address', 'image' ]
    
    def test_func(self):
        apply = self.get_object()
        if self.request.user == apply.author:
            return True
        return False

class AGraphicContractDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = AGraphicContract   
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False 

class BidsListView(ListView):
    model = Bid    
    template_name = 'Home_Business/bid.html'   #<app>/<model>_<viewtype>.html
    context_object_name = 'bids'
    ordering = [ '-dateposted']
    paginate_by = 5

class BidDetailView(DetailView):
    model = Bid 

class Bid2DetailView(DetailView, UpdateView):
    model = Bid 
    fields = ['status']

class BidUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Bid    
    fields = ['title', 'content','image', 'category', 'theme', 'rate', 'artist_username', 'city', 'street']   
    
    
    def test_func(self):
        bid = self.get_object()
        if self.request.user == bid.author:
            return True
        return False
class BidDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Bid   
    success_url = '/'
    def test_func(self):
        bid = self.get_object()
        if self.request.user == bid.author:
            return True
        return False

class ApplyDetailView(DetailView):
    model = Apply   
class ApplyCreateView(LoginRequiredMixin, CreateView):
    model = Apply   
    fields = ['Expertise', 'Background', 'category', 'theme', 'rate', 'Business_username', 'image1','image2','image3', 'city', 'street']

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)
        

class ApplyUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Apply    
    fields = ['Expertise', 'Background', 'category', 'theme', 'rate', 'Business_username', 'image1','image2','image3', 'city', 'street']   
    
    
    def test_func(self):
        apply = self.get_object()
        if self.request.user == apply.author:
            return True
        return False

class ApplyDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Apply   
    success_url = '/'
    def test_func(self):
        apply = self.get_object()
        if self.request.user == apply.author:
            return True
        return False

class ApplyListView(ListView):
    model = Apply    
    template_name = 'Home_Business/apply.html'   #<app>/<model>_<viewtype>.html
    context_object_name = 'applies'
    ordering = [ '-dateposted']
    paginate_by = 5

class AcceptDetailView(DetailView):
    model = Accept 

class AcceptListView(ListView):
    model = Accept    
    template_name = 'Home_Business/accept.html'   #<app>/<model>_<viewtype>.html
    context_object_name = 'accepts'
    ordering = [ '-dateposted']
    paginate_by = 5

class AcceptCreateView(LoginRequiredMixin, CreateView):
    model = Accept   
    fields = [ 'Message','Business_username']

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)

class AcceptUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Accept    
    fields = ['Message','Business_username']   
    
    
    def test_func(self):
        accept = self.get_object()
        if self.request.user == accept.author:
            return True
        return False

class AcceptDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Accept   
    success_url = '/'
    def test_func(self):
        accept = self.get_object()
        if self.request.user == accept.author:
            return True
        return False


class EmployDetailView(DetailView):
    model = Employ 

class EmployListView(ListView):
    model = Employ    
    template_name = 'Home_Business/employ.html'   #<app>/<model>_<viewtype>.html
    context_object_name = 'employs'
    ordering = [ '-dateposted']
    paginate_by = 5

class EmployCreateView(LoginRequiredMixin, CreateView):
    model = Employ   
    fields = [ 'Message','artist_username']

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)
        

class EmployUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Employ    
    fields = ['Message','artist_username']   
    
    
    def test_func(self):
        employ = self.get_object()
        if self.request.user == employ.author:
            return True
        return False

class EmployDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Employ   
    success_url = '/'
    def test_func(self):
        employ = self.get_object()
        if self.request.user == employ.author:
            return True
        return False

class LikhanapFeedbackDetailView(DetailView):
    model = LikhanapFeedback 

class LikhanapFeedbackListView(ListView):
    model = LikhanapFeedback    
    template_name = 'Home_Business/homestatus2.html'   #<app>/<model>_<viewtype>.html
    context_object_name = 'likhanapfeedbacks'
    ordering = [ '-dateposted']
    paginate_by = 5

class LikhanapFeedbackCreateView(LoginRequiredMixin, CreateView):
    model = LikhanapFeedback   
    fields = ['Feedback']

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)
        

class LikhanapFeedbackUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = LikhanapFeedback    
    fields = ['Feedback']   
    
    
    def test_func(self):
        likhanapfeedback = self.get_object()
        if self.request.user == likhanapfeedback.author:
            return True
        return False

class LikhanapFeedbackDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = LikhanapFeedback   
    success_url = '/'
    def test_func(self):
        likhanapfeedback = self.get_object()
        if self.request.user == likhanapfeedback.author:
            return True
        return False

class ReportDetailView(DetailView):
    model = Report 

class ReportListView(ListView):
    model = Report    
    template_name = 'Home_Business/report.html'   #<app>/<model>_<viewtype>.html
    context_object_name = 'report'
    ordering = [ '-dateposted']
    paginate_by = 5

class ReportCreateView(LoginRequiredMixin, CreateView):
    model = Report   
    fields = ['Report', 'artist_username']

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)
        

class ReportUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Report    
    fields = ['Report', 'artist_username']   
    
    
    def test_func(self):
        report = self.get_object()
        if self.request.user == report.author:
            return True
        return False

class ReportDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Report   
    success_url = '/'
    def test_func(self):
        report = self.get_object()
        if self.request.user == report.author:
            return True
        return False


class FeedbackCreateView(LoginRequiredMixin, CreateView):
    model = Feedback   
    fields = [ 'Comment','rating', 'artist_username']

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)

class FeedbackDetailView(DetailView):
    model = Feedback 

class FeedbackListView(ListView):
    model = Feedback       
    template_name = 'Home_Business/feedbacks.html'   #<app>/<model>_<viewtype>.html
    context_object_name = 'feedback'
    ordering = [ '-dateposted']
    paginate_by = 5
    
    def get_queryset(self):
        
        request = self.request
        query = request.GET.get('q', ' ')
        Feedback_results= Feedback.objects.filter(Q(artist_username__icontains=query))
        Feedback_count=Feedback.objects.filter(Q(artist_username__icontains=query)).count()  
        try:
            if Feedback_count < 1:
                messages.warning(request, f'')
                
        except:
            messages.warning(request, f'')
             
        else:
            return Feedback_results

class LogoCertificateCreateView(LoginRequiredMixin, CreateView):
    model = LogoCertificate    
    fields = ['businessname', 'ownername', 'artistname', 'logo' ]

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)

class LogoCertificateDetailView(DetailView):
    model = LogoCertificate 

class LogoCertificateUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = LogoCertificate    
    fields = ['businessname', 'ownername', 'artistname', 'logo' ]
    
    def test_func(self):
        apply = self.get_object()
        if self.request.user == apply.author:
            return True
        return False

class LogoCertificateDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = LogoCertificate   
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False 

class WebCertificateCreateView(LoginRequiredMixin, CreateView):
    model = WebCertificate    
    fields = ['businessname', 'ownername', 'artistname', 'link' ]

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)

class WebCertificateDetailView(DetailView):
    model = WebCertificate 

class WebCertificateUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = WebCertificate    
    fields = ['businessname', 'ownername', 'artistname', 'link' ]
    
    def test_func(self):
        apply = self.get_object()
        if self.request.user == apply.author:
            return True
        return False

class WebCertificateDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = WebCertificate   
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False 

def categories(request):
    return render(request, 'Home_Business/categories.html',{'title': 'Categories'})
def howitworks(request):
    return render(request, 'Home_Business/howitworks.html',{'title': 'howitworks'})
def FAQ(request):
    return render(request, 'Home_Business/FAQ.html',{'title': 'FAQ'})
def about(request):
    return render(request, 'Home_Business/about.html',{'title': 'About'})
def help(request):
    return render(request, 'Home_Business/helpcenter.html',{'title': 'Help'})
def view(request):
    return render(request, 'Home_Business/profile_view.html',{'title': 'View'})
def terms(request):
    return render(request, 'Home_Business/terms.html',{'title': 'Terms'})
def homestatus(request):
    return render(request, 'Home_Business/homestatus.html',{'title': 'HomeStatus'})
def prehome(request):
    return render(request, 'Home_Business/prehome.html',{'title': 'Home'})
def home(request):
    return render(request, 'Home_Business/home.html',{'title': 'Likhanap'})
def registration(request):
    return render(request, 'Home_Business/registration.html',{'title': 'registration'})
def findproject(request):
    return render(request, 'Home_Business/findproject.html',{'title': 'findproject'})
def findartists(request):
    return render(request, 'Home_Business/findartists.html',{'title': 'findartists'})
def prescreen(request):
    return render(request, 'Home_Business/prescreen.html',{'title': 'prescreen'})
def subscribe(request):
    return render(request, 'Home_Business/subscribe.html',{'title': 'subscribe'})
def subscribe2(request):
    return render(request, 'Home_Business/subscribe2.html',{'title': 'subscribe2'})
def contractcategory(request):
    return render(request, 'Home_Business/contractcategory.html',{'title': 'contractcategory'})
def contractlist(request):
    return render(request, 'Home_Business/contractlist.html',{'title': 'contractlist'})
def certcategory(request):
    return render(request, 'Home_Business/certcategory.html',{'title': 'certcategory'})
def certificatelist(request):
    return render(request, 'Home_Business/certificatelist.html',{'title': 'certificatelist'})