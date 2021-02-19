from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import DetailView

from django_sendfile import sendfile

from archiefvernietigingscomponent.constants import RoleTypeChoices
from archiefvernietigingscomponent.report.models import DestructionReport


class DownloadDestructionReportView(UserPassesTestMixin, DetailView):
    """
    Verify the permission required and send the filefield via sendfile.

    :param permission_required: the permission required to view the file
    :param model: the model class to look up the object
    :param file_field: the name of the ``Filefield``
    """

    file_field = "content"
    # see :func:`sendfile.sendfile` for available parameters
    sendfile_options = None
    model = DestructionReport

    def test_func(self):
        if not self.request.user.is_authenticated:
            return False

        report = self.get_object()

        if (
            self.request.user == report.process_owner
            or self.request.user.role.type == RoleTypeChoices.functional_admin
        ):
            return True

        return False

    def get_sendfile_opts(self):
        return self.sendfile_options or {}

    def get(self, request, *args, **kwargs):
        filename = getattr(self.get_object(), self.file_field).path
        sendfile_options = self.get_sendfile_opts()
        return sendfile(request, filename, **sendfile_options)