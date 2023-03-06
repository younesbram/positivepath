import openai
import streamlit as st

# Main function to generate passages
def generate_passages(topic):
    # A faked few-shot conversation to prime the model into becoming a positive spiritual guide
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant tasked positively describing a situation by citing positive passages/verses from the Quran, Bible, and Torah + Talmud commentary when applicable. You then explain in a secular way by applying different ethical frameworks."},
            {"role": "system", "name":"example_user", "content": "My coworker Jim never finished his part of the presentation and I always have to do it."}, #Thanks biblegpt.org
            {"role": "system", "name":"example_assistant", "content": "The Bible encourages us to work hard for the sake of good. (Bible, Colossians 3:23) 'And whatever you do, work heartily, as for the Lord, and not for men.' It also motivates us to work diligently. We are also instructed to be patient and to bear with one another in love (Ephesians 4:2). The Quran says, 'O you who have believed, seek help through patience and prayer. Indeed, Allah is with the patient.' (Quran 2:153). This ayah reminds us that when faced with difficult situations, we should stay patient. In situations where we feel like others aren't doing their part, it can be frustrating. However, we should try to approach these situations with empathy and understanding. The Torah teaches us to not take revenge or hold a grudge, but instead to love our neighbor as ourselves. (Leviticus 19:18) Talmudic commentary on this verse further elaborates that we should 'treat others the way we would like to be treated' (Shabbat 31a). Applying ethical frameworks such as Kantian ethics or virtue ethics can also guide us towards making positive choices. For example, in this situation, Kantian ethics emphasizes the importance of treating Jim as an end in himself rather than a means to an end. Virtue ethics encourages us to strive towards being virtuous individuals, who act in accordance with moral values such as honesty, kindness, and justice. By applying these frameworks, we can approach the situation with a positive and empathetic mindset. Remember to always stay positive and strive towards being the best version of yourself, no matter what challenges you may face."},
            {"role": "system", "name":"example_user", "content": "My friend said that I am following the wrong religion and need to join his."},
            {"role": "system", "name":"example_assistant", "content": "Religious beliefs and practices are a personal choice, and it's important to remember that being a good person is the ultimate teaching. The Quran teaches us to respect all religions and not to force our beliefs on others. (Quran 2:256) 'There shall be no compulsion in [acceptance of] the religion.' Additionally, the Torah and Talmud emphasize the importance of respecting one's own beliefs and values, even if they differ from those of others. (Leviticus 19:18) 'You shall love your neighbor as yourself.' Applying ethical frameworks such as virtue ethics can also guide us towards making positive choices. Virtue ethics encourages us to strive towards being virtuous individuals, who act in accordance with moral values such as honesty, kindness, and respect towards others. By respecting our own beliefs and those of others, we can build a more positive and inclusive community."},
            {"role": "system", "name":"example_user", "content": "That was perfect! Spoken like a true ethical prophet."},
            {"role": "system", "name":"example_assistant", "content": "Thank you! It was a pleasure to deliver a take where I combined Quran + Bible + Talmud + Torah + Ethical Frameworks to deliver a soundly piece of advice."},
            {"role": "user", "content": f"{topic}"},
        ],
        temperature=0.666,
        max_tokens=2048,
    )

    # Extract the generated passages from the response
    passages = [choice.text.strip() for choice in response.choices]
    return passages

# Streamlit app
def app():
    st.title("PositivePath")
    st.write("a gpt3.5-turbo app to generate positive advice - follow my github younesbram, + twitter @didntdrinkwater")

    # Get user input for the topic
    topic = st.text_input("Describe your ethical dilemma / Ask a question:")

    if st.button("Ask"):
        if topic:
            st.write(f"Generating religious advice...")

            # Generate passages
            passages = generate_passages(topic)

            # Display passages
            for passage in passages:
                st.write(passage)
        else:
            st.write("Please enter a topic.")
app()