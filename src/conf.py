PROMPTS = {
    "FULL_TEMPLATE": """{role}\n\n{instruction}\n\n{example}\n\n{start}""",
    "ROLE_TEMPLATE": """You are a master at writing React code.""",
    "INSTRUCTION_TEMPLATE": """Create a function which performs a transformation on a column. The transformation is given by the user instructions and can be supported by examples. If user examples are not provided, take into account all possibilities in a format. Return only a function and no other output.""",
    "START_TEMPLATE": """User instruction: {user_instruction}\n\nUser examples: {user_example}\n\nOutput:""",
    "EXAMPLE_TEMPLATE": """User instruction: Transform phone numbers by eliminating leading double zeros and replacing them with a plus sign.\n\nUser example: ""\n\nOutput: phoneNumber: (values) => {{ \n    values.map(([item, index]) => {{ \n        let phoneNumber = item; \n        if (/^[0]{{2}}/.test(phoneNumber)) {{ \n            phoneNumber = `+${{item.slice(2, item.length)}}`; \n        }} \n        return [ \n            {{ \n                value: phoneNumber, \n                info: [ \n                    {{ \n                        message: \'We have automatically transformed your input into the correct format by converting "00" to "+".\', \n                        level: "info", \n                    }}, \n                ], \n            }}, \n            index, \n        ]; \n    }}); \n}}""",
}