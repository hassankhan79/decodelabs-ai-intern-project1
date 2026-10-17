# decodelabs-ai-intern-project1
Rule-based CLI chatbot in Python using the IPO model (Decode Labs AI Internship, Project 1).
This project is a small command-line chatbot written in Python. It demonstrates the basic structure of an interactive program: accepting a user's message, preparing it for comparison, choosing a response, and continuing until the user exits.

## Project work

The chatbot runs from `main.py` and uses a dictionary of predefined responses. It currently recognizes these messages:

- `hello`
- `help`
- `who are you`
- `exit` to close the chatbot

Messages that do not match a predefined response receive a fallback message: "Sorry, I didn't understand that."

The code is organized into small functions:

- `sanitize()` removes extra spaces and converts text to lowercase so that inputs such as ` Hello ` and `HELLO` work consistently.
- `process()` looks up the cleaned message in the response dictionary.
- `main()` runs the conversation loop, handles empty input, and ends the program when the user types `exit`.

## How to run

Make sure Python is installed, then run:

```bash
python main.py
```

Example:

```text
Bot started. Type 'exit' to quit.
You: hello
Bot: Hi! How can I help you?
You: exit
Bot: Goodbye!
```

## IPO explanation

IPO means **Input, Process, Output**. It is a simple way to describe how a program works.

| IPO stage | In this project |
| --- | --- |
| **Input** | The user types a message at the `You:` prompt. |
| **Process** | The program cleans the message with `sanitize()`, checks whether it is `exit`, and otherwise finds a matching reply with `process()`. |
| **Output** | The chatbot prints a reply, such as `Bot: Hi! How can I help you?`, or prints a goodbye message and stops. |

In short, the chatbot takes text from the user, processes it using simple rules, and outputs an appropriate response.
