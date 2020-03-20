from googlesearch import search
from DBModel.model import UserSearchHistory


class ResponseHandler:
    """
    This class is responsible for sending response back to the user based on its messages
    """
    @classmethod
    def handle_request(cls, message):
        """
        this function read the message and reply with corresponding message
        if message starts with '!google' it search on google and save data in local db and reply with top 5 links
        if message starts with '!recent' it search on local db with the keyword and reply
        """
        message_text = str(message.content).lower()
        if message_text == 'hi':
            return 'hey'

        if message_text.startswith('!google'):
            result = list(search(message_text.split("!google")[1], tld="com", num=5, start=0, stop=5, pause=2))
            data = {
                'user_id': message.author,
                'keyword': message_text.split('!google')[1],
                'search_results': result
            }
            UserSearchHistory.create_record(data)
            return '\n'.join(result)

        if message_text.startswith('!recent'):
            return UserSearchHistory.get_search_history(message_text.split('!recent')[1], message.author)
