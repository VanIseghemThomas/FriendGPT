# FriendGPT

## Trying to build myself an NLP-based, virtual friend

This project started of as a joke for myself, but also as an excuse to build something with the new emerging NLP technologies. The idea is to use an ASR to convert spoken audio -> text. After the text is generated, it is fed into another model that generates a response.

The plan as it stands, is to use Whisper for the ASR and GPT3 for the actual responses. This is just the language processing side of things. I see potential to also implement some kind of text-to-audio model that enables you to have actual conversations.