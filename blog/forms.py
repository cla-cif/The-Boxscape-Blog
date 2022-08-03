from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, HTML  # noqa
from django_summernote.widgets import SummernoteWidget
from crispy_forms.bootstrap import StrictButton
from .models import Comment, Post


# CREATE NEW COMMENT
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control',
                                          'rows': 4}),
        }


# EDIT COMMENT
class EditCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control',
                                          'rows': 4}),
        }


# CREATE POST
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'tags', 'list_image', 'excerpt', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'tags': forms.TextInput(attrs={'class': 'form-control'}),
            'list_image': forms.TextInput(attrs={'class': 'form-control'}),
            'excerpt': forms.Textarea(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            # 'body': forms.CharField(widget=SummernoteWidget(attrs={'class': 'form-control'})),
        }


# EDIT POST
class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'list_image', 'excerpt', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'list_image': forms.TextInput(attrs={'class': 'form-control'}),
            'excerpt': forms.Textarea(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            # 'body': forms.CharField(widget=SummernoteWidget(attrs={'class': 'form-control'})),
        }


# CONTACT THE ADMIN
class ContactForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-vertical'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-12'

        self.helper.layout = Layout(
            'first_name',
            'last_name',
            'email_address',
            'message',
            Div(
                StrictButton('Send', css_class='btn btn-lg', type='submit'),
                css_class='d-grid col-6 mx-auto pt-4 pb-4'
            )
        )

    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email_address = forms.EmailField(max_length=150)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)
