import os
from getpass import getpass

import conf
from dotenv import load_dotenv
from langchain.prompts import (
    FewShotPromptTemplate,
    PipelinePromptTemplate,
    PromptTemplate,
)
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import OpenAI

# OPENAI_API_KEY = getpass()


def main():
    load_dotenv()
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    llm = OpenAI(openai_api_key=OPENAI_API_KEY, model_name="gpt-3.5-turbo", temperature=0.0)
    full_template = conf.PROMPTS["FULL_TEMPLATE"]
    role_template = conf.PROMPTS["ROLE_TEMPLATE"]
    instruction_template = conf.PROMPTS["INSTRUCTION_TEMPLATE"]
    example_template = conf.PROMPTS["EXAMPLE_TEMPLATE"]
    start_template = conf.PROMPTS["START_TEMPLATE"]

    full_prompt = PromptTemplate.from_template(full_template)
    role_prompt = PromptTemplate.from_template(role_template)
    instruction_prompt = PromptTemplate.from_template(instruction_template)
    example_prompt = PromptTemplate.from_template(example_template)
    start_prompt = PromptTemplate.from_template(start_template)

    input_prompts = [
        ("role", role_prompt),
        ("instruction", instruction_prompt),
        ("example", example_prompt),
        ("start", start_prompt),
    ]
    pipeline_prompt = PipelinePromptTemplate(final_prompt=full_prompt, pipeline_prompts=input_prompts)

    result = llm.invoke(
        pipeline_prompt.format(
            user_example="(001658345423, +491658345423), (01743456732, +491743456732), (1845342361, +491845342361)",
            user_instruction="Format the phone numbers. For example, replace leading zeros by '+49'. See other examples",
        )
    )

    return result


# print(pipeline_prompt.input_variables)
# print(
#     pipeline_prompt.format(
#         user_example="(001658345423, +491658345423), (01743456732, +491743456732), (1845342361, +491845342361)",
#         user_instruction="Format the phone numbers. For example, replace leading zeros by '+49'. See other examples",
#     )
# )


# prompt = PromptTemplate.from_template("What is a good name for a company that makes {product}?")
# prompt.format(product="colorful socks")
