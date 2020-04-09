from django.db import models
from wagtail.core.models import Page
from ckeditor.fields import RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel, FieldRowPanel
from wagtail.search import index
from modelcluster.fields import ParentalKey
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.contrib.settings.models import BaseSetting, register_setting


class HomePage(Page):
	body = RichTextField(blank=True)
	meta_titlee = models.CharField(max_length=30,blank=True)
	no_index_field = models.CharField(max_length=30,blank=True)
	meta_description = models.CharField(max_length=255,blank=True)
	image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
	content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),FieldPanel('meta_description'),FieldPanel('no_index_field'),FieldPanel('meta_titlee'),ImageChooserPanel('image'),]

@register_setting
class SocialMediaSettings(BaseSetting):
    facebook_pixel = models.CharField(max_length=9000,blank=True)
    google_tag = models.CharField(max_length=9000,blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('facebook_pixel', classname="full"),]

class ContactUsPage(Page):
	body = RichTextField(blank=True)
	content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),]

class FormField(AbstractFormField):
    page = ParentalKey('FormPage', on_delete=models.CASCADE, related_name='form_fields')


class FormPage(AbstractEmailForm):
    intro = RichTextField(blank=True)
    no_index_field = models.CharField(max_length=30,blank=True)
    thank_you_text = RichTextField(blank=True)
    meta_description = models.CharField(max_length=255,blank=True)
    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro', classname="full"),
        FieldPanel('no_index_field', classname="full"),
        FieldPanel('meta_description', classname="full"),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]
