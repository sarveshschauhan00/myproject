from django import forms


GEEKS_CHOICES =(
    ("+", "Add"),
    ("-", "Sub"),
    ("*", "Mul"),
    ("/", "Div"),
)


class HomeForm(forms.Form):
    num1 = forms.IntegerField(required=False)
    num2 = forms.IntegerField(required=False)
    action = forms.ChoiceField(choices = GEEKS_CHOICES)