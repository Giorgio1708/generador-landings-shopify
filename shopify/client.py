import time
import requests
from config.settings import (
    SHOPIFY_STORE,
    SHOPIFY_CLIENT_ID,
    SHOPIFY_CLIENT_SECRET,
    SHOPIFY_API_VERSION,
)


class ShopifyClient:
    def __init__(self):
        if not SHOPIFY_STORE or not SHOPIFY_CLIENT_ID or not SHOPIFY_CLIENT_SECRET:
            raise ValueError(
                "SHOPIFY_STORE, SHOPIFY_CLIENT_ID y SHOPIFY_CLIENT_SECRET "
                "deben estar configurados en el archivo .env"
            )
        self.base_url = f"https://{SHOPIFY_STORE}/admin/api/{SHOPIFY_API_VERSION}"
        self._access_token = None
        self._token_expires_at = 0

    def _get_access_token(self) -> str:
        """Obtiene un token de acceso via client credentials. Se renueva automáticamente."""
        if self._access_token and time.time() < self._token_expires_at - 60:
            return self._access_token

        response = requests.post(
            f"https://{SHOPIFY_STORE}/admin/oauth/access_token",
            data={
                "grant_type": "client_credentials",
                "client_id": SHOPIFY_CLIENT_ID,
                "client_secret": SHOPIFY_CLIENT_SECRET,
            },
        )
        if not response.ok:
            raise RuntimeError(
                f"Error obteniendo token de Shopify: {response.status_code} {response.text}"
            )
        data = response.json()
        self._access_token = data["access_token"]
        self._token_expires_at = time.time() + data.get("expires_in", 86399)
        return self._access_token

    def _headers(self) -> dict:
        return {
            "X-Shopify-Access-Token": self._get_access_token(),
            "Content-Type": "application/json",
        }

    def post(self, endpoint: str, data: dict) -> dict:
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, headers=self._headers(), json=data)
        self._raise_for_status(response)
        return response.json()

    def get(self, endpoint: str) -> dict:
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, headers=self._headers())
        self._raise_for_status(response)
        return response.json()

    def put(self, endpoint: str, data: dict) -> dict:
        url = f"{self.base_url}{endpoint}"
        response = requests.put(url, headers=self._headers(), json=data)
        self._raise_for_status(response)
        return response.json()

    def put_asset(self, theme_id: int, key: str, value: str) -> dict:
        url = f"{self.base_url}/themes/{theme_id}/assets.json"
        response = requests.put(
            url,
            headers=self._headers(),
            json={"asset": {"key": key, "value": value}},
        )
        self._raise_for_status(response)
        return response.json()

    def _raise_for_status(self, response: requests.Response) -> None:
        if response.status_code == 429:
            retry_after = int(response.headers.get("Retry-After", 2))
            time.sleep(retry_after)
            return
        if not response.ok:
            raise RuntimeError(
                f"Shopify API error {response.status_code}: {response.text}"
            )
