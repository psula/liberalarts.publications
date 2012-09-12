from five import grok
from zope import schema

from plone.directives import form, dexterity

from plone.app.textfield import RichText

from liberalarts.publications import _

from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName

from liberalarts.publications.publication import IPublication

class IPublicationsFolder(form.Schema):
    """A folder to contain all publications.
    """
    
    title = schema.TextLine(
            title=_(u"Folder Title"),
			description=_(u"Enter a name for the publications folder"),
        )
    
    description = schema.Text(
            title=_(u"A Short Summary about the contents of the folder."),
        )

class View(grok.View):
    grok.context(IPublicationsFolder)
    grok.require('zope2.View')

    def publications(self):
            
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')

        return catalog(object_provides=IPublication.__identifier__,
            path='/'.join(context.getPhysicalPath()),
            sort_on='sortable_title')