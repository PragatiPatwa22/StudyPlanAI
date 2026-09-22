# StudyPlanAI

## 1. Description

StudyPlanAI is a web-based study planning application developed using Python and Streamlit. It helps students organize their studies by considering factors such as subject difficulty, exam urgency, and personal weakness.

The application uses **fuzzy logic** to calculate the priority of a subject. It also includes an **AI-based study planner** using LangChain and a language model to generate personalized study plans from natural-language student requests.

The main purpose of the project is to combine **AI, fuzzy logic, and structured learning principles** to help students plan their study time effectively.

---

## 2. Features

* Subject priority calculation
* Difficulty-based study planning
* Exam urgency analysis
* Student weakness analysis
* Fuzzy-logic based priority score
* High, Medium and Low priority classification
* Natural-language study requests
* AI-based study-plan generation
* Time allocation for topics
* Break and revision planning
* Streamlit web interface
* SQLite database support
* Public cloud deployment
* GitHub source-code repository

---

## 3. Technologies Used

| Technology                | Purpose                        |
| ------------------------- | ------------------------------ |
| Python                    | Main programming language      |
| Streamlit                 | Web application interface      |
| Fuzzy Logic               | Subject priority calculation   |
| Scikit-Fuzzy              | Implementation of fuzzy logic  |
| LangChain                 | AI application framework       |
| LangChain OpenAI          | Integration with OpenAI models |
| OpenAI API                | AI-based study-plan generation |
| SQLite                    | Local database                 |
| Git                       | Version control                |
| GitHub                    | Source-code management         |
| Streamlit Community Cloud | Deployment                     |

---

## 4. System Workflow

```text
Student
   ↓
Enter Study Requirements
   ↓
Difficulty + Exam Urgency + Weakness
   ↓
Fuzzy Logic Processing
   ↓
Calculate Subject Priority
   ↓
High / Medium / Low Priority
   ↓
Generate Study Plan
   ↓
Topics + Time Allocation + Breaks + Revision
   ↓
Display Results
```

For the AI component:

```text
Student's Natural-Language Request
              ↓
        AI Processor
              ↓
          LangChain
              ↓
       Language Model
              ↓
     Personalized Plan
              ↓
        Display Result
```

---

## 5. Project Structure

```text
StudyPlanAI/
│
├── app.py
├── ai_processor.py
├── fuzzy_logic.py
├── database.py
├── study_planner.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── .streamlit/
    └── secrets.toml
```

---

## 6. File Description

| File                      | Description                                             |
| ------------------------- | ------------------------------------------------------- |
| `app.py`                  | Main Streamlit application and user interface           |
| `ai_processor.py`         | Handles AI-based study-plan generation                  |
| `fuzzy_logic.py`          | Performs fuzzy-logic based subject-priority calculation |
| `database.py`             | Handles SQLite database operations                      |
| `study_planner.py`        | Contains study-planning functionality                   |
| `requirements.txt`        | Contains required Python libraries                      |
| `README.md`               | Contains project information and setup instructions     |
| `.gitignore`              | Prevents unnecessary/private files from being uploaded  |
| `.streamlit/secrets.toml` | Stores local deployment secrets such as API credentials |

**Note:** `secrets.toml` must not be uploaded to GitHub.

---

## 7. Installation and Setup

### Step 1: Clone the repository

```bash
git clone https://github.com/PragatiPatwa22/StudyPlanAI.git
```

### Step 2: Open the project folder

```bash
cd StudyPlanAI
```

### Step 3: Create a virtual environment

```bash
python -m venv venv
```

### Step 4: Activate the virtual environment

For Windows:

```bash
venv\Scripts\activate
```

### Step 5: Install the required libraries

```bash
pip install -r requirements.txt
```

### Step 6: Configure secrets

For local AI functionality, configure the required API key in the appropriate Streamlit secrets/environment configuration.

Do not place the actual API key inside Python source files.

---

## 8. Running the Application

