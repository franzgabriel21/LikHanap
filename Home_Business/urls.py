"""LikHanap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import (PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView,
PortfolioDetailView, PortfolioCreateView, PortfolioUpdateView, PortfolioDeleteView, PortfolioListView, 
ProjectListView, LogoArtistListView, BannerAdsArtistListView, SignageArtistListView, WebDesignsArtistListView,  
LogoProjectListView, BannerAdsProjectListView, SignageProjectListView, WebDesignsProjectListView,
BidCreateView, BidsListView, BidDetailView, BidUpdateView, BidDeleteView,
ApplyCreateView, ApplyListView, ApplyDetailView, ApplyUpdateView, ApplyDeleteView,
AcceptDetailView, AcceptListView, AcceptCreateView, AcceptUpdateView, AcceptDeleteView,
EmployListView, EmployDetailView, EmployCreateView, EmployUpdateView, EmployDeleteView,
FeedbackCreateView, FeedbackDetailView, FeedbackListView, Bid2DetailView, UserPostDetailView, LogoContractCreateView, ALogoContractCreateView, 
LogoContractDetailView, ALogoContractDetailView, LogoContractUpdateView, ALogoContractUpdateView, LogoContractDeleteView, ALogoContractDeleteView, WebContractCreateView, WebContractDetailView, WebContractUpdateView, WebContractDeleteView,
AWebContractCreateView, AWebContractDetailView, AWebContractUpdateView, AWebContractDeleteView,
GraphicContractCreateView, GraphicContractDetailView, GraphicContractUpdateView, GraphicContractDeleteView,
AGraphicContractCreateView, AGraphicContractDetailView, AGraphicContractUpdateView, AGraphicContractDeleteView, 
LogoCertificateCreateView, LogoCertificateDetailView, LogoCertificateUpdateView, LogoCertificateDeleteView,
WebCertificateCreateView, WebCertificateDetailView, WebCertificateUpdateView, WebCertificateDeleteView,
LikhanapFeedbackListView, LikhanapFeedbackDetailView, LikhanapFeedbackCreateView, LikhanapFeedbackUpdateView, LikhanapFeedbackDeleteView,
ReportListView, ReportDetailView, ReportCreateView, ReportUpdateView, ReportDeleteView)
 
from . import views


urlpatterns = [
    path('posts/', PostListView.as_view(), name = 'LikHanap-Business'),

    path('projects/', ProjectListView.as_view(), name = 'LikHanap-Projects'),

    path('logoartist/', LogoArtistListView.as_view(), name = 'Logo-Artist'),

    path('logoproject/', LogoProjectListView.as_view(), name = 'Logo-Project'),

    path('banneradsartist/', BannerAdsArtistListView.as_view(), name = 'Bannerads-Artist'),

    path('banneradsproject/', BannerAdsProjectListView.as_view(), name = 'Bannerads-Project'),

    path('signageartist/', SignageArtistListView.as_view(), name = 'Signage-Artist'),

    path('signageproject/', SignageProjectListView.as_view(), name = 'Signage-Project'),

    path('webdesignsartist/', WebDesignsArtistListView.as_view(), name = 'WebDesigns-Artist'),

    path('webdesignsproject/', WebDesignsProjectListView.as_view(), name = 'WebDesigns-Project'),

    path('portfolios/', PortfolioListView.as_view(), name = 'LikHanap-Freelance'),
        
    path('user/<str:username>', UserPostListView.as_view(), name = 'user-posts'),
   
    path('user/<int:pk>/', UserPostDetailView.as_view(), name = 'UserPost-Detail'),
    
    #
    path('portfolios/<int:pk>/', PortfolioDetailView.as_view(), name = 'Portfolio-Detail'),
    #
    
    path('post/new/', PostCreateView.as_view(), name = 'Post-Create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'Post-Detail'),
  
    #
    path('portfolios/new/', PortfolioCreateView.as_view(), name = 'Portfolio-Create'),
    #
    
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'Post-Update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'Post-Delete'),

    #
    path('portfolios/<int:pk>/update/', PortfolioUpdateView.as_view(), name = 'Portfolio-Update'),
    path('portfolios/<int:pk>/delete/', PortfolioDeleteView.as_view(), name = 'Portfolio-Delete'),
    #
    path('bid/new/', BidCreateView.as_view(), name = 'Bid-Create'),

    path('bids/', BidsListView.as_view(), name = 'LikHanap-Bids'),

    path('bid/<int:pk>/', BidDetailView.as_view(), name = 'Bid-Detail'),
    path('bid2/<int:pk>/', Bid2DetailView.as_view(), name = 'Bid2-Detail'),

    path('bid/<int:pk>/update/', BidUpdateView.as_view(), name = 'Bid-Update'),
    path('bid/<int:pk>/delete/', BidDeleteView.as_view(), name = 'Bid-Delete'),
    #
    path('apply/new/', ApplyCreateView.as_view(), name = 'Apply-Create'),

    path('applies/', ApplyListView.as_view(), name = 'LikHanap-Apply'),

    path('apply/<int:pk>/', ApplyDetailView.as_view(), name = 'Apply-Detail'),

    path('apply/<int:pk>/update/', ApplyUpdateView.as_view(), name = 'Apply-Update'),
    path('apply/<int:pk>/delete/', ApplyDeleteView.as_view(), name = 'Apply-Delete'),
   
    #
    path('accepts/', AcceptListView.as_view(), name = 'Accept'),
    path('accepts/<int:pk>/', AcceptDetailView.as_view(), name = 'Accept-Detail'),
    path('accepts/new/', AcceptCreateView.as_view(), name = 'Accept-Create'),
    path('accept/<int:pk>/update/', AcceptUpdateView.as_view(), name = 'Accept-Update'),
    path('accept/<int:pk>/delete/', AcceptDeleteView.as_view(), name = 'Accept-Delete'),
    #

    path('employs/', EmployListView.as_view(), name = 'Employ'),
    path('employs/<int:pk>/', EmployDetailView.as_view(), name = 'Employ-Detail'),
    path('employs/new/', EmployCreateView.as_view(), name = 'Employ-Create'),
    path('employ/<int:pk>/update/', EmployUpdateView.as_view(), name = 'Employ-Update'),
    path('employ/<int:pk>/delete/', EmployDeleteView.as_view(), name = 'Employ-Delete'),
    #

    path('homestatus2/', LikhanapFeedbackListView.as_view(), name = 'LikhanapFeedback'),
    path('likhanapfeedbacks/<int:pk>/', LikhanapFeedbackDetailView.as_view(), name = 'LikhanapFeedback-Detail'),
    path('likhanapfeedbacks/new/', LikhanapFeedbackCreateView.as_view(), name = 'LikhanapFeedback-Create'),
    path('likhanapfeedback/<int:pk>/update/', LikhanapFeedbackUpdateView.as_view(), name = 'LikhanapFeedback-Update'),
    path('likhanapfeedback/<int:pk>/delete/', LikhanapFeedbackDeleteView.as_view(), name = 'LikhanapFeedback-Delete'),

    #    

    path('reports/', ReportListView.as_view(), name = 'Report'),
    path('reports/<int:pk>/', ReportDetailView.as_view(), name = 'Report-Detail'),
    path('reports/new/', ReportCreateView.as_view(), name = 'Report-Create'),
    path('report/<int:pk>/update/', ReportUpdateView.as_view(), name = 'Report-Update'),
    path('report/<int:pk>/delete/', ReportDeleteView.as_view(), name = 'Report-Delete'),

    #
    path('feedback/new/', FeedbackCreateView.as_view(), name = 'Feedback-Create'),
    path('feedback/', FeedbackListView.as_view(), name = 'Feedback'),
    path('feedback/<int:pk>/', FeedbackDetailView.as_view(), name = 'Feedback-Detail'),

    path('about/', views.about, name = 'LikHanap-About'),
    path('help/', views.help, name = 'Help-Center'),
    path('view', views.view, name = 'Profile-View'),
    path('terms/', views.terms, name = 'LikHanap-Terms'),
    path('homestatus/', views.homestatus, name = 'LikHanap-HomeStatus'),
    path('', views.prehome, name='prehome'),
    path('categories/', views.categories, name='categories'),
    path('howitworks/', views.howitworks, name='howitworks'),
    path('FAQ/', views.FAQ, name='FAQ'),
    path('registration/', views.registration, name='registration'),
    path('findproject/', views.findproject, name='findproject'),
    path('findartists/', views.findartists, name='findartists'),
    path('prescreen/', views.prescreen, name='prescreen'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('subscribe2/', views.subscribe2, name='subscribe2'),
    #
    path('logocontract/new/', LogoContractCreateView.as_view(), name = 'LogoContract-Create'),
    path('alogocontract/new/', ALogoContractCreateView.as_view(), name = 'ALogoContract-Create'),
    path('logocertificate/new/', LogoCertificateCreateView.as_view(), name = 'LogoCertificate-Create'),
    path('webcertificate/new/', WebCertificateCreateView.as_view(), name = 'WebCertificate-Create'),

    path('logocontract/<int:pk>/', LogoContractDetailView.as_view(), name = 'LogoContract-Detail'),
    path('alogocontract/<int:pk>/', ALogoContractDetailView.as_view(), name = 'ALogoContract-Detail'),
    path('logocertificate/<int:pk>/', LogoCertificateDetailView.as_view(), name = 'LogoCertificate-Detail'),
    path('webcertificate/<int:pk>/', WebCertificateDetailView.as_view(), name = 'WebCertificate-Detail'),

    path('logocontract/<int:pk>/update/', LogoContractUpdateView.as_view(), name = 'LogoContract-Update'),
    path('alogocontract/<int:pk>/update/', ALogoContractUpdateView.as_view(), name = 'ALogoContract-Update'),
    path('logocertificate/<int:pk>/update/', LogoCertificateUpdateView.as_view(), name = 'LogoCertificate-Update'),
    path('webcertificate/<int:pk>/update/', WebCertificateUpdateView.as_view(), name = 'WebCertificate-Update'),

    path('logocontract/<int:pk>/delete/', LogoContractDeleteView.as_view(), name = 'LogoContract-Delete'),
    path('alogocontract/<int:pk>/delete/', ALogoContractDeleteView.as_view(), name = 'ALogoContract-Delete'),
    path('logocertificate/<int:pk>/delete/', LogoCertificateDeleteView.as_view(), name = 'LogoCertificate-Delete'),
    path('webcertificate/<int:pk>/delete/', WebCertificateDeleteView.as_view(), name = 'WebCertificate-Delete'),

    #
    path('webcontract/new/', WebContractCreateView.as_view(), name = 'WebContract-Create'),
    path('awebcontract/new/', AWebContractCreateView.as_view(), name = 'AWebContract-Create'),

    path('webcontract/<int:pk>/', WebContractDetailView.as_view(), name = 'WebContract-Detail'),
    path('awebcontract/<int:pk>/', AWebContractDetailView.as_view(), name = 'AWebContract-Detail'),

    path('webcontract/<int:pk>/update/', WebContractUpdateView.as_view(), name = 'WebContract-Update'),
    path('awebcontract/<int:pk>/update/', AWebContractUpdateView.as_view(), name = 'AWebContract-Update'),

    path('webcontract/<int:pk>/delete/', WebContractDeleteView.as_view(), name = 'WebContract-Delete'),
    path('awebcontract/<int:pk>/delete/', AWebContractDeleteView.as_view(), name = 'AWebContract-Delete'),

    #
    path('graphiccontract/new/', GraphicContractCreateView.as_view(), name = 'GraphicContract-Create'),
    path('agraphiccontract/new/', AGraphicContractCreateView.as_view(), name = 'AGraphicContract-Create'),

    path('graphiccontract/<int:pk>/', GraphicContractDetailView.as_view(), name = 'GraphicContract-Detail'),
    path('agraphiccontract/<int:pk>/', AGraphicContractDetailView.as_view(), name = 'AGraphicContract-Detail'),

    path('graphiccontract/<int:pk>/update/', GraphicContractUpdateView.as_view(), name = 'GraphicContract-Update'),
    path('agraphiccontract/<int:pk>/update/', AGraphicContractUpdateView.as_view(), name = 'AGraphicContract-Update'),
   
    path('graphiccontract/<int:pk>/delete/', GraphicContractDeleteView.as_view(), name = 'GraphicContract-Delete'),
    path('agraphiccontract/<int:pk>/delete/', AGraphicContractDeleteView.as_view(), name = 'AGraphicContract-Delete'),
   
    #
    path('contractcategory/', views.contractcategory, name='contractcategory'),
    path('certcategory/', views.certcategory, name='certcategory'),
    path('contractlist/', views.contractlist, name='contractlist'),
    path('certificatelist/', views.certificatelist, name='certificatelist'),
]
