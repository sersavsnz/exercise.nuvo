from getpass import getpass

from flask import Flask, jsonify, request
from src.text2code import Text2Code


def run_t2c(user_input: str) -> str:
    """
    Runs text-to-code generation.
    """
    OPENAI_API_KEY = getpass()

    t2c = Text2Code(OPENAI_API_KEY)
    t2c.init_llm_chain()
    result = t2c.generate_code(user_input)

    return result


app = Flask(__name__)


@app.route("/t2c", methods=["POST"])
def get_response():
    """
    Input need to be in the following JSON format:
    {"user_input": {"user_instruction": "some instruction", "user_example": "some examples"}}
    """
    data = request.get_json()
    user_input = data.get("user_input")
    result = run_t2c(user_input)

    return jsonify({"response": result})


if __name__ == "__main__":
    app.run(debug=True)
