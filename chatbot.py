import re
import random

# Dictionary of common pesticide and crop protection queries and responses
pesticide_knowledge_base = {
    "organic pesticides": [
        "Organic pesticides include neem oil, diatomaceous earth, insecticidal soaps, and pyrethrin. They're effective while being environmentally friendly.",
        "For organic pest control, you can use neem oil, garlic spray, or beneficial insects like ladybugs and lacewings.",
        "Spinosad is another organic-approved pesticide that targets a wide range of pests like thrips and leaf miners.",
        "Horticultural oils can be used to smother soft-bodied insects like aphids, scales, and whiteflies.",
        "Plant-based pesticides like chrysanthemum extract (pyrethrin) are fast-acting and degrade quickly in the environment."
    ],
    "chemical pesticides": [
        "Common chemical pesticides include carbamates, organophosphates, and pyrethroids. Always follow label instructions carefully.",
        "Chemical pesticides should be used as a last resort. Examples include malathion, carbaryl, and bifenthrin.",
        "Synthetic pesticides are effective but can harm non-target species and contribute to pesticide resistance.",
        "Use systemic insecticides like imidacloprid cautiously, as they are absorbed into plant tissues and can harm pollinators.",
        "Rotate pesticide types to prevent resistance buildup in pests over time."
    ],
    "prevention": [
        "Preventative measures include crop rotation, proper spacing, good air circulation, and regular monitoring for early detection.",
        "To prevent plant diseases, maintain proper sanitation, remove infected plants, and ensure good drainage in your garden.",
        "Use resistant plant varieties whenever possible to reduce the need for pesticide use.",
        "Mulching can suppress weeds and reduce soil-borne disease transmission.",
        "Avoid overwatering to prevent fungal growth and root rot."
    ],
    "apple": [
        "For apple trees, dormant oil can control overwintering pests. For fungal issues like apple scab, use a fungicide containing captan.",
        "Apple trees often face issues with codling moths and apple maggots. Consider using kaolin clay or targeted insecticides.",
        "Use pheromone traps for monitoring and disrupting mating of codling moths.",
        "Prune trees to increase airflow and reduce fungal disease risk.",
        "Sulfur sprays can help manage apple powdery mildew effectively."
    ],
    "tomato": [
        "Common tomato issues include early blight and hornworms. Copper-based fungicides help with blights, while Bt (Bacillus thuringiensis) controls caterpillars.",
        "For tomato plants, neem oil helps with aphids and whiteflies. Copper fungicide works well for blight and bacterial spot.",
        "Use floating row covers to protect young tomato plants from early pest damage.",
        "Companion planting with basil or marigolds may deter common tomato pests.",
        "Apply calcium supplements to prevent blossom end rot in tomatoes."
    ],
    "potato": [
        "Colorado potato beetles are a common pest. Consider using spinosad or neem oil. For blight, use copper-based fungicides.",
        "For potatoes, watch for late blight. Use copper fungicides preventatively and practice crop rotation.",
        "Hand-pick beetles and larvae in the early morning to reduce infestations.",
        "Planting trap crops like eggplant nearby can divert beetles from potatoes.",
        "Avoid planting potatoes in the same soil consecutively to prevent disease buildup."
    ],
    "corn": [
        "Corn earworms can be controlled with Bt (Bacillus thuringiensis). For fungal diseases, use propiconazole-based fungicides.",
        "For corn, corn borers and earworms are common pests. Consider Bt-based products or mineral oil applied to silk.",
        "Use row covers early in the season to block moth egg laying.",
        "Good field sanitation helps prevent overwintering of corn borers.",
        "Encourage natural predators like birds and parasitic wasps to reduce pest pressure."
    ],
    "grapes": [
        "Grape vines often face powdery mildew. Sulfur-based fungicides work well. For insects, consider neem oil or insecticidal soap.",
        "For grapes, Japanese beetles can be a problem. Use traps away from vines and consider neem oil or pyrethrin for control.",
        "Apply dormant sprays in winter to kill overwintering pests and fungi.",
        "Remove fallen leaves and prune for better airflow to reduce fungal outbreaks.",
        "Use netting to protect grape clusters from birds and flying insects."
    ],
    "application": [
        "Always apply pesticides in calm weather, early morning or evening to avoid harming beneficial insects like bees.",
        "For best results, apply pesticides at the first sign of infestation and follow label directions for timing and coverage.",
        "Use the right nozzle and pressure settings to avoid over- or under-applying chemicals.",
        "Clean equipment thoroughly after each use to avoid cross-contamination.",
        "Rotate pesticide types seasonally to prevent resistance buildup in pests."
    ],
    "safety": [
        "Always wear protective clothing, including gloves, long sleeves, and eye protection when applying pesticides.",
        "Store pesticides in their original containers, away from children and pets, and never reuse empty pesticide containers.",
        "Avoid inhaling fumes; use masks or respirators in enclosed spaces.",
        "Wash hands and clothing thoroughly after pesticide use.",
        "Never apply pesticides near water bodies without appropriate precautions."
    ],
    "beneficial insects": [
        "Beneficial insects like ladybugs, lacewings, and predatory wasps can help control pest populations naturally.",
        "To attract beneficial insects, plant flowers like marigolds, dill, and alyssum near your crops.",
        "Avoid broad-spectrum pesticides that can kill beneficial insects.",
        "Release purchased beneficial insects in the early morning or evening for best survival.",
        "Use hedgerows or insect hotels to provide habitats for beneficial species year-round."
    ],
    "fertilizer": [
        "While not a pesticide, proper fertilization keeps plants healthy and more resistant to pests and diseases.",
        "Over-fertilization can actually make plants more susceptible to pests, especially with excess nitrogen.",
        "Use slow-release or organic fertilizers to minimize nutrient leaching and pest attraction.",
        "Perform soil tests to determine exact nutrient needs before fertilizing.",
        "Avoid fertilizing in late fall, which may encourage tender growth prone to frost and pest damage."
    ]
}


# Greeting and farewell responses
greetings = ["Hello! How can I help with your crop protection questions today?", 
            "Hi there! I'm your crop protection assistant. What can I help you with?", 
            "Welcome! What would you like to know about pesticides or crop protection?"]

farewells = ["Hope that helps! Let me know if you have more questions.", 
            "Happy gardening! Feel free to ask if you need more information.", 
            "Good luck with your crops! Ask again if you need more help."]

fallbacks = ["I'm not sure about that, but I can help with common pesticide and crop protection questions.",
            "I don't have specific information on that. Is there a particular crop or pest you're dealing with?",
            "I'm still learning! Could you ask about a specific crop, pest, or pesticide type?"]

def get_response(user_message):
    """Generate a response based on the user's query"""
    # Convert to lowercase for matching
    message = user_message.lower()
    
    # Check for greetings
    if re.search(r'\b(hi|hello|hey|greetings)\b', message):
        return random.choice(greetings)
    
    # Check for farewells
    if re.search(r'\b(bye|goodbye|thank you|thanks)\b', message):
        return random.choice(farewells)
    
    # Search for relevant keywords in our knowledge base
    for keyword, responses in pesticide_knowledge_base.items():
        if keyword in message:
            return random.choice(responses)
    
    # If no specific match found, check if it's about a pest or disease
    if re.search(r'\b(pest|disease|bug|insect|fungus|mold|mildew|rot|blight)\b', message):
        return "For most pest and disease issues, early detection is key. Could you specify which crop you're growing or what the symptoms look like?"
    
    # Default fallback
    return random.choice(fallbacks)