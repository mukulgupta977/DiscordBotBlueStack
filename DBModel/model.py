from pymodm import MongoModel, fields
from pymongo.write_concern import WriteConcern
from datetime import datetime
import re


class UserSearchHistory(MongoModel):
    """
        Model used for storing search results of a user
    """
    user_id = fields.CharField(required=True)
    keyword = fields.CharField(required=True)
    created_on = fields.DateTimeField(required=True, default=datetime.now())
    search_results = fields.ListField(required=True)

    class Meta:
        write_concern = WriteConcern(j=True)
        connection_alias = 'app'

    @classmethod
    def create_record(cls, request):
        """
        this method inserts the search result into the database of a user
        """
        cls(**request).save()

    @classmethod
    def get_search_history(cls, keyword, author):
        """
        this method fetch the search history records of a user for a particular keyword
        """
        final_records = []
        regex = re.compile('{keyword}'.format(keyword=keyword), re.IGNORECASE)
        print(author)
        records = cls.objects.raw(
            {
                'user_id': str(author).strip(),
                'keyword': {
                    '$regex': regex
                }
            }
        )
        for record in records:
            final_records = final_records + record.search_results

        records = '\n'.join(final_records)

        return records
