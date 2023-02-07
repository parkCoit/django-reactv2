from fastapi import APIRouter
from starlette.responses import JSONResponse

from app.schemas.chatbot import ChatBotDTO
from app.services.chatbot.kakao_chatbot import KakaoChatbot

from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

html = """<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/chatbot/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>"""

chatbot_router = APIRouter()


@chatbot_router.get("")
async def get():
    return HTMLResponse(html)


@chatbot_router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        print(f"받은 메세지 : {data}")
        await websocket.send_text(f" 작성자 : {data}")
        await websocket.send_text(f" AI 봇 : {KakaoChatbot().exec_7(data)}")


@chatbot_router.get("/chat", status_code=201)
async def chat_bot(sentence: ChatBotDTO):
    return JSONResponse(status_code=200,
                        content=dict(msg=KakaoChatbot().exec_7(sentence)))