from api.models import ChapterNode, DoorNode, EmailBody, EventNode, InsurancePackage, CompletionResult, Node
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
import os
import typing


def send_email(body: EmailBody) -> dict[str, str]:
    """Send an email as defined in EmailBody"""
    msg = MIMEText(body.message)
    msg["subject"] = body.subject
    with SMTP_SSL("smtp.gmail.com", 465) as smtp_server:
        smtp_server.login(
            os.environ.get("SMTP_EMAIL_ADDRESS", ""),
            os.environ.get("SMTP_PASSWORD", ""),
        )
        smtp_server.sendmail(
            os.environ.get("SMTP_EMAIL_ADDRESS", ""), [body.to], msg.as_string()
        )
    return {"message": "Email sent successfully"}


def get_all_insurance_packages() -> list[InsurancePackage]:
    vehicle_insurace = InsurancePackage(
        name="Kfz-Versicherung",
        price=0,  # FIXME
        description="",  # FIXME
        covered_items=["Vehicle"],
    )

    occupational_disability_instance = InsurancePackage(
        name="Berufsunfähigkeits-Versicherung",
        price=0,  # FIXME
        description="",  # FIXME
        covered_items=[
            "Lebenssituation",
            "Lebenslage",
        ],
    )

    household_insurace = InsurancePackage(
        name="Hausratsversicherung",
        price=0,  # FIXME
        description="",  # FIXME
        covered_items=["Haustiere", "Lebenslage", "Handy", "Familienstand"],
    )

    abroad_travel_insure = InsurancePackage(
        name="Auslandsreiseversicherung",
        price=0,  # FIXME
        description="",  # FIXME
        covered_items=["Lebenslage", "Reise"],  # TODO ADD ME
    )

    liability_insurance = InsurancePackage(
        name="Haftpflichtversicherung",
        price=0,  # FIXME
        description="",  # FIXME
        covered_items=["Lebenssituation", "Lebenslage", "Haustiere"],
    )

    return [
        abroad_travel_insure,
        household_insurace,
        liability_insurance,
        occupational_disability_instance,
        vehicle_insurace,
    ]


def generate_email_content(completion_result: CompletionResult) -> str:
    email_message = """
Lieber Kollege,

Eine weitere Simulation in InsureNauts wurde erfolgreich durchlaufen.

Angaben zur Person:
- Name: {0}
- Email Adresse: {1}

Ermittelte Interessen im Rahmen der Simulation:
- {2}

Durch die automatisierte Auswertung wurden diese Versicherungen als
besonders erfolgsversprächend eingestuft:
- {3}

Mit freundlichen Grüßen,
Ihr InsureNauts Team
    """.format(
        completion_result.name,
        completion_result.email,
        "\n- ".join(completion_result.relevant_attributes),
        "\n- ".join(completion_result.suggested_insurance_packages),
    )

    return email_message






def get_liability_insurance() -> ChapterNode:
    """Liability Cover"""
    print("Inside UTILS")
    liability_chapter = ChapterNode(
        text="Text für das Haftpflichtkapitel",
        options=[
            Node(id="1", text="Geh zum Job"),
            Node(id="2", text="Schlendere weiter")
        ],
        insurance="Liability Insurance"
    )
    liability_door1 = Node(text= "Wähle eine option")

    liability_event_good= EventNode(insurance="Haftplicht",cost="5",text="""Deine  Fruend erzählt dir was von einem coolen
neuen Job. Du bewirbst dich und wirst genommen.""")
    liability_event_bad= EventNode(insurance="Haftplicht",cost="",text="""Der Ball zerstört das Fenster des Nachbarn ,leider hast du keine Versicherung musst für den schaden aufkommen""")

    liability_event_good2= EventNode(insurance="Haftplicht",cost="5",text="""""")
    # You might want to add the doors and events to the options if they are meant to be part of the story.
    liability_chapter.options.extend([liability_door1, liability_event_good, liability_event_bad, liability_event_good2])

    return liability_chapter






   
