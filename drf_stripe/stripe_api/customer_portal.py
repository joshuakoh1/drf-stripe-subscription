from .api import stripe_api as stripe
from .customers import get_or_create_stripe_user
from ..settings import drf_stripe_settings
from functools import reduce


def stripe_api_create_billing_portal_session(user_id, return_url = None):
    """
    Creates a Stripe Customer Portal Session.

    :param str user_id: Django User id
    """
    stripe_user = get_or_create_stripe_user(user_id=user_id)

    return_url = return_url if return_url else reduce(urljoin, (drf_stripe_settings.FRONT_END_BASE_URL,
                                  drf_stripe_settings.PORTAL_RETURN_URL_PATH))

    session = stripe.billing_portal.Session.create(
        customer=stripe_user.customer_id,
        return_url=return_url
    )

    return session
