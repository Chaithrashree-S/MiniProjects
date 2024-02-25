import random

def generate_markov_chain(text, order=2):
    words = text.split()
    chain = {}

    for i in range(len(words) - order):
        prefix = tuple(words[i:i + order])
        suffix = words[i + order]
        if prefix in chain:
            chain[prefix].append(suffix)
        else:
            chain[prefix] = [suffix]

    return chain

def generate_text(chain, length=100, seed=None):
    if seed is not None:
        random.seed(seed)

    prefix = random.choice(list(chain.keys()))
    generated_words = list(prefix)

    for _ in range(length):
        suffix = random.choice(chain[prefix])
        generated_words.append(suffix)
        prefix = tuple(generated_words[-len(prefix):])

    return ' '.join(generated_words)

# Take input from user
text = input("Enter some text: ")
order = int(input("Enter the order of Markov chain (e.g., 1, 2, 3): "))
length = int(input("Enter the length of generated text: "))

chain = generate_markov_chain(text, order=order)
generated_text = generate_text(chain, length=length)
print("Generated text:")
print(generated_text)

