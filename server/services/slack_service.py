import logging

from slack_sdk.web.async_client import AsyncWebClient

from server.config import settings

logger = logging.getLogger(__name__)

slack_client = AsyncWebClient(token=settings.slack_bot_token)


async def send_message(channel: str, text: str):
    """슬랙 DM으로 메시지 발송"""
    try:
        await slack_client.chat_postMessage(channel=channel, text=text)
    except Exception as e:
        logger.error(f"Failed to send Slack message: {e}")
