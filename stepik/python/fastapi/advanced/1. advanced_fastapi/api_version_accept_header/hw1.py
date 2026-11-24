import re


def get_api_version_from_accept(accept_header: str | None) -> str | None:
    # Извлеките поддерживаемую версию из vendor media type.
    if not accept_header:
        return None

    match = re.search(r'application/vnd\.mycompany\.v([12])\+json', accept_header)
    if match:
        return match.group(1)
    return None
