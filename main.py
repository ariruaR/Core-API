from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Core Backend Service")

# Описываем структуру данных, которую пришлет Event Processor
class EventUpdate(BaseModel):
    event_id: str
    filename: str
    user_id: int
    status: str
    timestamp: str

@app.post("/core/event-receiver")
async def receive_event(event: EventUpdate):
    # В реальности здесь будет запись в БД: await db.save(event)
    
    print(f" [CORE] Получено новое событие!")
    print(f" ID: {event.event_id}")
    print(f" Файл: {event.filename}")
    print(f" Пользователь ID: {event.user_id}")
    print(f" Статус: {event.status}")
    
    return {
        "status": "accepted", 
        "message": f"Event {event.event_id} registered in Core"
    }

if __name__ == "__main__":
    import uvicorn
    # Запускаем на 8001
    uvicorn.run(app, port=8001)