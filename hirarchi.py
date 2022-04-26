class User:
    """
    User class, represent user with name, password, is admin or not for Determine his permissions.
    :param(string) user_name: Full name.
    :param(string) password: User password for login.
    :param(bool) admin: Permissions options, different permissions between admin to simple user.
    """
    def __init__(self, user_name, password, admin=False):
        self.user_name = user_name
        self.__password = password
        self.admin = admin

    def is_admin(self):
        """
        Check the type of the user(admin).
        :return:(bool) If the user is admin or simple user.
        """
        if self.admin:
            return True
        return False


class File:
    """

    :param file_name:
    :param file_type:
    """
    def __init__(self, file_name, file_type):
        self.name = file_name
        self.file_type = file_type


class Directory(File):
    """
    Directory class, , Inheritance from File. represent Directory that can contain list of 1)Directory 2)Text File
        3)Binary file.
    """
    def __init__(self, file_name, file_type, list_files=[]):
        super().__init__(file_name, file_type)
        self.list_files = list_files

    def add_file(self, file):
        """
        Add new file to the list of the directory.
        :param file: File to add to this directory.
        """
        self.list_files.append(file)

    def get_files(self):
        """
        Get files inside the directory.
        :return:(List) List of all files include in this directory.
        """
        return self.list_files


class FileContent(File):
    """
    Class of Content file, Inheritance from File. represent text file or binary file.
    :param(string) file_name:File name.
    :param(string) file_type: File class.
    :param(int) file_weight: Weight of the file in kilobytes
    :param(string) file_content: Content of the file
    :param(User) user_owner:  User data that create the file.
    """
    def __init__(self, file_name, file_type, file_weight, file_content, user_owner):
        super().__init__(file_name, file_type)
        self.file_weight = file_weight
        self.file_content = file_content
        self.user_owner = user_owner

    def read(self, user):
        """
        Check if the user have permissions, If the user is the owner of the file or he is 'Admin' we will get access to
        the content.
        :param user: User class.
        :return: File content if the user have permissions, otherwise return None
        """
        if user == self.user_owner or user.admin:
            return self.file_content
        return None

    def __str__(self):
        """
        Function for print the file content.
        :return: File content
        """
        return self.file_content


class FileText(FileContent):
    """
    Class of Text file. Inheritance from FileContent and add count method.
    :param(string) file_name:File name.
    :param(string) file_type: File class.
    :param(int) file_weight: Weight of the file in kilobytes
    :param(string) file_content: Content of the file
    :param(User) user_owner:  User data that create the file.
    """
    def __init__(self, file_name, file_type, file_weight, file_content, user_owner):
        super().__init__(file_name, file_type, file_weight, file_content, user_owner)

    def count(self, search_string):
        """
        :param(string) search_string:
        :return:(int) How many times the search string is in trhe
        """
        return self.file_content.count(search_string)


class FileBinary(FileContent):
    """
    File Binary class, Representing photos.
    :param(string) file_name:File name.
    :param(string) file_type: File class.
    :param(int) file_weight: Weight of the file in kilobytes
    :param(string) file_content: Content of the file
    :param(User) user_owner:  User data that create the file.
    :param(int)height: height pixels of the photo
    :param(int) weight: weight pixels of the photo
    """
    def __init__(self, file_name, file_type, file_weight, file_content, user_owner, height, weight):
        super().__init__(file_name, file_type, file_weight, file_content, user_owner)
        self.height = height
        self.weight = weight

    def get_dimensions (self):
        """
        Get the Height and weight number of pixles in the photo.
        :return: Height of the picture, weight of the picture.
        """
        return self.height, self.weight


if __name__ == '__main__':
    user1 = User("Orel Aviad", "orel007", admin=False)
    user2 = User("Leel Aviad", "leel007", admin=True)
    user3 = User("Itai Aviad", "leel007", admin=False)
    file1 = FileBinary("file1", FileBinary, 100, "1010101101010", user1, 20, 20)
    file2 = FileText("file1", FileText, 200, "This my file 2", user1)
    dir1 = Directory("direct1", "Directory", [file1, file2])
    print(file1.read(user1))  # Read by user owner
    print(file2.read(user1))  # Read by user owner
    print(file2.read(user2))  # Read by user Admin
    print(file2.read(user3))  # Read by not user owner and not Admin
    print(file1)  # __str__ of ContentFile
    print(file2)  # __str__ of ContentFile



