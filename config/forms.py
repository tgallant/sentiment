from django import forms
 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import FormActions
  

class SentimentForm(forms.Form):
     text = forms.CharField(
         widget = forms.Textarea(),
     )

     helper = FormHelper()
     helper.form_action = 'analysis'
     helper.layout = Layout(
         FormActions(
             Field('text', rows="10", css_class='input-xlarge'),
             Submit('analysis', 'Submit')
         )
     )

class SubmitRedirect(forms.Form):
    helper = FormHelper()
    helper.form_action = 'home'
    helper.layout = Layout(
        FormActions(
            Submit('redirect', 'Go Back')
        )
    )
