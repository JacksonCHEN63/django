from django.db import models

class MyModelName(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')
    ...

    # Metadata
    #這邊是去決定數據返回的順序
    class Meta:
        ordering = ['-my_field_name']

    # Methods
    # 個人理解就是他這邊算是一個寫變數的地方，也許html來抓這邊的變數，
    def get_absolute_url(self):
         """Returns the url to access a particular instance of MyModelName."""
         return reverse('model-detail-view', args=[str(self.id)])
    
    #定義標準python的類方法__str__，為每個物件返回一個人類可讀的字符串
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        # Create your models here.
        record = MyModelName(my_field_name="Instance #1")
        record.save()
        print(record.id) #should return 1 for the first record.
        print(record.my_field_name) # should print 'Instance #1'
        
        # Change record by modifying the fields, then calling save().
        record.my_field_name = "New Instance Name"
        record.save()
        return self.field_name
