import streamlit as st
from fuzzy_logic import calculate_priority
from study_planner import create_study_plan
from database import (
    create_database,
    save_plan,
    get_plans,
    delete_plan,
    delete_all_plans
)


st.set_page_config(
    page_title="AI Study Plan Generator",
    page_icon="📚",
    layout="wide"
)


create_database()


st.title("📚 AI + Fuzzy Logic Study Plan Generator")

st.write(
    "Create personalized study plans using fuzzy logic based on "
    "difficulty, exam urgency and subject weakness."
)


st.header("📝 Create Your Study Plan")


col1, col2 = st.columns(2)


with col1:

    subject = st.text_input(
        "Subject Name",
        placeholder="Example: Mathematics"
    )

    hours = st.number_input(
        "Study Hours Per Day",
        min_value=1,
        max_value=12,
        value=2
    )

    exam_date = st.date_input(
        "Exam Date"
    )


with col2:

    difficulty = st.slider(
        "Subject Difficulty",
        0,
        100,
        50
    )

    urgency = st.slider(
        "Exam Urgency",
        0,
        100,
        50
    )

    weakness = st.slider(
        "Your Weakness in Subject",
        0,
        100,
        50
    )


if st.button("🚀 Generate Study Plan"):

    if subject.strip() == "":

        st.warning(
            "Please enter a subject name."
        )

    else:

        priority = calculate_priority(
            difficulty,
            urgency,
            weakness
        )

        study_plan = create_study_plan(
            subject,
            hours,
            difficulty,
            priority,
            exam_date
        )

        save_plan(
            subject,
            hours,
            exam_date,
            difficulty,
            urgency,
            weakness,
            priority,
            study_plan
        )

        st.success(
            "Study plan generated and saved successfully!"
        )

        st.subheader("📊 Study Priority")

        if priority >= 70:

            st.error(
                f"High Priority: {priority:.2f}/100"
            )

        elif priority >= 35:

            st.warning(
                f"Medium Priority: {priority:.2f}/100"
            )

        else:

            st.success(
                f"Low Priority: {priority:.2f}/100"
            )


st.divider()


st.header("📚 My Saved Study Plans")


plans = get_plans()


if len(plans) == 0:

    st.info(
        "No study plans available. Create your first study plan above."
    )

else:

    st.metric(
        "Total Saved Plans",
        len(plans)
    )


    for plan in plans:

        plan_id = plan[0]
        subject_name = plan[1]
        study_hours = plan[2]
        exam_date_value = plan[3]
        difficulty_value = plan[4]
        urgency_value = plan[5]
        weakness_value = plan[6]
        priority_value = plan[7]
        study_plan_value = plan[8]


        st.subheader(
            f"📖 {subject_name}"
        )


        col1, col2, col3, col4 = st.columns(4)


        with col1:

            st.metric(
                "Study Hours",
                f"{study_hours} hr"
            )


        with col2:

            st.metric(
                "Difficulty",
                difficulty_value
            )


        with col3:

            st.metric(
                "Urgency",
                urgency_value
            )


        with col4:

            st.metric(
                "Priority",
                f"{priority_value:.1f}"
            )


        st.write(
            f"📅 Exam Date: {exam_date_value}"
        )


        st.write(
            f"💪 Weakness: {weakness_value}/100"
        )


        with st.expander(
            "📋 View Complete Study Plan"
        ):

            st.write(
                study_plan_value
            )


        if st.button(
            "🗑️ Remove This Plan",
            key=f"delete_{plan_id}"
        ):

            delete_plan(plan_id)

            st.success(
                "Study plan removed successfully."
            )

            st.rerun()


        st.divider()


    if st.button("🗑️ Clear All Study Plans"):

        delete_all_plans()

        st.success(
            "All study plans have been removed."
        )

        st.rerun()