from datetime import timedelta


def create_study_plan(subject, hours, difficulty, priority, exam_date):

    if priority >= 70:
        days = 5
        focus = "Focus more on difficult topics and practice."
    elif priority >= 35:
        days = 4
        focus = "Focus on concepts and regular practice."
    else:
        days = 3
        focus = "Focus on basic concepts and revision."

    daily_hours = hours

    start_date = exam_date - timedelta(days=days)

    plan = f"Study Plan for {subject}\n\n"

    plan += f"Priority: {priority:.2f}/100\n"
    plan += f"Difficulty: {difficulty}/100\n"
    plan += f"Daily Study Time: {daily_hours} hour(s)\n"
    plan += f"Exam Date: {exam_date.strftime('%d %B %Y')}\n\n"

    plan += f"Study Strategy:\n{focus}\n\n"

    for day in range(1, days + 1):

        study_date = start_date + timedelta(days=day - 1)

        if day == 1:
            activity = "Learn basic concepts and understand the syllabus."
        elif day == 2:
            activity = "Study important topics and make short notes."
        elif day == 3:
            activity = "Solve practice questions and previous problems."
        elif day == 4:
            activity = "Practice difficult topics and solve more questions."
        else:
            activity = "Complete revision and take a self-test."

        plan += f"Day {day}\n"
        plan += f"Date: {study_date.strftime('%d %B %Y')}\n"
        plan += f"Study Time: {daily_hours} hour(s)\n"
        plan += f"Activity: {activity}\n"
        plan += "Break: Take a 10-15 minute break after each study session.\n"
        plan += "Revision: Spend the last 15-20 minutes revising.\n\n"

    return plan