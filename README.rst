====================================
Django app name translation in admin
====================================

This application allows translation of application names in the admin interface.

Works with Django 1.3.1.

Configuration and usage
-----------------------

1. Put ``app_name_translation_in_admin`` into your ``INSTALLED_APPS`` **before**
   ``django.contrib.admin``::

        INSTALLED_APPS = (
           ...
           'app_name_translation_in_admin',
           'django.contrib.admin',
           ...
        )

2. Define the app names and mark them for translations. Use cap first names.

  ::

    from django.utils.translation import ugettext_lazy as _ 

    _(u'Auth') 
    _(u'Sites') 

Notes
-----

Related tickets:

* `Ticket #3591 add support for custom app_label and verbose_name<https://code.djangoproject.com/ticket/3591>`_.
  When this ticket is resolved, this application would be excessive.

* `Ticket #10436 - Application names i18n in the admin app broken<https://code.djangoproject.com/ticket/10436>`_

* this `thread <https://groups.google.com/d/msg/django-users/-Py-JeMyfF0/lm7lgzlyWu8J>`_

