import logging

from fastapi import APIRouter, Request, Response

from server.services.orchestrator import handle_message

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/events")
async def slack_events(request: Request):
    body = await request.json()

    # Slack URL verification challenge
    if body.get("type") == "url_verification":
        return {"challenge": body["challenge"]}

    if body.get("type") == "event_callback":
        event = body.get("event", {})

        # DM 메시지만 처리
        if event.get("type") != "message" or event.get("channel_type") != "im":
            return Response(status_code=200)

        # 봇 자신의 메시지 무시 (무한루프 방지)
        if event.get("bot_id") or event.get("subtype"):
            return Response(status_code=200)

        slack_user_id = event.get("user")
        text = event.get("text", "")
        channel = event.get("channel")

        if not slack_user_id or not text.strip():
            return Response(status_code=200)

        # 비동기 처리 (슬랙 3초 룰 대응)
        import asyncio
        asyncio.create_task(
            handle_message(slack_user_id=slack_user_id, text=text, channel=channel)
        )

    return Response(status_code=200)
