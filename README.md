# django-unfold-admin-list-filter-dropdown

[![PyPI version](https://badge.fury.io/py/django-unfold-admin-list-filter-dropdown.svg)](https://badge.fury.io/py/django-unfold-admin-list-filter-dropdown)

> [!NOTE]  
> This version is compatible with [django-unfold](https://github.com/unfoldadmin/django-unfold).

A Django admin filter implementation that renders as a dropdown.

If you have more than ten values for a field that you want to filter by in
Django admin, the filtering sidebar gets long, cluttered and hard to use.

This app contains the `DropdownFilter` class that renders as a drop-down in the
filtering sidebar to avoid this problem.

# Usage

Install:

```sh
pip install django-unfold-admin-list-filter-dropdown
```

Enable in `settings.py`:

```py
INSTALLED_APPS = (
    ...
    'django_unfold_admin_listfilter_dropdown',
    ...
)

```

Use in `admin.py`:

```py
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter

class EntityAdmin(admin.ModelAdmin):
    ...
    list_filter = (
        # for ordinary fields
        ('a_charfield', DropdownFilter),
        # for choice fields
        ('a_choicefield', ChoiceDropdownFilter),
        # for related fields
        ('a_foreignkey_field', RelatedDropdownFilter),
    )
```

Example of a custom filter that uses the provided template:

```py
class CustomFilter(SimpleListFilter):
    template = 'django_unfold_admin_listfilter_dropdown/dropdown_filter.html'

    def lookups(self, request, model_admin):
        ...

    def queryset(self, request, queryset):
        ...
```
