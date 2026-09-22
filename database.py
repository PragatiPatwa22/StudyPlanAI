import sqlite3


DATABASE_NAME = "study_plans.db"


def create_database():

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS study_plans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject TEXT NOT NULL,
            hours INTEGER NOT NULL,
            exam_date TEXT NOT NULL,
            difficulty INTEGER NOT NULL,
            urgency INTEGER NOT NULL,
            weakness INTEGER NOT NULL,
            priority REAL NOT NULL,
            study_plan TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def save_plan(
    subject,
    hours,
    exam_date,
    difficulty,
    urgency,
    weakness,
    priority,
    study_plan
):

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO study_plans
        (
            subject,
            hours,
            exam_date,
            difficulty,
            urgency,
            weakness,
            priority,
            study_plan
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        subject,
        hours,
        str(exam_date),
        difficulty,
        urgency,
        weakness,
        priority,
        study_plan
    ))

    connection.commit()
    connection.close()


def get_plans():

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            subject,
            hours,
            exam_date,
            difficulty,
            urgency,
            weakness,
            priority,
            study_plan
        FROM study_plans
        ORDER BY id DESC
    """)

    plans = cursor.fetchall()

    connection.close()

    return plans


def delete_plan(plan_id):

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM study_plans WHERE id = ?",
        (plan_id,)
    )

    connection.commit()
    connection.close()


def delete_all_plans():

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("DELETE FROM study_plans")

    connection.commit()
    connection.close()