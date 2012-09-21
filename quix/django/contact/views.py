from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from quix.django.contact.forms import ContactForm
from django.views.generic.edit import FormView

class ContactView(FormView):
    template_name = getattr(settings, 'CONTACT_FORM_TEMPLATE', 'contact/form.html')
    form_class = ContactForm
    success_url = reverse_lazy("contact-success")

    def form_valid(self, form):
        form.send_email()
        return super(ContactView, self).form_valid(form)
