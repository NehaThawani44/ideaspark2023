import typing
import uvicorn
from fastapi import FastAPI
from typing import Union

from api.models import (
    ChapterNode,DoorNode,
    GeneratedQuestion,
    UserAnswer,
    RecommendationResult,
    EmailBody,
    InsurancePackage,
    CompletionResult,

)
from api.utils import get_all_insurance_packages, send_email, generate_email_content , get_liability_insurance


app = FastAPI()


@app.get("/healthcheck")
async def get_health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/init", description="Load initial data.")
async def load_initial_app_data_handler() -> dict[str, str]:
    return {"message": "Hello World"}


@app.get("/insurances", description="List all insurance packages.")
async def list_all_insurance_packages() -> list[InsurancePackage]:
    return get_all_insurance_packages()






    return liability_chapter
def get_next_chapter(question_id: str, user_answer: str) -> Union[ChapterNode, DoorNode]:
   

    # Example logic for chapter 1
    if question_id == "1" and user_answer.lower() == "yes":
        return get_liability_insurance()
    else:
        # Return a generic chapter for other cases
        return ChapterNode(id="2", text="Another chapter", insurance="")




@app.post("/answer", response_model=ChapterNode, description="Process a user answer and generate next chapter.")
async def process_answer_handler(user_answer: UserAnswer) -> typing.Any:
    next_chapter = get_next_chapter(user_answer.question_id, user_answer.message)

    # Assuming next_chapter is an instance of ChapterNode
    response = ChapterNode(
        id=next_chapter.id,
        text=next_chapter.text,
        insurance=next_chapter.insurance,
        options=[option.text for option in next_chapter.options]
    )
    return response
    
@app.get("/recommendations", description="Generate recommendations based on user id")
async def generate_recommendations_handler(user_id: int) -> RecommendationResult:
    pass


@app.post("/email")
async def send_email_handler(body: EmailBody) -> dict[str, str]:
    return send_email(body)


@app.post("/submit", description="User completes game and result gets mailed to agent.")
async def complete_game(completion_result: CompletionResult) -> dict[str, str]:
    email_content = generate_email_content(completion_result)
    email_body = EmailBody(
        to="manuellang183@gmail.com",
        subject="Auswertung von InsureNauts verfügbar",
        message=email_content,
    )
    return send_email(email_body)


def run_app():
    uvicorn.run("api.main:app", host="0.0.0.0", port=8001, reload=True)
