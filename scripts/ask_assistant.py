import json
import sys
import urllib.request


def ask_local_assistant(
    prompt: str,
    model: str = "qwen2.5-coder:3b",
    num_ctx: int = 2048,
) -> str:
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "system": (
            "You are a private local coding assistant for scalling-core "
            "(data infrastructure, labeling, and edge cases for physical AI/robotics). "
            "Write clean, practical Python/PyTorch code and concise technical steps."
        ),
        "prompt": prompt,
        "options": {"num_ctx": num_ctx},
        "stream": False,
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=180) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        return data.get("response", "")


def main() -> None:
    if len(sys.argv) < 2:
        print('Matumizi: python3 -m scripts.ask_assistant "swali au maelekezo yako"')
        sys.exit(1)
    question = " ".join(sys.argv[1:])
    print(ask_local_assistant(question))


if __name__ == "__main__":
    main()
