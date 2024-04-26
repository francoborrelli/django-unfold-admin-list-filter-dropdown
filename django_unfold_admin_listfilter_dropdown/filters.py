from django.contrib.admin.filters import (
    SimpleListFilter,
    AllValuesFieldListFilter,
    ChoicesFieldListFilter,
    RelatedFieldListFilter,
    RelatedOnlyFieldListFilter
)


class SimpleDropdownFilter(SimpleListFilter):
    template = 'django_unfold_admin_listfilter_dropdown/dropdown_filter.html'


class DropdownFilter(AllValuesFieldListFilter):
    template = 'django_unfold_admin_listfilter_dropdown/dropdown_filter.html'


class ChoiceDropdownFilter(ChoicesFieldListFilter):
    template = 'django_unfold_admin_listfilter_dropdown/dropdown_filter.html'


class RelatedDropdownFilter(RelatedFieldListFilter):
    template = 'django_unfold_admin_listfilter_dropdown/dropdown_filter.html'


class RelatedOnlyDropdownFilter(RelatedOnlyFieldListFilter):
    template = 'django_unfold_admin_listfilter_dropdown/dropdown_filter.html'
