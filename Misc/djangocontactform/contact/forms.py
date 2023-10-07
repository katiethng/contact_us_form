from django import forms

DEPARTMENT_CHOICES = (
    ("City Hall", "City Hall"),
    ("Police Department", "Police Department"),
    ("Department of Public Works", "Department of Public Works"),
    ("Assessing Department", "Assessing Department"),
    ("Building Department", "Building Department"),
)

class ContactForm(forms.Form):
    department = forms.ChoiceField(
        choices=DEPARTMENT_CHOICES,
        label="Department",
        required=True,
    )
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)
