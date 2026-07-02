from backend.tools.groq_tool import call_groq


def suggest_transport(source, destination, people, travel_type, budget_data):
    transport_budget = budget_data.get("transport", 0)

    prompt = f"""
You are a realistic Indian transport planning agent.

Trip:
Source: {source}
Destination: {destination}
People: {people}
Travel Type: {travel_type}
Transport Budget: ₹{transport_budget}

Important rules:
- Do NOT give exact real-time ticket prices.
- Give realistic estimated price ranges only.
- For long-distance routes in India, train is usually cheaper than bus.
- Bus should NOT be shown cheaper than train for long routes.
- Flight is fastest but usually most expensive.
- Recommend only the option that fits the transport budget.
- If something exceeds budget, clearly say "Not budget-friendly".
- Mention: prices are approximate and should be checked on IRCTC, RedBus, or airline websites.

Use this general pricing logic:
Train: cheapest for long distance
Bus: usually higher than sleeper train for long distance
Flight: highest but fastest

Output format:

Best Transport Option:
- Mode:
- Estimated cost/person:
- Estimated total cost:
- Budget fit:
- Why this is best:

Other Options:
1. Train
2. Bus
3. Flight

Final Recommendation:
"""

    return call_groq(prompt)