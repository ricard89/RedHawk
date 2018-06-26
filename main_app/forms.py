from django import forms
from main_app.models import Tag


class TagForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(TagForm, self).__init__(*args, **kwargs)
        self.fields['device'].queryset = Device.objects.filter(owner=user)

    class Meta():
        model = Tag
        fields = ['num_ID', 'name_ID', 'value', 'unit', 'type', 'widget', 'arguments']
