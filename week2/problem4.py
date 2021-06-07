import os
import sys


def main():
    # text for question
    h = "पायथन एक अद्भुत प्रोग्रामिंग भाषा है जिसके माध्यम से मैं बहुत कुछ हासिल कर सकता हूं।"

    print(h, type(h))
    # b. Variable type is string

    h_encoded = h.encode(encoding="utf-8")
    # it's good that above is explicing using the keyword argument (typically abbreviated to kwarg)
    print(h_encoded, type(h_encoded))

    # c. Type of encoded data is: bytes
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
