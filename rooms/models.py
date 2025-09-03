from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.panels import FieldPanel, MultiFieldPanel


class RoomsIndexPage(Page):
    intro = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]
    
    def get_context(self, request):
        context = super().get_context(request)
        context['room_pages'] = RoomPage.objects.child_of(self).live()
        return context


class RoomPage(Page):
    room_type = models.CharField(max_length=100, help_text="z.B. Einzelzimmer, Doppelzimmer, Suite")
    description = RichTextField()
    size_sqm = models.PositiveIntegerField(help_text="Zimmergröße in m²")
    max_guests = models.PositiveIntegerField(default=2)
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    
    amenities = StreamField([
        ('amenity', blocks.CharBlock(max_length=100)),
    ], blank=True, use_json_field=True)
    
    gallery = StreamField([
        ('image', ImageChooserBlock()),
    ], blank=True, use_json_field=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('room_type'),
        FieldPanel('description'),
        MultiFieldPanel([
            FieldPanel('size_sqm'),
            FieldPanel('max_guests'),
            FieldPanel('price_per_night'),
        ], heading="Zimmerdetails"),
        FieldPanel('main_image'),
        FieldPanel('amenities'),
        FieldPanel('gallery'),
    ]
