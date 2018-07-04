import crowd
import logging.handlers
from django.conf import settings
from django.contrib.auth.models import User, Group

crowd_logger = logging.getLogger(__name__)


class ClientException(Exception):
    def __init__(self, msg):
        super(ClientException, self).__init__(msg)


class UserException(Exception):
    def __init__(self, username):
        super(UserException, self).__init__()
        self.username = username


class InvalidUser(UserException):
    def __init__(self, username):
        super(InvalidUser, self).__init__(username)

    def __str__(self):
        return "User '%s' is not valid Crowd user" % self.username


class AuthFailed(UserException):
    def __init__(self, username):
        super(AuthFailed, self).__init__(username)

    def __str__(self):
        return "Failed to authenticate user '%s' in Crowd" % self.username


class CrowdRestBackend(object):
    """Atlassian Crowd Authentication Backend using REST API"""

    crowdClient = None

    def check_client_and_app_authentication(self):
        """Create a client to access Crowd."""
        try:
            if self.crowdClient is None:
                self.crowdClient = CrowdRestClient()
        except:
            crowd_logger.exception("Create Crowd client failed")

    def create_or_update_user(self, user_id):
        """Create or update django user of given identifier"""
        user, created = User.objects.get_or_create(username=user_id)
        saveUser = False

        if created:
            user.set_unusable_password()
            saveUser = True

        if getattr(settings, "AUTH_CROWD_ALWAYS_UPDATE_USER", True):
            self.sync(user)
            saveUser = True

        if getattr(settings, "AUTH_CROWD_ALWAYS_UPDATE_GROUPS", True):
            self.sync_groups(user)
            saveUser = True

        if saveUser:
            user.save()

        return user

    def authenticate(self, username=None, password=None):
        """Try to authenticate given user and return a User instance on success."""
        user = None
        try:
            crowd_logger.debug("Authenticate user '%s'..." % username)
            self.check_client_and_app_authentication()
            self.crowdClient.authenticate(username, password)
            user = self.create_or_update_user(username)
            crowd_logger.debug("Authenticated user '%s' successfully." % user.username)
        except:
            crowd_logger.info("Authenticate failed '%s'" % username)
        return user

    def sync(self, user):
        """Sync given user instance with data from crowd."""
        usrData = self.crowdClient.get_user(user.username)
        if "first-name" in usrData:
            user.first_name = usrData["first-name"]
        if "last-name" in usrData:
            user.last_name = usrData["last-name"]
        if "email" in usrData:
            user.email = usrData["email"]
        if "active" in usrData:
            user.is_active = usrData["active"]

    def sync_groups(self, user):
        data = self.crowdClient.get_user_groups(user.username)

        group_names = data

        superuser_groups = getattr(settings, "AUTH_CROWD_SUPERUSER_GROUP", None)
        if isinstance(superuser_groups, str):
            superuser_groups = superuser_groups.replace(' ', '').split(',')

        if len(set(superuser_groups).intersection(group_names)) > 0:
            user.is_superuser = True
        else:
            user.is_superuser = False

        staff_groups = getattr(settings, "AUTH_CROWD_STAFF_GROUP", None)
        if isinstance(staff_groups, str):
            staff_groups = staff_groups.replace(' ', '').split(',')

        if len(set(staff_groups).intersection(group_names)) > 0:
            user.is_staff = True
        else:
            user.is_staff = False

        if getattr(settings, "AUTH_CROWD_CREATE_GROUPS", False):
            group_objs = [Group.objects.get_or_create(name=g)[0] for g in group_names]
        else:
            group_objs = Group.objects.all()
            group_objs = filter(lambda x: x.name in group_names, group_objs)

        user.groups.set(group_objs)

    def get_user(self, user_id):
        """Return User instance of given identifier."""
        user = None
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            crowd_logger.exception("User not found")
        return user


class CrowdRestClient(object):
    def __init__(self):
        try:
            self._client = crowd.CrowdServer(
                settings.AUTH_CROWD_SERVER_REST_URI,
                settings.AUTH_CROWD_APPLICATION_USER,
                settings.AUTH_CROWD_APPLICATION_PASSWORD
            )
            self.connect()
        except:
            crowd_logger.exception("Initialize Crowd client failed")

    def connect(self):
        """Connect to Crowd."""
        try:
            crowd_logger.debug("Connecting to %s..." % self._client.crowd_url)
            if not self._client.auth_ping():
                raise Exception()
            crowd_logger.debug("Connected to Crowd.")
        except:
            crowd_logger.exception("Failed to connect to Crowd")
            raise ClientException("Failed to connect to Crowd")

    def authenticate(self, username, password, maxRetry=3):
        """Authenticate given user via Crowd."""
        try:
            crowd_logger.debug("Authenticating '%s'..." % username)

            usrData = self._client.auth_user(username=username, password=password)
            if usrData is not None:
                crowd_logger.debug("Authenticated '%s' successfully." % usrData["display-name"])
                return
        except:
            crowd_logger.exception("Unknown exception")

        # Force auth to fail
        raise AuthFailed(username)

    def get_user(self, username):
        """Query for given user and return dict of user fields from Crowd."""
        try:
            crowd_logger.debug("Fetching details of '%s'..." % username)
            user = self._client.get_user(username)
            if user is not None:
                return user
        except:
            crowd_logger.exception("Failed to fetch user data from Crowd")
        raise InvalidUser(username)

    def get_user_groups(self, username):
        """Query for groups of given user and return dict of group fields from Crowd."""
        try:
            crowd_logger.debug("Fetching groups of '%s'..." % username)
            groups = self._client.get_nested_groups(username)
            if groups is not None:
                return groups
        except:
            crowd_logger.exception("Failed to fetch user data from Crowd")
        raise InvalidUser(username)
