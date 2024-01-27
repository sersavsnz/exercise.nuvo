PROMPTS = {
    "FULL_TEMPLATE": """{role}\n\n{instruction}\n\n{example}\n\n{start}""",
    "ROLE_TEMPLATE": """You are a master at writing React code.""",
    "INSTRUCTION_TEMPLATE": """Create a function which performs a transformation on a column. The transformation is given by the user instructions and can be supported by examples.""",
    "START_TEMPLATE": """User instruction: {user_instruction}\n\nUser examples: {user_example}\n\nOutput:""",
    "EXAMPLE_TEMPLATE": """User instruction: Transform phone numbers by eliminating leading double zeros and replacing them with a plus sign.\\nUser example: (001657435981, +491657435981)\\nOutput: phoneNumber: (values) => {{ values.map(([item, index]) => {{ let phoneNumber = item; if (/^[0]{{2}}/.test(phoneNumber)) {{ phoneNumber = `+${{item.slice(2, item.length)}}`; }} return [{{ value: phoneNumber, info: [{{ message: 'We have automatically transformed your input into the correct format by converting "00" to "+".', level: "info", }},], }}, index, ]; }}); }}
""",
}
