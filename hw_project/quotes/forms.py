# from django import forms
#
# from .models import Quote
#
#
# class NoteForm(forms.ModelForm):
#
#     # name = forms.CharField(min_length=5, max_length=50, required=True, widget=forms.TextInput())
#     # description = forms.CharField(min_length=10, max_length=150, required=True, widget=forms.TextInput())
#     quote = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     tags = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     author = forms.CharField(min_length=5, max_length=50, required=True, widget=forms.TextInput())
#     created_at = forms.CharField(min_length=5, max_length=50, required=True, widget=forms.TextInput())
#
#     class Meta:
#         model = Quote
#         fields = ['name', 'description']
#         exclude = ['tags']


from django import forms
from .models import Author, Quote


class AuthorForm(forms.ModelForm):
    fullname = forms.CharField(min_length=5, max_length=50, required=True, widget=forms.TextInput())
    born_date = forms.DateField()
    born_location = forms.CharField(min_length=3, max_length=50, required=True, widget=forms.TextInput())
    description = forms.CharField(max_length=250, widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']


class QuoteForm(forms.ModelForm):
    quote = forms.CharField()
    tags = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(QuoteForm, self).__init__(*args, **kwargs)
        # Додайте варіанти вибору автора
        self.fields['author'].queryset = Author.objects.all()

    def clean_quote(self):
        quote = self.cleaned_data.get('quote')
        # Перевірка довжини цитати
        if len(quote) < 10:
            raise forms.ValidationError("Цитата занадто коротка")
        return quote

    class Meta:
        model = Quote
        fields = ['quote', 'tags', 'author']