from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render
from django_social_share.forms import EmailForm


class ProductListView(ListView):

    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProductDetailView(DetailView):
    template_name = 'product/product_detail.html'
    model = Product

    def get(self, request, pk):
        form = EmailForm(product_pk=pk)
        product = Product.objects.get(pk=pk)
        return render(request, self.template_name, {'form': form, 'object': product})

    def post(self, request, pk):
        form = EmailForm(request.POST, product_pk=pk)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            to_email = [from_email, form.cleaned_data['to_email']]
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, to_email)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return self.get_success_url()


    def get_success_url(self):
         return HttpResponse('<div class="alert alert-success" role="alert">Email envoyé avec sucés</div>')




