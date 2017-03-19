from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, InlineField


class GalleryNewForm(forms.Form):
    gallery_name = forms.CharField(max_length=50)

    helper = FormHelper()
    helper.form_class = 'form-inline'
    helper.layout = Layout(
        InlineField('gallery_name'),
        FormActions(
            Submit('save_changes', 'Save changes', css_class="btn-primary"),
            Submit('cancel', 'Cancel', css_class='btn-secondary'),
        )
    )


class GalleryEditForm(forms.Form):
    pass

