import os


class ServerConfig:
    def __init__(self) -> None:
        self.sse_port = int(os.getenv("MCP_SSE_PORT", "8000"))
        self.streamable_http_port = int(os.getenv("MCP_STREAMABLE_HTTP_PORT", "8080"))
        self.sourcegraph_endpoint = self._get_required_env("SRC_ENDPOINT")
        self.sourcegraph_token = os.getenv("SRC_ACCESS_TOKEN", "")  # Optional

    @staticmethod
    def _get_required_env(key: str) -> str:
        """Get required environment variable or raise descriptive error."""
        value = os.getenv(key)
        if not value:
            raise ValueError(f"Required environment variable {key} is not set")
        return value
