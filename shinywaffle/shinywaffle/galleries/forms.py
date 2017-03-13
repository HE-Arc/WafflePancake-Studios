from django import forms


class GalleryNewForm(forms.Form):
    gallery_name = forms.CharField(label='Gallery name', max_length=50)


class GalleryEditForm(forms.Form):
    pass

