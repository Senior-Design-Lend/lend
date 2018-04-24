import datetime
from haystack import indexes
from items.models import Item

class ItemIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    # Can also search by these fields...
    condition = indexes.CharField(model_attr='condition')
    category = indexes.CharField(model_attr='category')
    zipcode = indexes.CharField(model_attr='zipCode')
    owner = indexes.CharField(model_attr='owner')
    update_date = indexes.DateTimeField(model_attr='update_date')
    # NOT WORKING....
    # content_auto = indexes.EdgeNgramField(model_attr='content')
    
    def get_model(self):
        return Item

    def index_queryset(self, using=None):
        '''Used when the entire index for model is updated.'''
        return self.get_model().objects.filter(update_date__lte=datetime.datetime.now())
