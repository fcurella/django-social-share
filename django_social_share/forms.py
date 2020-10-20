from django import forms
from .models import Product


class EmailForm(forms.Form):

    def __init__(self, *arg, product_pk, **kwargs):
        super(forms.Form, self).__init__(*arg, **kwargs)
        product = Product.objects.get(pk=product_pk)
        self.fields["message"] = forms.CharField(widget=forms.Textarea, label="Message", initial="J'ai trouver ce nouveau produit' "+product.name+" 'et j'ai penser qu'il pourrai t'interesser : http://127.0.0.1:8000"+product.get_absolute_url())

    from_email = forms.EmailField(required=True, label="Votre email",)
    to_email = forms.EmailField(required=True, label="Email du déstinataire")
    subject = forms.CharField(required=True, label="Sujet", )
    message = forms.CharField(widget=forms.Textarea, label="Message", initial="http://127.0.0.1:8000" )