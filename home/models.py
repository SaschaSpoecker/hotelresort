from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.panels import FieldPanel, MultiFieldPanel


class HomePage(Page):
    hero_title = models.CharField(max_length=200, blank=True, help_text="Haupttitel für die Homepage")
    hero_subtitle = models.CharField(max_length=300, blank=True, help_text="Untertitel für die Homepage")
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    
    # Special Offers Section
    offer_title = models.CharField(max_length=200, blank=True, help_text="z.B. 'Herbst-Special'")
    offer_description = RichTextField(blank=True, help_text="Beschreibung des Angebots")
    offer_cta_text = models.CharField(max_length=100, blank=True, default="Jetzt buchen", help_text="Text für Call-to-Action Button")
    offer_cta_url = models.URLField(blank=True, help_text="Link für CTA Button")
    offer_background_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Hintergrundbild für die Angebots-Section"
    )
    offer_valid_until = models.DateField(blank=True, null=True, help_text="Gültig bis (optional)")
    
    intro_text = RichTextField(blank=True, help_text="Einführungstext")
    
    features = StreamField([
        ('feature', blocks.StructBlock([
            ('title', blocks.CharBlock(max_length=100)),
            ('description', blocks.TextBlock()),
            ('icon', blocks.CharBlock(max_length=50, help_text="Font Awesome Icon Name")),
        ])),
    ], blank=True, use_json_field=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('hero_title'),
        FieldPanel('hero_subtitle'),
        FieldPanel('hero_image'),
        MultiFieldPanel([
            FieldPanel('offer_title'),
            FieldPanel('offer_description'),
            FieldPanel('offer_cta_text'),
            FieldPanel('offer_cta_url'),
            FieldPanel('offer_background_image'),
            FieldPanel('offer_valid_until'),
        ], heading="Special Offers Section"),
        FieldPanel('intro_text'),
        FieldPanel('features'),
    ]
