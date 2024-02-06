from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse


# Create your views here.
def contact(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')

            # Enviamos correo y redireccionamos
            # email = EmailMessage(
            #     "Cafettiera: A new message",
            #     f'From {name} <{email}>\n\nWrites:\n\n{content}',
            #     'no-reply@inbox.mailtrap.io',
            #     ['alejandrobueno92@hotmail.com'],
            #     reply_to=[email]
            # )
            # email.send()
            return redirect(reverse('contact') + '?ok')

    return render(request, 'contact/contact.html', {'forms': contact_form})