Run the following command in the VS Code terminal:

```bash
streamlit run app.py
```

After running the command, Streamlit will provide a local address, usually:

```text
http://localhost:8501
```

Open the address in a web browser to use the application.

---

## 9. Example Input

A student can provide a natural-language request such as:

```text
I have a Mathematics exam in 5 days.
I am weak in Integration and can study for 3 hours every day.
Create a study plan with revision and breaks.
```

For the fuzzy-logic module, example values can be:

| Input              | Example Value |
| ------------------ | ------------: |
| Subject Difficulty |            80 |
| Exam Urgency       |            80 |
| Student Weakness   |            70 |

---

## 10. Example Extracted Preferences

From the example request, the application can identify the following study requirements:

| Preference           | Extracted Information |
| -------------------- | --------------------- |
| Subject              | Mathematics           |
| Topic                | Integration           |
| Exam Time            | 5 days                |
| Available Study Time | 3 hours/day           |
| Weakness             | Integration           |
| Revision Required    | Yes                   |
| Breaks Required      | Yes                   |

---

## 11. Example Recommendations

Based on the above requirements, the application can generate recommendations such as:

| Area              | Recommendation                                  |
| ----------------- | ----------------------------------------------- |
| Priority          | Give Mathematics high priority                  |
| Main Topic        | Focus on Integration                            |
| Daily Study       | Use the available 3 hours effectively           |
| Practice          | Include problem-solving practice                |
| Breaks            | Include short breaks between sessions           |
| Revision          | Reserve time for revision                       |
| Final Preparation | Perform a final revision before the examination |

## 12. IKS Connection

StudyPlanAI connects modern Information Technology with principles associated with **Indian Knowledge Systems (IKS)**.

Traditional Indian learning approaches emphasized concepts such as:

* Discipline in learning
* Regular practice
* Revision
* Time management
* Systematic progression of knowledge
* Focus and concentration

StudyPlanAI applies these principles through a modern digital study-planning system.

For example, the application includes **structured study sessions, revision periods and breaks**, while fuzzy logic helps determine which subjects require greater attention.

Thus, the project demonstrates how traditional learning principles can be supported using **AI, fuzzy logic and modern web technologies**.

## 13. Deployment

The application is deployed using **Streamlit Community Cloud**.

### GitHub Repository

```text
https://github.com/PragatiPatwa22/StudyPlanAI
```

### Live Application

```text
https://studyplanai-cieylyyxvfdbgvgat2uziy.streamlit.app
```

The GitHub repository contains the source code and dependency files, while Streamlit Community Cloud hosts the web application.

## 14. Student Details

| Detail          | Information    |
| --------------- | -------------- |
| Student Name    | Pragati Patwa  |
| Course          | TY IT          |
| Project Name    | StudyPlanAI    |
| Subject         | IKS            |
| Academic Year   | 2026–27        |
| GitHub Username | PragatiPatwa22 |
Roll no: 19041


## 15. Security

The project follows basic security practices:

* API keys are not stored directly in the source code.
* API credentials are stored using secrets/environment variables.
* `.gitignore` is used to prevent sensitive/local files from being committed.
* Passwords and tokens should not be uploaded to GitHub.
* Public repositories should contain only source code and safe configuration placeholders.
* API keys should be regenerated if accidentally exposed.

Example placeholder:

```text
OPENAI_API_KEY=your_api_key_here
```

Never replace `your_api_key_here` with your real key in `README.md`.

---

## 16. Future Scope

Future versions of StudyPlanAI can include:

1. Automatic daily and weekly timetable generation.
2. Student progress tracking.
3. Study reminders and notifications.
4. Performance-based recommendations.
5. Mobile application support.
6. More subjects and learning parameters.
7. Calendar integration.
8. Dashboard with study statistics.
9. Integration with additional AI models.
10. Local AI model support to reduce dependency on paid APIs.
11. More IKS-based learning principles.
12. Personalized plans based on previous academic performance.
