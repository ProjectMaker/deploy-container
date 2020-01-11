import hashlib
import hmac
import six
from flask import abort, request


def _get_header(key, logger):
    """Return message header"""
    logger.info('_get_header : ' + key)
    try:
        return request.headers[key]
    except KeyError:
        logger.info('Missing header ' + key)
        abort(400, "Missing header: " + key)


def _get_digest(secret):
    return hmac.new(secret.encode(), request.data, hashlib.sha1).hexdigest()


def verify_hook(logger):
    digest = _get_digest('Loosely21Burp32Lathrop')
    sig_parts = _get_header("X-Hub-Signature", logger).split("=", 1)
    if not isinstance(digest, six.text_type):
        digest = six.text_type(digest)

    if len(sig_parts) < 2 or sig_parts[0] != "sha1" or not hmac.compare_digest(sig_parts[1], digest):
        logger.info('invalid signature')
        abort(400, "Invalid signature")

    return True


