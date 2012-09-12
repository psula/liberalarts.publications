from five import grok
from zope import schema

from plone.directives import form, dexterity

from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage

from liberalarts.publications import _

class IPublication(form.Schema):
    """A publication.
    """
    
    title = schema.TextLine(
            title=_(u"Publication Title"),
			description=_(u"Enter the title of the book, the book chapter or article."),
        )

    citation = schema.Text(
	        title=_(u"Citation"),
	        description=_(u"Enter the citation for the publication.  You can also copy and past the citation from an existing document."),
	        required=True
	        )
	
    description = schema.Text(
	        title=_(u"A Short Summary about the Book or article"),
	        )

    purchase = schema.TextLine(
			title=_(u"Purchase Link"),
			description=_(u"If you would like to link to another site, such as amazon, where the publication can be purchased, copy and paste the url here."),
			required=False
			)
    
    picture = NamedImage(
            title=_(u"Publication Image"),
            description=_(u"Please upload an image"),
            required=False,
        )
