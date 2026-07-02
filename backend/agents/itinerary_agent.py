import json
from backend.tools.groq_tool import call_groq


def extract_trip_updates(user_question, current_trip_data):
    prompt = f"""
You are a trip update extraction assistant.

Current trip data:
{current_trip_data}

User message:
{user_question}

Extract only the changes requested by the user.

Return ONLY valid JSON.
Do not write explanation.
Do not use markdown.

Possible keys:
source_city
destination
budget
people
travel_type
food_preference

Example:
{{
  "destination": "Paris",
  "budget": 800000
}}

If no trip update is requested, return:
{{}}
"""

    response = call_groq(prompt)

    try:
        return json.loads(response)
    except Exception:
        return {}


def generate_ai_plan(
    source,
    destination,
    start_date,
    end_date,
    days,
    people,
    travel_type,
    budget,
    budget_data,
    weather,
    places,
    hotels,
    food_preference,
    latest_news,
    emergency_info,
    packing_checklist,
    transport_suggestion
):
    prompt = f"""
You are TripMate AI, a realistic multi-agent travel planner.

IMPORTANT RULES:
- Do NOT invent unrealistic prices.
- Every tourist place must include approximate cost/person.
- Suggest budget-friendly attractions first.
- Do not suggest luxury hotels for low budgets.
- Respect food preference.
- Include weather/climate tips.
- Include latest travel alerts/news.
- Include emergency contact information.
- Include packing checklist based on weather and trip type.
- Transport must fit within the given transport budget.
- If flight is not possible in budget, clearly say it is not recommended.

Trip Details:
Source: {source}
Destination: {destination}
Start Date: {start_date}
End Date: {end_date}
Days: {days}
People: {people}
Travel Type: {travel_type}
Total Budget: ₹{budget}
Food Preference: {food_preference}

Budget Data:
{budget_data}

Transport Suggestion:
{transport_suggestion}

Weather Data:
{weather}

Places:
{places}

Hotels:
{hotels}

Latest News:
{latest_news}

Emergency Info:
{emergency_info}

Packing Checklist:
{packing_checklist}

Output Format:
1. Budget Reality Check
2. Recommended Transport with Estimated Cost and Budget Fit
3. Weather and Climate Conditions
4. Latest News / Travel Alerts
5. Emergency Contact Information
6. Budget-Friendly Places to Visit with Approx Cost
7. Realistic Hotel Suggestions
8. Day-wise Itinerary
9. Veg / Non-Veg Food Suggestions
10. Packing Checklist
11. Money-Saving Tips
12. Safety Tips

Keep it practical, realistic, and suitable for an internship project demo.
"""

    return call_groq(prompt)


def chat_with_tripmate(user_question, plan_context, budget_data=None, food_preference=None):
    prompt = f"""
You are TripMate AI, a practical travel assistant.

Existing Travel Plan:
{plan_context}

Budget Constraints:
{budget_data}

Food Preference:
{food_preference}

User Follow-up Question:
{user_question}

Rules:
- Keep suggestions realistic.
- Include approximate costs where relevant.
- Respect budget and food preference.
- If the user asks about transport, suggest options that fit the transport budget.
- If the user's request is not possible within budget, clearly say so and suggest alternatives.
- Do not suggest luxury options for a low budget.

Answer clearly and practically.
"""

    return call_groq(prompt)