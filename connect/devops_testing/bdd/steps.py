from behave import when
from behave.runner import Context


@when("subscription request is processed")
def request_is_processed(context: Context):
    """
    Sends the request to Connect API and waits some time so the
    request is processed either by a processor or by manually.

    :param context: Context
    :return: None
    """
    context.request = context.connect.provision_request(context.builder.build())
