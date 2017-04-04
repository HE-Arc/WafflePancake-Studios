from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit, HTML
from crispy_forms.bootstrap import InlineField


class GalleryForm(forms.Form):
    gallery_name = forms.CharField(max_length=50)

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        InlineField('gallery_name'),
        ButtonHolder(
            Submit('save_changes', 'Save changes', css_class="btn-primary"),
            HTML('<a class="btn btn-secondary" href={% url "galleries:index" %}>Cancel</a>')
        ),
    )


class ImageForm(forms.Form):
    image_name = forms.CharField(max_length=50)
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        InlineField('image_name'),
        InlineField('images'),
        ButtonHolder(
            Submit('save_changes', 'Save changes', css_class="btn-primary"),
            HTML('<a class="btn btn-secondary" href={% url "galleries:detail" pk=view.gallery.id %}>Cancel</a>')
        ),
    )

