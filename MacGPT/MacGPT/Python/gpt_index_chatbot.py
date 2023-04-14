import os
from gpt_index import SimpleDirectoryReader, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain import OpenAI

def create_index(path):
    # Code from the article
    max_input = 4096
    tokens = 200
    chunk_size = 600
    max_chunk_overlap = 20

    promptHelper = PromptHelper(max_input, tokens, max_chunk_overlap, chunk_size_limit=chunk_size)

    llmPredictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="text-ada-001", max_tokens=tokens))

    docs = SimpleDirectoryReader(path).load_data()

    vectorIndex = GPTSimpleVectorIndex(documents=docs, llm_predictor=llmPredictor, prompt_helper=promptHelper)

    vectorIndex.save_to_disk('vectorIndex.json')

    return vectorIndex

def answer_question(vector_index_file, question):
    vIndex = GPTSimpleVectorIndex.load_from_disk(vector_index_file)
    response = vIndex.query(question, response_mode="compact")
    return response

if __name__ == "__main__":
    text_files_directory = "<path_to_your_text_files_directory>"
    create_index(text_files_directory)
