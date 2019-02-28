from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

# Create your views here.
from .forms import ContactForm, ContactModel

# function that render the index.html along displaying saved contacts
def index(request):
    contacts = ContactModel.objects.all()
    context = {
        "contacts": contacts
    }
    return render(request, "m_f_appApp/index.html", context)

# function that allows user to edit a contact by redirecting the user to a seperate page with a form
def contact(request):

    newcontact = ContactForm(request.POST or None)
    print(newcontact)
    if newcontact.is_valid():
        print("Clean Data")
        newcontact.save()
        return redirect('index')
    context = {
        "newcontact": newcontact
    }
    return render(request, "m_f_appApp/contact.html", context)
# function that allows user to edit a contact
def edit_contact(request, id):
    edit = get_object_or_404(ContactModel, pk=id)
    edited = ContactForm(request.POST or None, instance=edit)
    if edited.is_valid():
        print("Clean Data")
        edited.save()
        return redirect('index')
    context = {
        "newcontact": edited
    }
    return render(request, "m_f_appApp/contact.html", context)
#function that deletes contacts
def delete_contact(request, id):
    deleteit = get_object_or_404(ContactModel, pk=id)
    if request.method == 'POST':
        deleteit.delete()
        return redirect('index')
    context = {
        "deleteuser": deleteit
    }
    return render(request, "m_f_appApp/delete.html", context)