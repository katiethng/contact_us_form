from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .forms import ContactForm

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
    
        if form.is_valid():
            department = form.cleaned_data['department']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            # Include the 'department' in the email subject
            subject = f'Contact Form Submission - {department}'

            html = render_to_string('contact/emails/contactform.html', {
                'department': department,
                'name': name,
                'email': email,
                'content': content
            })

            send_mail(subject, 'This is the message', 'katiethng@gmail.com', ['kimthu21299@gmail.com'], html_message=html)
            return redirect('index')
    else:
        form = ContactForm()

    return render(request, 'contact/index.html', {
        'form': form
    })
