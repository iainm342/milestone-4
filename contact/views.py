from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ContactForm


def contact(request):

    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():

            messages.success(request, 'Message sent!')
            return redirect('home')

    context = {
        'form': form,
    }

    return render(request, 'contact/contact.html', context)
