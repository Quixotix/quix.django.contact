from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView
from django.utils.importlib import import_module

# import contact form class based on value in settings.py
full_class = getattr(settings, 'CONTACT_FORM_CLASS', 'quix.django.contact.forms.ContactForm')
module_name = '.'.join(full_class.split('.')[0:-1])
module = import_module(module_name)
class_instance = getattr(module, full_class.split('.')[-1])

class ContactView(FormView):
    template_name = getattr(settings, 'CONTACT_FORM_TEMPLATE', 'contact/form.html')
    form_class = class_instance
    success_url = reverse_lazy("contact-success")

    def form_valid(self, form):
        form.send_email()
        return super(ContactView, self).form_valid(form)
