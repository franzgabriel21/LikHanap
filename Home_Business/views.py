from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Post
from .models import Portfolio
from .models import Bid
from .models import Apply
from .models import Accept
from .models import Employ
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.contrib import messages

User = get_user_model()


def home(request):
    posts= Post.objects.all()
    query = request.GET.get('q')
    if query:
        posts= Post.objects.filter(title__icontains=query)
    
    context=    {
        
        'posts': posts,

    }
    return render(request, 'Home_Business/home.html', context)

class PostListView(ListView):
    model = Post    
    template_name = 'Home_Business/home.html'   #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = [ '-dateposted']
    paginate_by = 5
    
    def get_queryset(self):
        
        request = self.request
        query = request.GET.get('q', ' ')
        posts_results= Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query) |
            Q(author__username__icontains=query) | Q(location__icontains=query) | Q(category__icontains=query))
        posts_count=Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query) |
            Q(author__username__icontains=query) | Q(location__icontains=query)| Q(category__icontains=query)).count()  
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
        query = request.GET.get('q', ' ')
        posts_results= Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query) |
            Q(author__username__icontains=query) | Q(location__icontains=query) | Q(category__icontains=query))
        posts_count=Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query) |
            Q(author__username__icontains=query) | Q(location__icontains=query)| Q(category__icontains=query)).count()  
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
    paginate_by = 5

class LogoProjectListView(ListView):
    model = Post    
    template_name = 'Home_Business/logoproject.html'   #<app>/<model>_<viewtype>.html
    context_object_name = 'logoproject'
    ordering = [ '-dateposted']
    paginate_by = 5

class TarpArtistListView(ListView):
    model = Portfolio    
    template_name = 'Home_Business/tarpartist.html'   #<app>/<model>_<viewtype>.html
    context_object_name = 'tarpartist'
    ordering = [ '-dateposted']
    paginate_by = 5

class TarpProjectListView(ListView):
    model = Post    
    template_name = 'Home_Business/tarpproject.html'   #<app>/<model>_<viewtype>.html
    context_object_name = 'tarpproject'
    ordering = [ '-dateposted']
    paginate_by = 5


class AdArtistListView(ListView):
    model = Portfolio    
    template_name = 'Home_Business/adartist.html'   #<app>/<model>_<viewtype>.html
    context_object_name = 'adartist'
    ordering = [ '-dateposted']
    paginate_by = 5

class AdProjectListView(ListView):
    model = Post    
    template_name = 'Home_Business/adproject.html'   #<app>/<model>_<viewtype>.html
    context_object_name = 'adproject'
    ordering = [ '-dateposted']
    paginate_by = 5

class InviArtistListView(ListView):
    model = Portfolio    
    template_name = 'Home_Business/inviartist.html'   #<app>/<model>_<viewtype>.html
    context_object_name = 'inviartist'
    ordering = [ '-dateposted']
    paginate_by = 5

class InviProjectListView(ListView):
    model = Post 
    template_name = 'Home_Business/inviproject.html'   #<app>/<model>_<viewtype>.html
    context_object_name = 'inviproject'
    ordering = [ '-dateposted']
    paginate_by = 5

class InteriorArtistListView(ListView):
    model = Portfolio    
    template_name = 'Home_Business/interiorartist.html'   #<app>/<model>_<viewtype>.html
    context_object_name = 'interiorartist'
    ordering = [ '-dateposted']
    paginate_by = 5

class InteriorProjectListView(ListView):
    model = Post 
    template_name = 'Home_Business/interiorproject.html'   #<app>/<model>_<viewtype>.html
    context_object_name = 'interiorproject'
    ordering = [ '-dateposted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post    
    template_name = 'Home_Business/user_posts.html'   #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
     
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-dateposted')


class PostDetailView(DetailView):
    model = Post   
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
       
    fields = ['title', 'content','image', 'category', 'location']

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post    
    fields = ['title', 'content','image', 'category', 'location']   
    
    
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


def home(request):
    context=    {
        
        'portfolios': Post.objects.all()

    }
    return render(request, 'Home_Business/home.html', context)

class PortfolioListView(ListView):
    model = Portfolio    
    template_name = 'Home_Business/home.html'   #<app>/<model>_<viewtype>.html
    context_object_name = 'portfolios'
    ordering = [ '-dateposted']
    paginate_by = 5

    
    def get_queryset(self):
        
        request = self.request
        query = request.GET.get('q', ' ')
        Portfolio_results= Portfolio.objects.filter(Q(Expertise__icontains=query) | Q(Background__icontains=query) |
             Q(author__username__icontains=query) | Q(location__icontains=query) | Q(category__icontains=query))
        Portfolio_count=Portfolio.objects.filter(Q(Expertise__icontains=query) | Q(Background__icontains=query) |
             Q(author__username__icontains=query) | Q(location__icontains=query) | Q(category__icontains=query)).count()  
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
    fields = ['Expertise', 'Background', 'category','image1','image2','image3', 'location']
    
    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)

class PortfolioUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    
    model = Portfolio  
    fields = ['Expertise', 'Background', 'category','image1','image2','image3', 'location']   
    
    
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
    fields = ['title', 'content','image', 'category', 'location', 'artist_username']

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)
        
    

class BidsListView(ListView):
    model = Bid    
    template_name = 'Home_Business/bid.html'   #<app>/<model>_<viewtype>.html
    context_object_name = 'bids'
    ordering = [ '-dateposted']
    paginate_by = 5

class BidDetailView(DetailView):
    model = Bid 

class BidUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Bid    
    fields = ['title', 'content','image', 'category', 'location', 'artist_username']   
    
    
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
    fields = ['Expertise', 'Background', 'category','image1','image2','image3', 'location', 'Business_username']

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)
        

class ApplyUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Apply    
    fields = ['Expertise', 'Background', 'category','image1','image2','image3', 'location', 'Business_username']   
    
    
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


def about(request):
    return render(request, 'Home_Business/about.html',{'title': 'About'})
def terms(request):
    return render(request, 'Home_Business/terms.html',{'title': 'Terms'})
def homestatus(request):
    return render(request, 'Home_Business/homestatus.html',{'title': 'HomeStatus'})
def prehome(request):
    return render(request, 'Home_Business/prehome.html',{'title': 'Home'})

    