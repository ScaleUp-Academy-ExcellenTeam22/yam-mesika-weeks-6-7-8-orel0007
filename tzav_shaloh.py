class PostOffice:
    """A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False):
        """Send a message to a recipient.

        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param str message_body: The body of the message.
        :param urgent: The urgency of the message.
        :type urgent: bool, optional
        :return: The message ID, auto incremented number.
        :rtype: int
        :raises KeyError: if the recipient does not exist.
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
            # I added this attribute to the class.
            'is_read': False,
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, username, num_massages=-1):
        """Get user name and number of wanted massages when default number is all.
           read the number of requested massages, update the massage as read and return list of all those massages.
        :param username:(str) user name
        :param num_massages:(int) number of massages.
        :return:list of last massages that weren't read yet.
        """
        last_massages = list()
        if num_massages < 0 or num_massages > len(self.boxes[username]):
            num_massages = len(self.boxes[username])
        for massage in self.boxes[username][:num_massages]:
            if massage['is_read'] is False:
                last_massages.append(massage['body'])
                massage['is_read'] = True
        return last_massages

    def read_massage(self, id_massage, user_name):
        self.boxes[user_name][id_massage]["is_read"] = True
        return self.boxes[user_name][id_massage]

    def search_inbox(self, username, search_string):
        """
        Search substring inside each massage and return list with all the massage that contain this requested
            substring.
        :param username:(str)
        :param search_string:(str) requested string contain in the massages.
        :return:list of all massages contain the search string in the title or in the body.
        """
        return [massage for massage in self.boxes[username] if search_string in massage]
#add commnet for new pull request

if __name__ == "__main__":
    p = PostOffice(["Orel", "Itai"])
    p.send_message("Orel", "Itai", "I hope you will like my coding.")
    p.send_message("Orel", "Itai", "Please give me a good grade.")
    p.send_message("Itai", "Orel", "I will give you 100 for this program, great job!!.")
    print(p.read_inbox("Itai"))
    print(p.read_inbox("Itai"))
    print(p.read_inbox("Orel"))

