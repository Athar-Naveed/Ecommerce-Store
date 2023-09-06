from django import forms
from .models import ConversationMessage
class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('content',)

    def __init__(self,*args,**kwargs):
        super(ConversationMessageForm,self).__init__(*args,**kwargs)

        self.fields['content'].widget.attrs['class'] = 'container w-[75%] mx-auto my-5 grid border-2 p-3 rounded-xl'
        self.fields['content'].widget.attrs['placeholder'] = "Your message here..."
    
  
