Django Contact Form
===================

A very simple contact form for a Django website. The form is emailed to one or
more email addresses upon submission.


Requires
--------

Django >= 1.4


Installation
------------

Install the latest release using ``pip``::

    pip install quix.django.contact

Or install the development version using ``git``::

    git clone https://github.com/Quixotix/quix.django.contact.git
    
Add ``quix.django.contact`` to ``INSTALLED_APPS`` in ``settings.py``.


Basic Usage
-----------

Specify the email addresses which will recieve the contact form message in
``settings.py``::

    CONTACT_EMAILS = ('somebody@localhost', 'another@localhost')

Include ``quix.django.contact.urls`` in ``urls.py``::

    urlpatterns = patterns('',
        # ... 
        url(r'^contact/', include('quix.django.contact.urls')),
        # ...
    )

Create the 3 templates (see examples in the next section): 

* ``contact/form.html`` - The contact form with ``form`` in the context.
* ``contact/success.html`` - Page the form redirects to when successful.
* ``contact/email.txt`` - The text template for the email.

Link to the contact form in a template using the ``"contact-form"`` named URL 
pattern::

    <a href="{% url contact-form %}">Contact</a>


Templates
---------

**contact/form.html**::

    {% extends "base.html" %}
    {% block content %}
      <h1>Contact</h1>
      <form action="." method="post">
        {% csrf_token %}
        {{ form.non_field_errors }}
        {{ form.as_p }}
        <input type="submit" value="Send" />
      </form>
    {% endblock %}

**contact/success.html**::

    {% extends "base.html" %}
    {% block content %}
      <h1>Your message has been sent.</h1>
    {% endblock %}

**contact/email.txt**::

    From: {{ name }} {{ email }}

    {{ message }}

    ---
    This message was sent via the website contact form.

Settings
--------

The following settings can be set in ``settings.py`` for the contact form. Only
``CONTACT_EMAILS`` is required, which is a tuple or list of email addresses to
which the contact form should be sent.

======================== ============================================ ========
Setting                  Default                                      Required
======================== ============================================ ========
CONTACT_EMAILS                                                        Yes
CONTACT_FORM_CLASS       ``"quix.django.contact.forms.ContactForm"``  No
CONTACT_FORM_TEMPLATE    ``"contact/form.html"``                      No
CONTACT_SUCCESS_TEMPLATE ``"contact/success.html"``                   No
CONTACT_EMAIL_TEMPLATE   ``"contact/email.txt"``                      No
======================== ========================== ================= ========

