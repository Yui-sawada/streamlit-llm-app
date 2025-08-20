from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

load_dotenv()
st.title("提出課題")
st.write("このアプリは、日々の学習や日常の中で生じる様々な疑問について、選択した専門家に質問を投げかけることができます。")
st.write("質問内容を入力し、専門家の種類を選択してください。")
st.divider()

input_message=st.text_input(label="質問内容はなんですか？" )

selected_model = st.radio(
    label="専門家の種類を選択してください",
    options=["英語", "理科", "歴史"]
)

def generate_expert_answer(input_message, selected_model):
  if selected_model == "英語":
    system_message = "あなたは英語の専門家です。"
  elif selected_model == "理科":
    system_message = "あなたは理科の専門家です。"
  elif selected_model == "歴史":
    system_message = "あなたは歴史の専門家です。"

  llm= ChatOpenAI(model_name="gpt-4o-mini",temperature=0.5)
  messages=[
    SystemMessage(content=system_message),
    HumanMessage(content=input_message)
  ]
  result = llm(messages)
  return result.content

if st.button("送信"):
  st.divider()
  result = generate_expert_answer(input_message, selected_model)
  st.write(f"**回答:** {result}")