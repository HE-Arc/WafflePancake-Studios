from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit, HTML
from crispy_forms.bootstrap import InlineField


class GalleryNewForm(forms.Form):
    gallery_name = forms.CharField(max_length=50)

    helper = FormHelper()
    helper.form_class = 'form-inline'
    helper.layout = Layout(
        InlineField('gallery_name'),
        ButtonHolder(
            Submit('save_changes', 'Save changes', css_class="btn-primary"),
            HTML('<a class="btn btn-secondary" href={% url "galleries:index" %}>Cancel</a>')  # not sure about this
        ),
    )


class GalleryEditForm(forms.Form):
    image_name = forms.CharField(max_length=50)
    images = forms.FileField()

    helper = FormHelper()
    helper.form_class = 'form-inline'
    helper.layout = Layout(
        InlineField('image_name'),
        InlineField('images'),
        ButtonHolder(
            Submit('save_changes', 'Save changes', css_class="btn-primary"),
            HTML('<a class="btn btn-secondary" href={% url "galleries:index" %}>Cancel</a>')  # not sure about this
        ),

    )

