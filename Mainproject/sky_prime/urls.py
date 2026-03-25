"""
URL configuration for sky_prime project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html"), name='index'),  

    # About Us Pages
    path('our-company/', TemplateView.as_view(template_name="our_company.html"), name='our_company'),
    path('core-values/', TemplateView.as_view(template_name="core_values.html"), name='core_values'),
    path('chairman-statement/', TemplateView.as_view(template_name="chairman_statement.html"), name='chairman_statement'),
    path('press-release/', TemplateView.as_view(template_name="press_release.html"), name='press_release'),
    path('event-gallery/', TemplateView.as_view(template_name="event_gallery.html"), name='event_gallery'),

    # Services Pages
    path('air-freight/', TemplateView.as_view(template_name="air_freight.html"), name='air_freight'),
    path('ocean-freight/', TemplateView.as_view(template_name="ocean_freight.html"), name='ocean_freight'),
    path('contract-logistics/', TemplateView.as_view(template_name="contract_logistics.html"), name='contract_logistics'),
    path('cargo-insurance/', TemplateView.as_view(template_name="cargo_insurance.html"), name='cargo_insurance'),
    path('custom-clearance/', TemplateView.as_view(template_name="custom_clearance.html"), name='custom_clearance'),
    path('warehousing/', TemplateView.as_view(template_name="warehousing.html"), name='warehousing'),
    path('packaging-services/', TemplateView.as_view(template_name="packaging_services.html"), name='packaging_services'),
    path('transportation-distribution/', TemplateView.as_view(template_name="transportation_distribution.html"), name='transportation_distribution'),
    path('project-heavy-lift/', TemplateView.as_view(template_name="project_heavy_lift.html"), name='project_heavy_lift'),
    path('distribution-logistics/', TemplateView.as_view(template_name="distribution_logistics.html"), name='distribution_logistics'),

    # Other Pages
    path('customer-care/', TemplateView.as_view(template_name="customer_care.html"), name='customer_care'),
    path('contact-us/', TemplateView.as_view(template_name="contact_us.html"), name='contact_us'),
    path('services/', TemplateView.as_view(template_name="services.html"), name='services'),
    path('about-us/', TemplateView.as_view(template_name="about_us.html"), name='about_us'),

]
