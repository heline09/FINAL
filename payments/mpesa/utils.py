from django_daraja.mpesa.utils import mpesa_config, mpesa_access_token
from datetime import datetime
import base64


class MpesaUtils:
    @classmethod
    def get_password(cls):
        passkey = mpesa_config("MPESA_PASSKEY")
        mpesa_environment = mpesa_config("MPESA_ENVIRONMENT")
        if mpesa_environment == "sandbox":
            business_short_code = mpesa_config("MPESA_EXPRESS_SHORTCODE")
        else:
            business_short_code = mpesa_config("MPESA_SHORTCODE")
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        password = base64.b64encode(
            (business_short_code + passkey + timestamp).encode("ascii")
        ).decode("utf-8")
        return password
    @classmethod
    def short_code(cls):
        mpesa_environment = mpesa_config("MPESA_ENVIRONMENT")
        if mpesa_environment == "sandbox":
            business_short_code = mpesa_config("MPESA_EXPRESS_SHORTCODE")
        else:
            business_short_code = mpesa_config("MPESA_SHORTCODE")
        return business_short_code
    @classmethod
    def timestamp(cls):
        return datetime.now().strftime("%Y%m%d%H%M%S")
    @classmethod
    def access_token(cls) -> str:
        return mpesa_access_token()
